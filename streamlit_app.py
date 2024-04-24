import streamlit as st
import requests

# Die URL Ihrer Modell-API
API_URL = "http://Ihre-API-URL/predict"

def get_model_response(text):
    # Senden einer POST-Anfrage an Ihre GPT-API
    response = requests.post(API_URL, json={"text": text})
    # Stellen Sie sicher, dass Ihre API die Antwort im richtigen Format zurückgibt
    return response.json()['response']

st.title('Mein Custom GPT Interface')

# Erstellen eines Texteingabefeldes für den Benutzer
user_input = st.text_area("Text eingeben", "Hier Text eingeben...")

# Erstellen eines Buttons, um die Anfrage zu senden
if st.button('Antwort erhalten'):
    # Abrufen der Antwort vom Modell
    response = get_model_response(user_input)
    # Anzeigen der Antwort
    st.text_area("Antwort", response, height=300)
