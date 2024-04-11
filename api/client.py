import requests
import streamlit as st 

def get_llama2_response(input_text):
    response = requests.post("http://localhost:8000/chat/invoke",
    json={'input':{'topic':input_text}})
    
    return response.json()['output']

def get_codellama_response(input_text):
    response = requests.post("http://localhost:8000/code/invoke",
    json={'input':{'topic':input_text}})
    
    return response.json()['output']

    
    ### Streamlit framework ###


st.title("Chatbot with FastAPI")
input_text = st.text_input("Write a chat on")
input_text1 = st.text_input("Write code on")

if input_text:
    st.write(get_llama2_response(input_text))
    
if input_text1:
    st.write(get_codellama_response(input_text1))    