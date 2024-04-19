import os
import pygame
import speech_recognition as sr
from bot_scrapper import *

def speak(text):
    voice = "en-US-EricNeural"

    command = f'edge-tts --voice "{voice}" --text "{text}" --write-media "output.mp3"'

    os.system(command)

    pygame.init()
    pygame.mixer.init()


    try:
        pygame.mixer.music.load("output.mp3")

        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    
    except Exception as e:
        print(e)
    
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
   
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
    
    except Exception as e:
        print(e)
        return "-"
    return query

# speak("hello i am your voa. How can i assist you today!")
# query = take_command()
# print(query)
click_on_chat_button()
while True:
    query = take_command().lower()
    print('\n You: '+ query)
    sendQuery(query)
    isBubbleLoaderVisible()
    response = retriveData()
    speak(response)