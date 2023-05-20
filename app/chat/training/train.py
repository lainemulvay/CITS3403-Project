import os
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.agents import create_pandas_dataframe_agent
from langchain.chains import RetrievalQA
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.chat_models import ChatOpenAI


os.environ["OPENAI_API_KEY"] = "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"

#finds and reads faq.csv
script_path = os.path.abspath(__file__)
faq_path = os.path.join(os.path.dirname(script_path), 'docs', 'faq.csv')
loader = CSVLoader(faq_path, encoding='utf-8')
question_bank = loader.load()

embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(question_bank, embeddings)
retriever = db.as_retriever()

def perform_query(query):
    qa = RetrievalQA.from_chain_type(llm=ChatOpenAI(model_name='gpt-3.5-turbo'), chain_type="stuff", retriever=retriever)
    response = qa.run(query)
    return response

print(perform_query(input("Enter a question: ")))

# loader = DataFrameLoader(df, page_content_column="question")


# embeddings = OpenAIEmbeddings()


# db = Chroma.from_documents(question_bank, embeddings)
# retriever = db.as_retriever(embeddings=embeddings)

# qa = RetrievalQA.from_chain_type(llm=OpenAI(model_name='gpt-3.5-turbo'), chain_type="stuff", retriever=retriever)
# query = "explin UniPrint?"
# response = qa.run(query)
# # docs = db.similarity_search(query, k=3)
# # print(docs)

# # index = VectorstoreIndexCreator().from_loaders([loader])
# # response = index.query(query)
# print(response)


#inputs question to chatbot and runs on faq.csv
# pd_agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=True)
# pd_agent.run("where are exams held?")