import pyttsx3
import time
engine = pyttsx3.init()
time.sleep(1)
engine.say("I will speak this text")
engine.runAndWait()