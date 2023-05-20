import os
import pandas as pd
import matplotlib.pyplot as plt
from transformers import GPT2TokenizerFast
from langchain.document_loaders import PyPDFLoader
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



# Split the dataframe by rows
chunks = [df.iloc[[i]] for i in range(len(df))]

# Iterate over the chunks and process them as needed
for i, chunk in enumerate(chunks):
    # Process the chunk (add to vector database, perform operations, etc.)
    
    # Print the chunk as an example
    print(f"Chunk {i+1}:\n{chunk}")


#inputs question to chatbot and runs on faq.csv
pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)
pd_agent.run("where are exams held?")


# import pandas as pd
# from langchain.document_loaders import DataFrameLoader
# from langchain.chat_models import ChatOpenAI
# from langchain.vectorstores import Chroma
# from langchain.chains import RetrievalQA
# from langchain.prompts import PromptTemplate
# from langchain.embeddings import OpenAIEmbeddings
# from langchain import ConversationChain

# OPENAI_API_KEY = "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"

# faq_url = r"C:\Users\61433\Desktop\UNI\CITS3403\Project\CITS3403-Project\app\chat\training\docs\faq.csv"
# faq_training = pd.read_csv(faq_url)


# llm = OpenAI()
# conversation = ConversationChain(llm=llm, verbose=True)

# # medium_loader = DataFrameLoader(medium, page_content_column="question")
# # medium_data = medium_loader.load()
# # print(len(medium_data))

# # # Define other variables

# # embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# llm = ChatOpenAI(
#     model_name="gpt-3.5-turbo",
#     temperature=0,
#     openai_api_key=OPENAI_API_KEY,
#     max_tokens=512,
# )

# response_template = """
# As a UWA question bot, your goal is to provide accurate and helpful information about the University of Western Australia based on Frequently asked Questions (FAQs).
# You should answer user inquiries based on the context provided and avoid making up answers.
# If you don't know the answer, simply state that you don't know.

# {context}

# Question: {question}"""

# SALES_PROMPT = PromptTemplate(
#     template=response_template, input_variables=["context", "question"]
# )

# sales_qa = RetrievalQA.from_chain_type(
#     llm=llm,
#     chain_type="map_reduce",
#     retriever=Chroma.from_documents(medium_data, embeddings).as_retriever(),
#     chain_type_kwargs={},
# )


# print(sales_qa.run("Where can I sit my exams"))
