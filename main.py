# Main entry point for the Voice Assistant
from speech import speak
from listener import listen

import datetime
import webbrowser
import os
import subprocess

import wikipedia
import pyjokes

speak("Hello Yash. I am your Voice Assistant.")

while True:

    command = listen()

    if command == "":
        continue

    # Greeting
    if "hello" in command or "hi" in command:

        speak("Hello Yash. How can I help you?")

    # Time
    elif "time" in command:

        current_time = datetime.datetime.now().strftime("%I:%M %p")

        speak(f"The current time is {current_time}")

    # Date
    elif "date" in command:

        current_date = datetime.datetime.now().strftime("%d %B %Y")

        speak(f"Today's date is {current_date}")

    # Google
    elif "open google" in command:

        speak("Opening Google")

        webbrowser.open("https://www.google.com")

    # Search
    elif "search" in command:

        query = command.replace("search", "")

        speak(f"Searching {query}")

        webbrowser.open(
            "https://www.google.com/search?q=" + query
        )

    # YouTube
    elif "open youtube" in command:

        speak("Opening YouTube")

        webbrowser.open("https://www.youtube.com")

    # Calculator
    elif "calculator" in command:

        speak("Opening Calculator")

        subprocess.Popen("calc.exe")

    # Notepad
    elif "notepad" in command:

        speak("Opening Notepad")

        subprocess.Popen("notepad.exe")

    # VS Code
    elif "visual studio code" in command or "vs code" in command:

        speak("Opening Visual Studio Code")

        os.system("code")

    # Wikipedia
    elif "wikipedia" in command:

        topic = command.replace("wikipedia", "")

        try:

            result = wikipedia.summary(topic, sentences=2)

            print(result)

            speak(result)

        except:

            speak("Sorry. I could not find anything.")

    # Joke
    elif "joke" in command:

        joke = pyjokes.get_joke()

        print(joke)

        speak(joke)

    # Exit
    elif "exit" in command or "bye" in command:

        speak("seeyou again Yash. Have a nice day.")

        break

    else:

        speak("Sorry, I don't know that command.")