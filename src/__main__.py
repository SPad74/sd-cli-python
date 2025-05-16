import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables del .env

api_url = os.getenv("API_URL")

print(f"{api_url}")