import streamlit as st
import functions

import os 
from langchain_groq import ChatGroq

# setup groq api keys
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    temperature=0,
    model_name="llama-3.1-8b-instant",
    groq_api_key=GROQ_API_KEY 
)

def streamlit_app(text):
    code = functions.get_workflow(text, llm)
    local_vars = {}
    exec(code, globals(), local_vars)
    create_graph = local_vars.get("create_graph")
    graph = create_graph()
    return graph

st.title("Method Section Workflow Generator")

text = st.text_input("Enter method section")

if st.button("Submit"):
    if text:
        output = streamlit_app(text)
        st.image(output, caption="Generated Workflow Graph")
    else:
        st.warning("Please enter a method section.")


st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: white;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        <p>Created by <a href="https://www.linkedin.com/in/mohamedfadlalla-ai/" target="_blank">Mohamed Fadlalla</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
