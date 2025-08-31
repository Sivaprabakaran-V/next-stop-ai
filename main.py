from dotenv import load_dotenv
from langchain.agents import AgentExecutor
from langchain.agents.react.agent import create_react_agent
from langchain_core.output_parsers.pydantic import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI

from schemas import AgentResponse
from prompt import REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS 

# Load environment variables
load_dotenv()

# Tools and LLM
tools = [TavilySearch()]
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

# Output parser
output_parser = PydanticOutputParser(pydantic_object=AgentResponse)

# Prompt template with format instructions
react_prompt_with_format = PromptTemplate(
    template=REACT_PROMPT_WITH_FORMAT_INSTRUCTIONS,
    input_variables=["input"],   # only input needed
).partial(format_instructions=output_parser.get_format_instructions())

# Create the agent
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt_with_format,
)

# Executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Extract + parse outputs
extract_output = RunnableLambda(lambda x: x.get("output"))
parse_output = RunnableLambda(lambda x: output_parser.parse(x))

# Chain them
chain = agent_executor | extract_output | parse_output

def main():
    result = chain.invoke(
        {
            "input": "search for 3 job postings for an Information security Manager using LangChain in the Bay Area on LinkedIn and list their details"
        }
    )
    print(result)

if __name__ == "__main__":
    main()
