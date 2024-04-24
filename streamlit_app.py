import openai
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

# Load the environment variables file
_ = load_dotenv(find_dotenv())

# Set the API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')
     
