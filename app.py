import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
# database like pincone , it runs locally, stores generated embeddings in own machine
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmltemplates import css, bot_template, user_template

def get_text_from_pdf(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    
    return text

def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap = 200,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

def create_vectore_store(chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore

def create_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

def handle_user_input(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i%2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)



def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with multiple pdfs", page_icon=":student:")
    st.header("Explore Books using GPT :books:")
    st.write(css, unsafe_allow_html=True)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    user_question = st.text_input("Ask a question about your document:")
    if user_question:
        handle_user_input(user_question)

    with st.sidebar:
        st.subheader("Your documents:")
        pdf_docs = st.file_uploader("Upload your documents here and process", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner():
                # extract texts from pdf
                raw_text = get_text_from_pdf(pdf_docs)

                #get text chunks
                chunks = get_text_chunks(raw_text)

                # create vector store
                vectore_store = create_vectore_store(chunks)

                st.session_state.conversation = create_conversation_chain(vectore_store)

if __name__ == '__main__':
    main()