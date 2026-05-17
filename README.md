# 🤖 Multiple AI Agents System

A powerful multi-agent AI application built using LangGraph, LangChain, Groq LLMs, and Streamlit. This project demonstrates how multiple AI agents collaborate to solve complex tasks like research, web search, Wikipedia queries, and intelligent reasoning workflows.

## 🚀 Features

✨ Multi-Agent Collaboration using LangGraph  
🔎 Real-time web search using DDGS  
📖 Wikipedia knowledge retrieval  
📄 Arxiv research paper search  
🧠 LLM reasoning using Groq (Llama models)  
💬 Interactive Streamlit UI  
⚡ Fast and structured AI responses  

## 🏗️ Architecture

🧠 Supervisor Agent → decides which agent to call  
🔎 Search Agent → performs web search  
📖 Wikipedia Agent → fetches factual knowledge  
📄 Arxiv Agent → retrieves research papers  
🤖 LLM (Groq) → generates final response  

## 🛠️ Tech Stack

Python, Streamlit, LangChain, LangGraph, Groq API, DDGS, Wikipedia API, Arxiv API, python-dotenv  

## 📦 Installation

git clone https://github.com/divyasreevemula918/Multiple_AI_Agents.git  
cd Multiple_AI_Agents  
pip install -r requirements.txt  

## ▶️ Run the App

streamlit run application.py  

## 🔐 Environment Variables

Create a .env file and add:

GROQ_API_KEY=your_groq_api_key  
LANGCHAIN_API_KEY=your_langchain_api_key  

## 📁 Project Structure

Multiple_AI_Agents/  
├── application.py  
├── agents/  
├── tools/  
├── graph/  
├── requirements.txt  
├── .env  
└── README.md  

## 💡 Example Queries

Latest AI research papers  
Explain reinforcement learning  
Who is Alan Turing?  
Recent SpaceX updates  

## ⚠️ Notes

Ensure stable dependencies in Streamlit Cloud  
Some tools require internet access  
Use correct API keys in .env file  

## 🌟 Future Improvements

Add memory to agents  
Voice-based interaction  
Better routing in LangGraph  
Docker deployment  

## 👩‍💻 Author

Divya  
https://github.com/divyasreevemula918  

## 📜 License

MIT License
