import requests
from bs4 import BeautifulSoup
import pandas as pd

from langchain.document_loaders import (
    DataFrameLoader
)
from langchain.text_splitter import CharacterTextSplitter
from langchain.schema import Document
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, Tool


# from langchain.agents import create_pandas_dataframe_agent
# from langchain.llms import OpenAI
# import pandas as pd
# import os

# os.environ["OPENAI_API_KEY"] = "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"

# faq_url = "C:/Users/61433/Desktop/UNI/CITS3403/Project/CITS3403-Project/app/chat/training/docs/faq.csv"

# df = pd.read_csv(faq_url)

# pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)

# pd_agent.run("where are exams held?")


# Medium
article_url = "https://raw.githubusercontent.com/tomasonjo/blog-datasets/main/medium/neo4j_articles.csv"
medium = pd.read_csv(faq_url)
medium_loader = DataFrameLoader(medium, page_content_column="text")
medium_data = medium_loader.load()
medium_data_split = splitter.split_documents(medium_data)
print(len(medium_data_split))


# Define embedding model
OPENAI_API_KEY = "OPENAI_API_KEY"
embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

sales_store = Chroma.from_documents(
    medium_data_split, embeddings, collection_name="faq"
)

llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0,
    openai_api_key=OPENAI_API_KEY,
    max_tokens=512,
)

response_template = """As a Neo4j question bot, your goal is to provide accurate and helpful information about the University of Western Australia based on Frequently asked Questions (FAQs),
You should answer user inquiries based on the context provided and avoid making up answers.
If you don't know the answer, simply state that you don't know.
{context}

Question: {question}"""
SALES_PROMPT = PromptTemplate(
    template=response_template, input_variables=["context", "question"]
)
sales_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=sales_store.as_retriever(),
    chain_type_kwargs={"prompt": SALES_PROMPT},
)

print(sales_qa.run("Where can I sit my exams"))