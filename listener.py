import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    try:

        print("Recognizing...")

        command = recognizer.recognize_google(audio)

        command = command.lower()

        print("You :", command)

        return command

    except:

        print("Sorry, I didn't understand.")

        return ""