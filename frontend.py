from rag_pipeline import answer_query, retrieve_docs, llm_model
import streamlit as st

# Add the title
st.title("KnowYourRights.AI")

# Step 1: Setup Upload PDF functionality
uploaded_file = st.file_uploader("Upload PDF", 
                                 type="pdf", 
                                 accept_multiple_files=False)

# Step 2: Chatbot Skeleton (Question and Answer)
user_query = st.text_area("Enter your prompt here: ", height=150, placeholder="Type your question...")

ask_question = st.button("Ask AI Lawyer")
if ask_question:

    if uploaded_file:
        st.chat_message("User").write(user_query)
        # Here you would typically process the PDF and generate a response

        # RAG Pipeline
        retrieve_docs = retrieve_docs(user_query)
        response = answer_query(documents=retrieve_docs, model=llm_model, query=user_query).content
       # fixed_response = "Hi, this is a fixed response from the AI Lawyer."
        st.chat_message("AI Lawyer").write(response)

    else:
        st.error("Please upload a PDF document before asking a question.")