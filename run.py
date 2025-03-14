import os
from playsound import playsound
import time


message2 = "Hola, soy Robert, un robot del hogar. Y gracias a la inteligencia artificial, puedo ayudarte respecto a la soledad no deseada."

message="Hola guapisima, ¿Cómo estás?"
commands = """sudo docker exec -ti piper-tts sh -c  + 'echo "string&2" | /opt/piper/build/piper --model es_ES-davefx-medium.onnx --output_file /opt/speech.wav'"""

os.system("sudo docker start piper-tts")
os.system(commands.replace("string&2", message))
os.system("sudo docker cp piper-tts:/opt/speech.wav ./")
os.system("aplay notification.wav")
os.system("aplay speech.wav")