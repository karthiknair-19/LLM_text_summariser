import os
import streamlit as st
import pickle
import time
from langchain import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv
load_dotenv()  

st.title("Alexy The Summarizer")
st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_vector_store.pkl"

main_placeholder = st.empty()
llm = OpenAI(temperature=0.6, max_tokens=500,model='gpt-3.5-turbo-instruct')

if process_url_clicked:
    
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("The data has started loading ...✅✅✅")
    data = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("The data is being splitted into chunks... ⚙️⚙️⚙️")
    texts = text_splitter.split_documents(data)
    
    embeddings = OpenAIEmbeddings()
    faiss=FAISS.from_documents(texts, embeddings)
    main_placeholder.text("Embeddings are getting stored.....📩📩📩")
    time.sleep(2)
    faiss.save_local(file_path)
    

question = main_placeholder.text_input("Question: ")
if question :
    if os.path.exists(file_path):
            vectordb=FAISS.load_local(file_path,OpenAIEmbeddings())
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectordb.as_retriever())
            result = chain({"question": question}, return_only_outputs=True)
            st.header("Answer")
            st.write(result["answer"])

            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  
                for source in sources_list:
                    st.write(source)



