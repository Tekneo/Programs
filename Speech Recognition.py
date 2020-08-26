#This project is about implementing Speech Recognizer using Pyaudio and SpeechRecognition Libraries.
from typing import Text
import speech
import speech_recognition as sr
speaker = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Something")
    audio = speaker.listen(source)
    try:
        Text = speaker.recognize_google(audio)
        print('You said: {}'.format.(Text))
    except
        print("Sorry , I could not capture your Voice")
