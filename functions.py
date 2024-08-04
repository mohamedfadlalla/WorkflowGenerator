from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import PromptTemplate

from prompts import system_prompt_1, system_prompt_2, get_markdown

import re
import os 


def toMarkdown(method, llm):
    markdown_prompt = ChatPromptTemplate.from_messages([("system", get_markdown,),
                                               ("human", method),])

    chain = markdown_prompt | llm
    markdown = chain.invoke({}).content
    return markdown

def create_nodes_and_edges(method, llm):
    create_nodes = ChatPromptTemplate.from_messages([("system", system_prompt_1,),
                                               ("human", method),])
    chain = create_nodes | llm
    response = chain.invoke({}).content
    return response


def extract_code_programatic(llm_response):
    pattern = re.compile(r'```python(.*?)```', re.DOTALL)
    match = pattern.search(llm_response)
    if match:
        return match.group(1).strip()
    else:
        return "No Python code found in the response."

def extract_code(text, llm):
    prompt = PromptTemplate.from_template('''
    you will be provided with a text that contain code, 
    your job is to extract the code only in """ code """. 
    **important** output the code only, avoide being verbose

    ###test###
    {response}

    ###code###
    ''')
    chain = prompt | llm
    response = chain.invoke({'response':text})
    
    return response.content.replace('""""','')
    
def generate_graphviz_code(nande_content, llm):
    create_nodes = ChatPromptTemplate.from_messages([("system", system_prompt_2,),
                                               ("human", nande_content),])

    chain = create_nodes | llm
    response = chain.invoke({}).content
    return response

def get_workflow(text, llm):
    """this code genrate a graph.png file with the workflow of the paper, the input is the text of the method section"""

    # Create nodes and edges
    method = toMarkdown(text, llm)
    
    nande = create_nodes_and_edges(method, llm)
    # Generate Graphviz code
    llm_response = generate_graphviz_code(nande, llm)
    # Extract and execute the code
    code = extract_code(llm_response, llm)
    code = extract_code_programatic(llm_response)
    exec(code)
    return code

    