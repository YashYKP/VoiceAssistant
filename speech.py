import pyttsx3

engine = pyttsx3.init()

# Voice speed
engine.setProperty("rate", 170)

# Select Female voice if available
voices = engine.getProperty("voices")

if len(voices) > 1:
    engine.setProperty("voice", voices[1].id)
else:
    engine.setProperty("voice", voices[0].id)


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()