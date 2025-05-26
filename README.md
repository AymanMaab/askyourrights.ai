🧠 AskYourRights.AI
Empowering individuals to understand their legal rights through AI.

AskYourRights.AI is an AI-powered legal assistant designed to help users comprehend their rights by analyzing legal documents, such as the Universal Declaration of Human Rights. Utilizing Retrieval-Augmented Generation (RAG) techniques, this application provides accurate and context-aware answers to legal inquiries.

🚀 Features
PDF Upload: Seamlessly upload legal documents in PDF format.

Intelligent Parsing: Extract and process text using PDFPlumberLoader.

Text Chunking: Divide documents into manageable chunks with RecursiveCharacterTextSplitter.

Embeddings Generation: Create embeddings using OllamaEmbeddings.

Vector Store: Store and retrieve document embeddings with FAISS.

Conversational Interface: Engage in a Q&A session with the AI lawyer via Streamlit.

Custom Prompting: Utilize tailored prompts to ensure accurate and context-relevant responses.

🛠️ Installation
Clone the Repository:

bash
Copy
Edit
git clone https://github.com/AymanMaab/askyourrights.ai.git
cd askyourrights.ai
Create a Virtual Environment:

bash
Copy
Edit
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
Install Dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set Up Environment Variables:

Create a .env file in the root directory and add your API key:

env
Copy
Edit
GROQ_API_KEY=your_api_key_here
📄 Usage
Run the Streamlit Application:

bash
Copy
Edit
streamlit run frontend.py
Interact with the AI Lawyer:

Upload a legal PDF document.

Enter your legal question in the text area.

Receive context-aware answers based on the uploaded document.

📁 Project Structure
bash
Copy
Edit
askyourrights.ai/
├── pdfs/                         # Directory for uploaded PDF files
├── vector_db/                    # FAISS vector database storage
├── frontend.py                   # Streamlit frontend application
├── rag_pipeline.py               # RAG pipeline implementation
├── vector_database.py            # Vector database setup and management
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables
└── README.md                     # Project documentation
🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

📄 License
This project is licensed under the MIT License.

📫 Contact
For any inquiries or feedback, please contact Ayman Maab.
