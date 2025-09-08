from dotenv import load_dotenv
from os import getenv

load_dotenv(override=True)  # The override=True ensures it overwrites existing vars

API_URL = getenv('API_URL', '')
OLLAMA_URL = getenv('OLLAMA_URL', '')