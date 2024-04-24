import streamlit as st
import requests
import os

API_URL = "https://chat.openai.com/g/g-wn8pp4t4P-grafikdesigner/predict"
API_KEY = os.getenv("API_KEY")  # Lesen des Schlüssels aus den Umgebungsvariablen

def get_model_response(text):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    try:
        response = requests.post(API_URL, json={"text": text}, headers=headers)
        if response.status_code == 200:
            return response.json()['response']
        else:
            return f"Fehler: API antwortete mit Statuscode {response.status_code}"
    except Exception as e:
        return f"Ausnahme aufgetreten: {str(e)}"

st.title('Mein Custom GPT Interface')

user_input = st.text_area("Text eingeben", "Hier Text eingeben...")
if st.button('Antwort erhalten'):
    response = get_model_response(user_input)
    st.text_area("Antwort", response, height=300)
