# ⚖️ AskYourRights.AI

**Understand your rights — without needing a law degree.**

AskYourRights.AI is an AI-powered legal assistant that helps users query legal documents, such as the Universal Declaration of Human Rights, and get context-aware answers. It uses Retrieval-Augmented Generation (RAG) with a conversational interface to bring clarity to complex legal text.

---

## 🚀 Features

- 📄 Upload and process PDF documents
- 🧠 Ask natural language questions and get informed answers
- 🔍 Uses FAISS vector store for fast similarity search
- 🗂️ Text splitting and embedding with LangChain
- 🤖 Powered by DeepSeek models and Groq LLMs
- 💬 Built with Streamlit for an intuitive chat experience

---

## 🛠 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/AymanMaab/askyourrights.ai.git
   cd askyourrights.ai
````

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv myenv
   myenv\Scripts\activate        # On Windows
   source myenv/bin/activate     # On macOS/Linux
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add your API Key**
   Create a `.env` file in the root folder:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## 📦 File Structure

```
askyourrights.ai/
├── pdfs/                    # Uploaded PDF files
├── vector_db/               # FAISS vector storage
├── rag_pipeline.py          # RAG logic with Groq LLM
├── vector_database.py       # PDF loading, chunking, embedding
├── frontend.py              # Streamlit app
├── requirements.txt         # Dependencies
├── .env                     # Your API key
└── README.md
```

---

## 💡 Usage

Run the Streamlit app:

```bash
streamlit run frontend.py
```

1. Upload a legal PDF (e.g. constitution, declaration, etc.)
2. Ask a legal question in natural language
3. Get an answer backed by the document context

---

## 🧠 Tech Stack

* [LangChain](https://www.langchain.com/)
* [Groq](https://groq.com/) LLMs (e.g. `deepseek-r1`)
* [FAISS](https://github.com/facebookresearch/faiss) for vector search
* [Streamlit](https://streamlit.io/) for the UI
* [Ollama Embeddings](https://github.com/ollama) for vectorization

---

## 🤝 Contributing

Got an idea? Found a bug? PRs are welcome.
Please open an issue or submit a pull request to collaborate!

---

## 📄 License

MIT License. See [LICENSE](LICENSE) for details.

---

## 🙋‍♂️ Author

Made with ❤️ by [Ayman Maab](https://github.com/AymanMaab)
Let’s make the law more accessible — one prompt at a time.
