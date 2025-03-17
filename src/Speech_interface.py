import os

def speak(text):
    commands = """sudo docker exec -ti piper-tts sh -c  + 'echo "string&2" | /opt/piper/build/piper --model es_ES-davefx-medium.onnx --output_file /opt/speech.wav'"""
    os.system("sudo docker start piper-tts")
    os.system(commands.replace("string&2", text))
    os.system("sudo docker cp piper-tts:/opt/speech.wav ./")
    os.system("aplay /temp/notification.wav")
    os.system("aplay /temp/speech.wav")