import os
from playsound import playsound

os.system("sudo docker exec -ti piper-tts sh -c 'echo 'To address the elephant in the room: using text-to-speech technology isn’t just practical, it’s a lot of fun too!' | /opt/piper/build/piper --model /opt/piper/voices/aru/medium/en_GB-aru-medium.onnx --output_file /opt/speech.wav'")
os.system("docker cp piper-tts:/opt/speech.wav ./")
playsound("speech.wav")