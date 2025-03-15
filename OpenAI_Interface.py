from openai import OpenAI
import os                                                                                                                                                                                                          
from dotenv import load_dotenv, find_dotenv
from pathlib import Path

load_dotenv(Path(".env"))
client = OpenAI(api_key=os.getenv("api_key"))

system_prompt = "Eres un robot de asistencia para mayores, utilizas una raspberry pi 5, cámaras y un lidar para funcionar. Tu idioma es el español. Tu objetivo es ayudar a las personas con la soledad no deseada, no estás hecho para reemplazar un humano, pero tienes que dar conversacion a tu usuario. Por favor, sé amable y educado. Si no sabes qué decir, puedes decir 'No sé qué decir', pero intenta dar siempre conversación."



while True:

  user_input = input("User -> ")

  completion = client.chat.completions.create(
    model="gpt-4o-mini-2024-07-18",
    messages=[
      {"role": "system", 
      "content": system_prompt
      },

      {"role": "user", 
      "content": user_input
      }
    ]
  )
  print(completion.choices[0].message.content)