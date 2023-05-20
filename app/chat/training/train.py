import os
import pandas as pd
import matplotlib.pyplot as plt
from transformers import GPT2TokenizerFast
from langchain.document_loaders import DataFrameLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.agents import create_pandas_dataframe_agent


os.environ["OPENAI_API_KEY"] = "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"

#finds and reads faq.csv
script_path = os.path.abspath(__file__)
faq_path = os.path.join(os.path.dirname(script_path), 'docs', 'faq.csv')
df = pd.read_csv(faq_path)

loader = DataFrameLoader(df, page_content_column="question")
print(loader.load())


#inputs question to chatbot and runs on faq.csv
# pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)
# pd_agent.run("where are exams held?")