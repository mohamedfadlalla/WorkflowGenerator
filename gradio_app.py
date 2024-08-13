import streamlit as st
import functions
import os
from langchain_groq import ChatGroq
import platform

# Set page configuration
st.set_page_config(page_title="Method Section Workflow Generator", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .main {
        background: #ffffff;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f0f2f6;
        color: #333333;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
</style>
""", unsafe_allow_html=True)

# Setup Groq API
if platform.system() == "Windows":
    from dotenv import load_dotenv
    load_dotenv()
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
elif platform.system() == "Linux":
    GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
else:
    raise OSError("Unsupported operating system")

llm = ChatGroq(
    temperature=0,
    model_name="llama-3.1-70b-versatile",
    groq_api_key=GROQ_API_KEY 
)

def streamlit_app(text):
    code = functions.get_workflow(text, llm)
    local_vars = {}
    exec(code, globals(), local_vars)
    create_graph = local_vars.get("create_graph")
    graph = create_graph()
    return graph

# App layout
st.title("Method Section Workflow Generator")

# Two-column layout
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("Transform your method section into a clear, step-by-step visual workflow. Simply paste your text below and watch the magic happen!")
    
    text = st.text_area("Paste the method section here (limit: 1500 words):", height=250)
    word_count = len(text.split())
    
    if word_count > 0:
        st.info(f"Word count: {word_count} words")
        if word_count > 1500:
            st.warning("⚠️ Word limit exceeded! Please shorten your text.")
    
    if st.button("Generate Workflow"):
        if text:
            with st.spinner("Generating workflow... This may take a moment."):
                output = streamlit_app(text)
                st.success("Workflow generated successfully!")
                st.image(output, caption="Generated Workflow Graph", use_column_width=True)
        else:
            st.warning("Please enter a method section.")

with col2:
    st.markdown("### How it works")
    st.markdown("""
    1. **Input**: Paste your method section text.
    2. **Processing**: Our AI analyzes the text.
    3. **Output**: A visual workflow is generated.
    
    ### Tips for best results
    - Use clear, concise language
    - Include all key steps in your method
    - Aim for 500-1000 words for optimal results
    
    ### Limitations
    Please note that the Workflow Generator may produce inaccurate results for very complex or ambiguous methods. We appreciate your understanding and encourage you to provide feedback to help us improve.
    """)

# Footer
st.markdown(
    """
    <div class="footer">
        <p>Created by <a href="https://www.linkedin.com/in/mohamedfadlalla-ai/" target="_blank">Mohamed Fadlalla</a> | 
        <a href="#" onclick="openFeedback()">Provide Feedback</a></p>
    </div>
    <script>
    function openFeedback() {
        window.open('https://forms.gle/yourFeedbackFormURL', '_blank');
    }
    </script>
    """,
    unsafe_allow_html=True
)