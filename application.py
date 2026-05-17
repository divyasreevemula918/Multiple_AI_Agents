import streamlit as st
from langchain_groq import ChatGroq
import wikipedia
from ddgs import DDGS
import arxiv

# ----------------------------
# 🔑 API KEY
# ----------------------------
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"] = os.environ.get("GROQ_API_KEY")

# ----------------------------
# 🤖 MODEL
# ----------------------------
llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

# ----------------------------
# 📚 TOOLS
# ----------------------------
def wikipedia_tool(query):
    try:
        return wikipedia.summary(query, sentences=3)
    except:
        return "No Wikipedia result found."

def duckduckgo_tool(query):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append({
                "title": r["title"],
                "snippet": r["body"],
                "url": r["href"]
            })
    return results

def arxiv_tool(query):
    search = arxiv.Search(
        query=query,
        max_results=3,
        sort_by=arxiv.SortCriterion.Relevance
    )

    papers = []
    for p in search.results():
        papers.append({
            "title": p.title,
            "summary": p.summary,
            "url": p.entry_id
        })
    return papers

# ----------------------------
# 🧠 TOOL ROUTER
# ----------------------------
def choose_tool(query):
    prompt = f"""
Pick ONE tool:
- wikipedia
- duckduckgo
- arxiv

Query: {query}

Return only one word.
"""
    result = llm.invoke(prompt).content.lower()

    if "wiki" in result:
        return "wikipedia"
    elif "arxiv" in result:
        return "arxiv"
    return "duckduckgo"

# ----------------------------
# 🧠 AGENT
# ----------------------------
def run_agent(query):
    tool = choose_tool(query)

    if tool == "wikipedia":
        output = wikipedia_tool(query)

    elif tool == "arxiv":
        output = arxiv_tool(query)

    else:
        output = duckduckgo_tool(query)

    final_prompt = f"""
User Query: {query}

Tool Used: {tool}

Tool Output: {output}

Give a clean, structured answer with bullet points if needed.
"""

    response = llm.invoke(final_prompt)

    return response.content, tool, output

# ----------------------------
# 🎨 UI CONFIG
# ----------------------------
st.set_page_config(page_title="Groq AI Agent", page_icon="🧠", layout="wide")

st.title("🧠 Groq AI Multi-Tool Assistant using Langgraph")
st.caption("Wikipedia 📚 | Arxiv 📄 | Web Search 🔍 | Powered by Groq ⚡")

# ----------------------------
# SIDEBAR
# ----------------------------
with st.sidebar:
    st.header("⚙️ Settings")
    model_temp = st.slider("Creativity (temperature)", 0.0, 1.0, 0.3)

    st.markdown("---")
    st.info("Tip 💡: Ask research, coding, or trending questions")

# ----------------------------
# MEMORY
# ----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ----------------------------
# CHAT DISPLAY
# ----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ----------------------------
# INPUT
# ----------------------------
user_query = st.chat_input("Ask anything...")

if user_query:

    # user message
    st.session_state.messages.append({"role": "user", "content": user_query})

    with st.chat_message("user"):
        st.write(user_query)

    with st.chat_message("assistant"):

        with st.spinner("Thinking + using tools ⚙️..."):
            answer, tool, tool_output = run_agent(user_query)

        st.markdown("### 🤖 Answer")
        st.write(answer)

        # ----------------------------
        # TOOL DETAILS (EXPANDABLE)
        # ----------------------------
        with st.expander(f"🔧 Tool Used: {tool}", expanded=False):
            st.write(tool_output)

        # ----------------------------
        # EXTRA VISUAL TABS
        # ----------------------------
        tab1, tab2 = st.tabs(["📌 Answer", "🔍 Raw Tool Data"])

        with tab1:
            st.success(answer)

        with tab2:
            st.json(tool_output)

    # save assistant message
    st.session_state.messages.append({"role": "assistant", "content": answer})