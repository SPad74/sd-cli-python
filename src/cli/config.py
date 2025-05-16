import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

# URL base del backend tradicional
API_BASE_URL = os.getenv("API_URL", "http://localhost:8000")

# Dirección del broker de Kafka
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
