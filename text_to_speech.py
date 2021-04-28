from playsound import playsound
from gtts import gTTS
import os

# Convert text to speak
def speak(text=''):
    tts = gTTS(text=text, lang="vi")
    filename = "voice.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)