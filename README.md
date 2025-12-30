# LangGraph Chatbot Agent

## Description
This project is an interactive AI-powered application that uses LangGraph, LangChain, and Groq-based LLMs to process natural language queries.It features a Streamlit frontend and a LangGraph backend,
making it suitable for lightweight research,AI experimentation, and custom tool integration.

## Features
- LangGraph Agent: Modular, graph-based stateful LLM agent
- Streamlit UI: Simple web interface to input and view responses
- Environment Separation: Secure handling of API keys via .env
- Modular Backend: Easily extend tools, memory, and workflows
- Fast LLM API: Uses ChatGroq (Gemma-2B model) for inference

## Tools Used
- Visual Studio Code
- Git for version control
- LangGraph for conversation management
- Groq API
- Python's type hinting for code reliability

## Project Implementation

### 1. Project Setup
- **Dependencies Management**: Uses requirement.txt to install LangGraph, LangChain, Streamlit, and langchain_groq.
- **Environment Configuration**: API keys and environment variables are securely stored in the .env file.
- **Project Structure**: Clean separation between backend (langGraph_backend.py) and frontend (frontend.py) logic.

### 2. Core Implementation
- **LangGraph Integration**: Implements StateGraph to define multi-step conversational agents.
- **Groq LLM Integration**: Uses ChatGroq with the Gemma-2B model for generating LLM responses.
- **State Management**: Uses ChatState and tool inputs to preserve context and manage dynamic agent behavior.
