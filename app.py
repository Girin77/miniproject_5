# =========================================
# SIMPLE AI CHATBOT USING OLLAMA
# AND STREAMLIT
# =========================================

# Import Streamlit
import streamlit as st

# Import Ollama
import ollama


# Title of the application

st.title("Simple AI Chatbot")


# Small description

st.write("Ask a question and get an answer from a local AI model.")


# Create a text box for the user

question = st.text_input("Enter your question:")


# Create an Ask AI button

if st.button("Ask AI"):

    # Check if the user entered something

    if question:

        # Send the question to Ollama

        response = ollama.chat(
            model="llama3.2:1b",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        # Get the answer from Ollama

        answer = response["message"]["content"]


        # Display the answer

        st.subheader("AI Response")

        st.write(answer)

    else:

        # Display a message if no question was entered

        st.warning("Please enter a question.")