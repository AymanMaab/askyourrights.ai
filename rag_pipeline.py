from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from vector_database import faiss_db
from langchain_core.prompts import ChatPromptTemplate


# Step 1: Setup LLM (Use DeepSeek R1 with Groq)

llm_model = ChatGroq(model="deepseek-r1-distill-llama-70b")

# Step 2: Retrieve Docs

def retrieve_docs(query):
    """Retrieve documents from the FAISS vector database based on the query."""
    return faiss_db.similarity_search(query)  # FIXED: Added return statement
    

def get_context(documents):
    """Get context from the retrieved documents."""
    if documents is None or len(documents) == 0:
        return "No relevant documents found."
    
    context = "\n\n".join([doc.page_content for doc in documents])
    return context

# Step 3: Generate Answer

custom_prompt = """
Use the pieces of information provided in the context to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Don't provide anything out of the given context.
Question: {question}
Context: {context}
Answer:
"""

def answer_query(documents, model, query):
    context = get_context(documents)
    prompt = ChatPromptTemplate.from_template(custom_prompt)
    chain = prompt | model
    return chain.invoke({"question": query, "context": context})

# # Main execution
# question = "if a government forbids the to assemble peacefully, which articles are violated and why?"
# retrieved_docs = retrieve_docs(question)  # FIXED: Changed variable name for clarity

# # Add some debugging
# print(f"Retrieved {len(retrieved_docs) if retrieved_docs else 0} documents")

# if retrieved_docs:
#     answer = answer_query(documents=retrieved_docs, model=llm_model, query=question)
#     print("AI Lawyer: ", answer.content)  # Extract just the content
# else:
#     print("No documents retrieved. Check your vector database.")