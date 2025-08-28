from langchain.prompts.prompt import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

def main():
    print("Summarizer Agent starting...")
    df = pd.read_csv(
    r"C:\Users\sivap\OneDrive\Desktop\akira.txt",
    header=None,
    names=["text"],
    delimiter="\t",   # force pandas to not split on commas
    engine="python"
)

    information = " ".join(df["text"].tolist())

    summary_template = """ Given the information {information} about a person, I want you to create:
    1. A short summary  
    2. Two interesting facts about them
    3. best movie they directed
    """

    summary_prompt_template = PromptTemplate(input_variables = ["information"], template= summary_template)
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  
        google_api_key=os.getenv("GOOGLE_API_KEY"),        
        temperature=0
    )
    chain = summary_prompt_template | llm | StrOutputParser()
    result = chain.invoke(input={"information": information})
    print(result)
    
if __name__ == "__main__":
    main()



