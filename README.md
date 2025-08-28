# ReAct Agent with LangChain, Google Generative AI, and Tavily Search

This project demonstrates how to build a **ReAct (Reasoning + Acting) Agent** using [LangChain](https://www.langchain.com/), Google's **Gemini** LLM, and **Tavily Search** as a tool. The agent is capable of structured reasoning, performing searches, and outputting results in a **validated Pydantic schema**.

---

## Features
- Uses **Google Gemini (gemini-1.5-flash)** as the LLM.
- Integrates **Tavily Search API** for web results.
- Implements **ReAct Agent** reasoning and action loop.
- Outputs results using a **Pydantic schema** for structured data validation.
- Supports **custom prompt templates** with format instructions.

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/react-agent.git
   cd react-agent
2. ** Project Structure **
   .
├── main.py               # Entry point
├── schemas.py            # Pydantic schema (AgentResponse)
├── prompt.py             # Prompt template
├── requirements.txt      # Dependencies
├── .env.example          # Sample env vars (not committed)
└── README.md             # Documentation

3. ** environment variables**
   GOOGLE_API_KEY=your_google_api_key
   TAVILY_API_KEY=your_tavily_api_key

4. ** Requirement**
   langchain
   langchain-google-genai
   langchain-tavily
   python-dotenv
   pydantic

