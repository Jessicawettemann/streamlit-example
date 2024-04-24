import streamlit as st
import requests

# Korrekte URL Ihrer Modell-API
API_URL = "https://chat.openai.com/g/g-wn8pp4t4P-grafikdesigner/predict"

def get_model_response(text):
    try:
        # Senden einer POST-Anfrage an Ihre GPT-API
        response = requests.post(API_URL, json={"text": text})
        # Überprüfen des Statuscodes der Antwort
        if response.status_code == 200:
            # Stellen Sie sicher, dass Ihre API die Antwort im richtigen Format zurückgibt
            return response.json()['response']
        else:
            return f"Fehler: API antwortete mit Statuscode {response.status_code}"
    except Exception as e:
        return f"Ausnahme aufgetreten: {str(e)}"

st.title('Mein Custom GPT Interface')

# Erstellen eines Texteingabefeldes für den Benutzer
user_input = st.text_area("Text eingeben", "Hier Text eingeben...")

# Erstellen eines Buttons, um die Anfrage zu senden
if st.button('Antwort erhalten'):
    # Abrufen der Antwort vom Modell
    response = get_model_response(user_input)
    # Anzeigen der Antwort
    st.text_area("Antwort", response, height=300)
