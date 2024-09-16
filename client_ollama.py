import requests
import streamlit as st
import json

def ollama_response1(input_text):
    try:
        response = requests.post("http://localhost:8000/information", json={'topic': input_text})
        response.raise_for_status()
        return response.json().get('response', 'No response key found')
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def ollama_response2(input_text):
    try:
        response = requests.post("http://localhost:8000/song", json={'topic': input_text})
        response.raise_for_status()
        return response.json().get('response', 'No response key found')
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

st.title("Creating APIs with Llama2 using Langchain")
input_text = st.text_input("Write information on")
input_text1 = st.text_input("Write a song on")

if input_text:
    st.write(ollama_response1(input_text))

if input_text1:
    st.write(ollama_response2(input_text))
