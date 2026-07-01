import pyttsx3
import time

engine = pyttsx3.init("sapi5")
engine.setProperty("rate", 170)

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

engine.say("Hello Yash")
engine.runAndWait()

time.sleep(0)

engine.say("Welcome to your Voice Assistant project.")
engine.runAndWait()

print("Done")