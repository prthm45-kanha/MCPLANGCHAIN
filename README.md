# MCPLANGCHAIN

A project integrating Model Context Protocol (MCP) servers with LangChain and LangGraph, using Groq LLM agents.

## Features

- **Multi-Server MCP Client**: Connects to multiple MCP servers using `langchain-mcp-adapters`.
- **FastMCP Servers**:
  - `mathserver.py`: Standard I/O (`stdio`) MCP server providing arithmetic operations (`add`, `multiple`).
  - `weather.py`: Streamable HTTP MCP server providing location weather tools.
- **LangGraph ReAct Agent**: Coordinates tool calling between FastMCP servers and ChatGroq (`qwen/qwen3.8-27b`).

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/prthm45-kanha/MCPLANGCHAIN.git
   cd MCPLANGCHAIN
   ```

2. **Configure environment variables:**
   Copy `.env.example` to `.env` and add your Groq API key:
   ```bash
   cp .env.example .env
   ```
   Edit `.env`:
   ```env
   GROQ_API_KEY="your_groq_api_key_here"
   ```

3. **Install dependencies:**
   Using `uv`:
   ```bash
   uv sync
   ```
   Or using `pip`:
   ```bash
   pip install -r requirement.txt
   ```

## Running the Project

1. Run the weather server (streamable HTTP):
   ```bash
   python weather.py
   ```

2. In another terminal, run the client agent:
   ```bash
   python client.py
   ```
