import openai
from openai import OpenAI
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')


API_URL = "https://chat.openai.com/g/g-wn8pp4t4P-grafikdesigner/predict"



client = OpenAI()
# Überprüfen, ob der API-Schlüssel korrekt abgerufen wurde
if not api_key:
    raise ValueError("API_KEY ist nicht in den Umgebungsvariablen definiert.")

# Verwenden Sie API_KEY in Ihrer Anwendung
print("Mein API-Schlüssel ist:", api_key)
def get_model_response(text):
    headers = {
        "Authorization": f"Bearer {api_key}"
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

user_input = st.text_area("Text eingeben")
if st.button('Antwort erhalten'):
    response = get_model_response(user_input)
    st.text_area("Antwort", response, height=300)
