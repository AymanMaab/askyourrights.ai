from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings  # ✅ use the new package

from langchain_community.vectorstores import FAISS
from tomlkit import document

# Step 1: Upload & Load raw PDF files

pdfs_directory = "pdfs/"

def upload_pdf(file):
    with open(pdfs_directory + file.name, "wb") as f:
        f.write(file.getbuffer())
        

def load_pdf(file_path):
    """Load a PDF file and return its content."""
    loader = PDFPlumberLoader(file_path)
    documents = loader.load()
    return documents

file_path = 'universal_declaration_of_human_rights.pdf'
documents = load_pdf(file_path)
#print(len(documents))  # Print number of documents loaded


# Step 2: Create Chunks of text from the PDF
def create_chuncks(documents):
    """Create chunks of text from the loaded documents."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000, 
        chunk_overlap = 200,
        add_start_index = True)
    text_chunks = text_splitter.split_documents(documents)
    return text_chunks

text_chunks = create_chuncks(documents)
#print("Chunks count:", len(text_chunks))  # Print number of text chunks created



# Step 3: Setup Embeddings Model (Use DeepSeel R1 with Ollama)
ollama_model_name = "deepseek-r1:1.5b"
def get_embeddings_model(ollama_model_name):
    """Get the Ollama embeddings model."""
    embeddings = OllamaEmbeddings(model=ollama_model_name)
    return embeddings


# Step 4: Index Documents Store embeddings in FAISS (vector database)
FAISS_DB_PATH = "vector_db/db_faiss"
faiss_db = FAISS.from_documents(text_chunks, get_embeddings_model(ollama_model_name))
faiss_db.save_local(FAISS_DB_PATH)
