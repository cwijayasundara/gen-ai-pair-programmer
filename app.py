import os
import openai
import streamlit as st
from langchain.chains import LLMChain

import prompt_templates

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate

os.environ['OPENAI_API_KEY'] = ""
openai.api_key = os.environ['OPENAI_API_KEY']

llm_name = "gpt-4"
# llm_name = "gpt-3.5-turbo-0301"
llm = ChatOpenAI(model_name=llm_name, temperature=0)

st.title("GENERIC AI PAIR PROGRAMMER !")

mode = st.radio(
    "Assistance Mode:",
    ["Improve Code",
     "Simplify Code",
     "Unit Test",
     "Make Code Efficient",
     "Debug Code",
     "Explain Code",
     "Document Code Markdown",
     "Document Code Marmaid Sequence Diagram",
     "Document Code Marmaid Class Diagram",
     "Convert to Python"])

# define the template
template = None
if mode == "Improve Code":
    template = prompt_templates.prompt_template_improve_3
elif mode == "Simplify Code":
    template = prompt_templates.prompt_template_simplify_1
elif mode == "Unit Test":
    template = prompt_templates.prompt_template_unit_test_1
elif mode == "Make Code Efficient":
    template = prompt_templates.prompt_template_efficient_1
elif mode == "Debug Code":
    template = prompt_templates.prompt_template_debug_1
elif mode == "Explain Code":
    template = prompt_templates.prompt_template_explain_1
elif mode == "Document Code Markdown":
    template = prompt_templates.prompt_template_documentation_1
elif mode == "Document Code Marmaid Sequence Diagram":
    template = prompt_templates.prompt_template_documentation_2
elif mode == "Document Code Marmaid Class Diagram":
    template = prompt_templates.prompt_template_documentation_3
elif mode == "Convert to Python":
    template = prompt_templates.prompt_template_conversion_1
else:
    print("Invalid Mode!")
print("template is", template)

question = st.text_area('Pls enter your code here', height=275)

submit = st.button("submit", type="primary")

if submit and template and question:
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(question)
    st.write(response)

