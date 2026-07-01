import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for index, voice in enumerate(voices):
    print(f"Voice {index}")
    print("ID:", voice.id)
    print("Name:", voice.name)
    print("Languages:", voice.languages)
    print("-" * 50)