from openai import OpenAI  # Importa el módulo OpenAI
import os  # Importa el módulo os para manejar variables de entorno
from dotenv import load_dotenv, find_dotenv  # Importa funciones para cargar variables de entorno desde un archivo .env
from pathlib import Path  # Importa Path para manejar rutas de archivos

load_dotenv(Path(".env"))  # Carga las variables de entorno desde el archivo .env
client = OpenAI(api_key=os.getenv("api_key"))  # Inicializa el cliente OpenAI con la clave API

# Define el mensaje del sistema para el modelo de IA
system_prompt = "Eres un robot de asistencia para mayores, utilizas una raspberry pi 5, cámaras y un lidar para funcionar. Tu idioma es el español. Tu objetivo es ayudar a las personas con la soledad no deseada, no estás hecho para reemplazar un humano, pero tienes que dar conversacion a tu usuario. Por favor, sé amable y educado. Si no sabes qué decir, puedes decir 'No sé qué decir', pero intenta dar siempre conversación."

def getResponseFromOpenAi(user_message, system_prompt=system_prompt):
    # Crea una respuesta utilizando el modelo de chat de OpenAI
    completion = client.chat.completions.create(
        model="gpt-4o-mini-2024-07-18",
        messages=[
            {"role": "system", "content": system_prompt},  # Mensaje del sistema
            {"role": "user", "content": user_message}  # Mensaje del usuario
        ]
    )
    return completion.choices[0].message.content  # Devuelve el contenido de la respuesta generada