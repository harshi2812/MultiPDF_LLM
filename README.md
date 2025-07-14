# 📚 Chat with Multiple PDFs using LangChain

This project is a **multi-document Q&A chatbot** that allows users to **chat with multiple PDF files** using a clean, interactive **Streamlit** interface. It implements **LangChain**, **FAISS**, and **OpenAI** or **Hugging Face LLMs** to extract answers from uploaded PDFs.

---

## 🚀 Features

- 💬 Conversational interface to query multiple PDFs.
- 🧠 Powered by **LangChain**, **FAISS vector store**, and **RAG pipeline**.
- 📄 Embeds and indexes PDF content for fast semantic search.
- 🤖 Works with **OpenAI**, **HuggingFace**, or custom LLMs.
- 🎨 Custom chat UI with avatars and improved styling.
- 📦 Lightweight, runs locally or can be deployed on Streamlit Cloud.

---

## 📂 Folder Structure

MULTIPLE-PDF-CONVERTER/
├── app.py # Streamlit frontend & main logic
├── htmlTemplates.py # HTML + CSS chat templates
├── requirements.txt # Python dependencies
├── images/
│ ├── image1.png # User avatar
│ └── image2.png # Bot avatar

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/harshi2812/MultiPDF_LLM.git
cd MultiPDF_LLM
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

#INCLUDE THIS
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token

#RUNNING
streamlit run app.py
```
🧠 How It Works
Upload PDFs: User uploads multiple PDF documents.

Text Extraction: Raw text is extracted from each PDF.

Text Chunking: Text is split into manageable semantic chunks.

Vector Store: FAISS is used to embed and store chunks.

Conversational Chain: LangChain retrieves relevant chunks and uses an LLM to generate responses.

📌 Tech Stack
LangChain

FAISS (Vector store)

OpenAI / HuggingFace LLMs

Streamlit

Python

🧩 Future Improvements
Voice input using Whisper

Audio output via TTS

Support for DOCX and TXT files

Save and revisit chat history

📄 License
MIT License — feel free to fork and use.

🙋‍♂️ Author
Built with ❤️ by Harshil Handoo

