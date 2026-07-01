# 🎙️ Voice Assistant in Python

A simple Voice Assistant built using Python that can listen to voice commands, speak responses, and perform everyday tasks such as opening applications, searching the web, telling the time and date, and more.

This project was developed as part of my internship to demonstrate the fundamentals of speech recognition, text-to-speech, and Python automation.

---

## 📌 Features

- 🎤 Voice Recognition using SpeechRecognition
- 🔊 Text-to-Speech using pyttsx3
- 👋 Greets the user
- ⏰ Tells the current time
- 📅 Tells the current date
- 🌐 Opens Google
- 🔍 Searches Google
- ▶️ Opens YouTube
- 📖 Searches Wikipedia
- 😂 Tells random jokes
- 📝 Opens Notepad
- 🧮 Opens Calculator
- 💻 Opens Visual Studio Code
- ❌ Exit command

---

## 🛠️ Technologies Used

- Python 3.11
- SpeechRecognition
- pyttsx3
- PyAudio
- Wikipedia
- PyJokes
- Webbrowser
- Datetime
- OS
- Subprocess

---

## 📁 Project Structure

```text
VoiceAssistant/
│
├── main.py              # Main application
├── speech.py            # Text-to-Speech module
├── listener.py          # Speech Recognition module
├── weather.py           # Weather module (optional)
├── email_service.py     # Email module (optional)
├── reminder.py          # Reminder module
├── commands.json        # Custom commands
├── config.py            # Configuration file
├── requirements.txt     # Required Python packages
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YashYKP/VoiceAssistant.git
```

### 2. Open the project

```bash
cd VoiceAssistant
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

---

## 🎤 Example Voice Commands

Try saying:

- Hello
- What is the time?
- What is today's date?
- Open Google
- Search Python Programming
- Open YouTube
- Wikipedia Artificial Intelligence
- Open Calculator
- Open Notepad
- Open VS Code
- Tell me a joke
- Exit

---

## 📦 Requirements

Install manually if needed:

```bash
pip install SpeechRecognition
pip install pyttsx3
pip install PyAudio
pip install wikipedia
pip install pyjokes
```

or

```bash
pip install -r requirements.txt
```

---

## 📸 Screenshots

You can add screenshots here after running the project.

Example:

```
screenshots/
    assistant.png
```

Then include them like this:

```markdown
![Voice Assistant](screenshots/assistant.png)
```

---

## 🚀 Future Improvements

- Weather Information
- Email Support
- Reminder Notifications
- Music Player
- Camera Control
- Battery Percentage
- Volume Control
- Offline Speech Recognition
- AI Chat Integration

---

## 🐞 Known Limitations

- Speech recognition requires an internet connection when using Google Speech Recognition.
- Background noise may reduce recognition accuracy.
- Some application paths may vary depending on the operating system.

---

## 👨‍💻 Author

**Yash Pandav**

Automobile Engineering Student  
Dhole Patil College of Engineering, Pune

GitHub: https://github.com/YashYKP

---

## 📄 License

This project is created for educational and internship purposes.

Feel free to fork, modify, and learn from the project.
