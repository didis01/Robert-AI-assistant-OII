import os
from playsound import playsound
import time


message = "Buenos dias, mi noimbre es Robert, encantado de conocerte. Soy un robot de asistencia psicológica"

commands = """sudo docker exec -ti piper-tts sh -c  + 'echo "string&2" | /opt/piper/build/piper --model es_ES-davefx-medium.onnx --output_file /opt/speech.wav'"""

os.system("sudo docker start piper-tts")
os.system(commands.replace("string&2", message))
os.system("sudo docker cp piper-tts:/opt/speech.wav ./")
os.system("aplay speech.wav")