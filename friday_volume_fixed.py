"""
FRIDAY - Offline Voice Assistant (Vosk + Volume Control)

Fully offline voice assistant GUI. Uses Vosk for speech recognition
(no internet / cloud API required), pyttsx3 for text-to-speech,
pygame for the pulsing GUI, and pyautogui/os for system control
(volume, notepad, chrome, calculator, screenshots).
"""

import pyaudio
import json
import pygame
import sys
import os
import math
import datetime
import pyautogui
import pyttsx3
from vosk import Model, KaldiRecognizer
import threading
import wave
import time

print("🚀 OFFLINE FRIDAY GUI - Vosk + Volume Control!")

import sys
import os


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller ."""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ---- Vosk speech recognition setup ----
model_path = resource_path("model")
model = Model(model_path)
rec = KaldiRecognizer(model, 16000)

# ---- Text-to-speech setup ----
engine = pyttsx3.init()
engine.setProperty("rate", 175)


def speak(text):
    print(f"Friday: {text}")
    engine.say(text)
    engine.runAndWait()


# ---- Microphone audio stream ----
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=16000,
    input=True,
    frames_per_buffer=8000,
)
stream.start_stream()


def listen_vosk():
    while True:
        try:
            data = stream.read(4000, exception_on_overflow=False)
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "").lower()
                if text and "friday" in text:
                    cmd = text.replace("friday", "").strip()
                    if process_command(cmd):
                        return
        except Exception:
            continue


def process_command(text):
    print(f"CMD: '{text}'")

    if "time" in text:
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Time is {now}")
        return None

    if "notepad" in text:
        os.system("start notepad")
        speak("Notepad opened")
        return None

    if "chrome" in text:
        os.system("start chrome")
        speak("Chrome opened")
        return None

    if "calc" in text:
        os.system("calc")
        speak("Calculator")
        return None

    if "screenshot" in text:
        pyautogui.screenshot(f"screen_{int(time.time())}.png")
        speak("Screenshot saved")
        return None

    if "volume up" in text:
        for _ in range(5):
            pyautogui.press("volumeup")
        speak("Volume UP - check tray!")
        return None

    if "volume down" in text:
        for _ in range(5):
            pyautogui.press("volumedown")
        speak("Volume DOWN - check tray!")
        return None

    if "mute" in text:
        pyautogui.press("volumemute")
        speak("Muted")
        return None

    if "bye" in text or "exit" in text or "stop" in text or "goodbye" in text:
        print("*** EXIT SEQUENCE ***")
        speak("Goodbye!")
        return True

    speak("Try: time, notepad, chrome, calc, screenshot, volume up/down, mute, bye")
    return None


# ---- Pygame GUI ----
pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("FRIDAY Offline")
clock = pygame.time.Clock()
font_big = pygame.font.SysFont("consolas", 28)
font = pygame.font.SysFont("consolas", 20)

threading.Thread(target=listen_vosk, daemon=True).start()
speak("Friday ready - say VOLUME UP!")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pulse = int(20 * abs(math.sin(time.time() * 3)))

    screen.fill((10, 10, 30))

    pygame.draw.circle(screen, (0, 255, 100), (250, 200), 80 + pulse // 2)
    pygame.draw.circle(screen, (255, 255, 0), (250, 200), 30, 4)

    screen.blit(font_big.render("OFFLINE FRIDAY", True, (0, 255, 0)), (100, 50))
    screen.blit(
        font.render("volume up/down/mute/time/etc", True, (150, 150, 255)),
        (20, 350),
    )

    pygame.display.flip()
    clock.tick(60)
