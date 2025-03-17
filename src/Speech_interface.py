import os  # Importa el módulo os para ejecutar comandos del sistema

def speak(text):
    # Comando para generar el archivo de audio con el texto proporcionado
    commands = """sudo docker exec -ti piper-tts sh -c  + 'echo "string&2" | /opt/piper/build/piper --model es_ES-davefx-medium.onnx --output_file /opt/speech.wav'"""
    os.system("sudo docker start piper-tts")  # Inicia el contenedor Docker piper-tts
    os.system(commands.replace("string&2", text))  # Genera el audio con el texto proporcionado
    os.system("sudo docker cp piper-tts:/opt/speech.wav ./")  # Copia el archivo de audio generado al sistema local
    os.system("aplay /temp/notification.wav")  # Reproduce un sonido de notificación
    os.system("aplay /temp/speech.wav")  # Reproduce el archivo de audio generado