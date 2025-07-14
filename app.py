# -*- coding: utf-8 -*-
import streamlit as st
import os
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain_community.embeddings import HuggingFaceInstructEmbeddings

from htmlTemplates import css, bot_template, user_template

from langchain.chains import ConversationalRetrievalChain

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    #embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore



from langchain.llms import HuggingFacePipeline
from transformers import pipeline

def get_conversation_chain(vectorstore):
    # Load model using HuggingFace pipeline
    hf_pipeline = pipeline(
        "text2text-generation",
        model="google/flan-t5-base",  # lightweight & free
        tokenizer="google/flan-t5-base",
        max_length=512,
        temperature=0.3
    )

    llm = HuggingFacePipeline(pipeline=hf_pipeline)

    memory = ConversationBufferMemory(
        memory_key='chat_history',
        return_messages=True
    )

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )

    return conversation_chain



def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
def main():
    load_dotenv()
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    st.set_page_config(page_title="Chat with PDFs", page_icon="📚", layout="wide")
    st.markdown(css, unsafe_allow_html=True)

    # Header Section
    st.markdown("""
    <div style='text-align: center; margin-bottom: 2rem;'>
        <h1 style='font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; 
                   color: #f1c40f; background: linear-gradient(to right, #2c3e50, #34495e); 
                   padding: 20px 30px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);'>
            Chat with Multiple PDFs 📚
        </h1>
    </div>
    """, unsafe_allow_html=True)

    # Session state setup
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # User question input
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)

    # Sidebar UI
    with st.sidebar:
        st.image("https://i.ibb.co/TgRdx0D/pdf-image.png", use_column_width=True)
        st.markdown("""
            <h2 style="color:#e67e22;">📄 Upload your PDFs</h2>
            <p style="font-size: 16px; color:#ecf0f1;">Supports multiple files. After uploading, click <b>'Process'</b>.</p>
        """, unsafe_allow_html=True)

        pdf_docs = st.file_uploader("Upload PDFs and click 'Process'", accept_multiple_files=True)

        if pdf_docs and st.button("Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                vectorstore = get_vectorstore(text_chunks)
                st.session_state.conversation = get_conversation_chain(vectorstore)
                st.session_state.chat_history = []

if __name__ == '__main__':
    main()
