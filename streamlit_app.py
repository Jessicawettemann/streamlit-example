import streamlit as st
import requests
import os

API_URL = "https://chat.openai.com/g/g-wn8pp4t4P-grafikdesigner/predict"

import os

# Abrufen des API-Schlüssels aus den Umgebungsvariablen
API_KEY = os.getenv("API_KEY")

# Überprüfen, ob der API-Schlüssel korrekt abgerufen wurde
if not API_KEY:
    raise ValueError("API_KEY ist nicht in den Umgebungsvariablen definiert.")

# Verwenden Sie API_KEY in Ihrer Anwendung
print("Mein API-Schlüssel ist:", API_KEY)
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
