from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
import os

os.environ["OPENAI_API_KEY"] = "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"

faq_url = "C:/Users/61433/Desktop/UNI/CITS3403/Project/CITS3403-Project/app/chat/training/docs/faq.csv"

df = pd.read_csv(faq_url)

pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)

pd_agent.run("where are exams held?")
