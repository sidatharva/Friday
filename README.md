# Friday — Offline Voice Assistant 🚀

A fully **offline** desktop voice assistant with a small pygame GUI. Speech
recognition runs locally via [Vosk](https://alphacephei.com/vosk/) — no
internet connection or cloud API required. Text-to-speech is handled by
`pyttsx3`, and system actions (volume, launching apps, screenshots) go
through `pyautogui` / `os.system`.

Say **"Friday, volume up"** (or notepad / chrome / calc / screenshot / time /
mute / bye) and it listens, recognizes, and acts — entirely on-device.

## Features

- 🎙️ Offline wake-word style commands (prefix any command with "friday")
- 🔊 Spoken feedback via text-to-speech
- 🖥️ Simple pulsing pygame GUI showing listening status
- 🔉 Volume up / down / mute
- 🕒 Spoken current time
- 📓 Launch Notepad, Chrome, Calculator
- 📸 Take a timestamped screenshot
- 👋 Voice-triggered exit ("bye" / "exit" / "stop" / "goodbye")

## Requirements

- Windows (uses `start notepad`, `start chrome`, `calc`, Windows volume keys)
- Python 3.10+
- A microphone
- The Vosk small English model (not included in this repo — see below)

## Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/<your-username>/friday-offline-assistant.git
   cd friday-offline-assistant
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > `pyaudio` can be fiddly to install on Windows with plain `pip`. If it
   > fails, install it via a prebuilt wheel, e.g. `pip install pipwin && pipwin install pyaudio`.

3. **Download the Vosk speech model**

   Download `vosk-model-small-en-us-0.15` from the
   [Vosk model list](https://alphacephei.com/vosk/models), unzip it, and
   place its contents in a folder named `model/` in the project root, so
   you end up with `model/am/`, `model/conf/`, `model/graph/`, etc.

4. **Run it**

   ```bash
   python friday_volume_fixed.py
   ```

## Voice commands

| Say (after "Friday")        | Action                              |
|------------------------------|--------------------------------------|
| "volume up"                  | Raises system volume                  |
| "volume down"                | Lowers system volume                  |
| "mute"                       | Mutes system volume                   |
| "time"                       | Speaks the current time               |
| "notepad"                    | Opens Notepad                         |
| "chrome"                     | Opens Chrome                          |
| "calc"                       | Opens Calculator                      |
| "screenshot"                 | Saves a timestamped screenshot        |
| "bye" / "exit" / "stop" / "goodbye" | Exits the assistant            |

## Building a standalone .exe

This project was originally distributed as a PyInstaller-bundled `.exe`.
To rebuild one yourself:

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "model;model" friday_volume_fixed.py
```

## Project structure

```
friday-offline-assistant/
├── friday_volume_fixed.py   # Main application
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## License

MIT — see [LICENSE](LICENSE).
