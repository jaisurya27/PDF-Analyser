# PDF-Analyser
GPT-powered PDF Analyser. Upload Multiple PDFs and chat with them. 

## Overview
PDF-Analyser is a Python project developed to facilitate interactive and semantic search on text extracted from multiple PDFs. It utilizes Streamlit for the user interface, Langchain for text extraction and chunking, and OpenAI GPT-3.5 for generating relevant results based on user queries.
![Screenshot 2024-01-08 163327](https://github.com/jaisurya27/PDF-Analyser/assets/64311010/087a8e62-2475-4462-9e34-c9e7ba9b438e)

## Features
- PDF Upload: Multiple PDFs can be uploaded simultaneously.
- Chunking: Converts extracted text into manageable chunks.
- Vector Database: Stores the text chunks in a vector database (FAISS).
- Chat Interface: Provides a user-friendly chat screen for interacting with the PDF data.
- Semantic Search: Performs a semantic search on the vector store using user queries.
- GPT-3.5 Integration: Passes vector results to OpenAI GPT-3.5 for generating relevant 
- Chat History: Preserves chat history to maintain context for generating more coherent responses.

## Installation
1. Clone the Repository
```
git clone https://github.com/jaisurya27/PDF-Analyser.git
```
2. Navigate to the project directory
3. Install the required dependencies
```
pip install -r requirements.txt
```
4. Add OPENAPI key to .env file
```
OPENAI_API_KEY=your_secrit_api_key
```

## Usage
1. Run the streamlit app
```
streamlit run app.py
```
2. Open your browser and navigate to http://localhost:8501 to access the PDF-Analyser interface
3. Upload PDFs and start interacting with the chat interface to retrieve relevant information from the PDF data. 
4. The chat history will also be preserved for a more contextual conversation.

![Screenshot 2024-01-08 163340](https://github.com/jaisurya27/PDF-Analyser/assets/64311010/33865f95-f7b5-47dd-afe3-9adbef4a7c26)
