#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Import the json library
import json
import requests
import speech_recognition as sr
from playsound import playsound

## Take input from user microphone
def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.......")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='vi-VN')
        print(query)
    except Exception as e:
        print(e)
        print("Say that again please....")
        return "None"
    return query
