import datetime
import os  # Importa el módulo os para manejar variables de entorno
from dotenv import load_dotenv, find_dotenv  # Importa funciones para cargar variables de entorno desde un archivo .env
from pathlib import Path  # Importa Path para manejar rutas de archivos

load_dotenv(Path(".env"))  # Carga las variables de entorno desde el archivo .env
condition = os.getenv("condition")  # Inicializa el cliente OpenAI con la clave API



def getContext():
    context = (
                "La fecha y hora actual es: " + str(datetime.datetime.now()) + "\n" + 
                "La condición fisica o psicológica del usuario es: " + condition
               )
    return context





if __name__ == '__main__':
  print(getContext())