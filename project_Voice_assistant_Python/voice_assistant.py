import pyttsx3
from datetime import datetime
import speech_recognition as sr
import os
import wikipedia
import time
import pywhatkit

hour_now=(datetime.now().strftime("%H"))
min_now=(datetime.now().strftime("%M"))

d=datetime.now().hour
if d>=0 and d<6:
    d="good night"
elif d>6 and d<12:
    d="good morning"
elif d>=12 and d<16:
    d="good afternoon"
elif d>=16 and d<21:
    d="good evening"
elif d>=21:
    d="good night"

def speak(audio):
    '''text to speech'''
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def notepad():
    '''notepad opener function'''
    os.system("start notepad")

def excel():
    '''excel opener'''
    os.system("start excel")

def chrome():
    '''open chrome'''
    os.system("start chrome")

def google_result_by_chrome(else_text):
    '''google result of what have u said'''
    os.system(f"start chrome www.google.com/search?q={else_text}")

def youtube():
    '''open youtube by saying'''
    os.system("start brave www.youtube.com")  

def play_song_or_video_on_yt(music):
    '''play music or video on yt'''
    pywhatkit.playonyt(music)

def whatsapp():
    '''open whatsapp'''  
    os.system("start chrome https://web.whatsapp.com")

def gmail():
    '''open gmail'''
    os.system("start chrome https://mail.google.com/mail/u/0/#inbox")

def speechtotext():
    '''speech to text'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening your voice....")
        audio = r.listen(source)
        # global text
        print("Recognising....")
        text = r.recognize_google(audio,language="en-in").lower()
        print("recognised.")
        print(text)
        # print(type(text))
        return text

speak(f"{d} Sir")
# speechtotext.text

if __name__=="__main__":
    while True:
        speak("How can I help you?\nsay exit to close me")
        try:
            # speechtotext()#func called, now say whatever u want,converting speech to text
            stt=speechtotext()
            if "exit" in stt:
                break
            elif "open notepad" in stt:
                speak("notepad has opened")
                notepad()
                time.sleep(5)
            elif "play song" in stt or "play video" in stt:
                stt=stt.replace("play","")
                stt.replace("song","")
                speak("Your query is going to play...")
                play_song_or_video_on_yt(stt)
                time.sleep(5)
            elif "wikipedia" in stt:
                stt=stt.replace("wikipedia","")
                result=wikipedia.summary(stt,sentences=2)
                speak(result)
                time.sleep(5)
            elif "start chrome" in stt or "open chrome" in stt:
                speak("Chrome has ran")
                chrome()
                time.sleep(5)
            elif "open youtube" in stt:
                speak("Youtube has opened")
                youtube()
                time.sleep(5)
            # elif (f"play {text} song"):
            #     play_song()
            elif "open whatsapp" in stt:
                speak("Whatsapp has opened")
                whatsapp()
                time.sleep(5)
            elif "open mail" in stt:
                speak("Mail has opened")
                gmail()
                time.sleep(5)
            elif "open excel" in stt:
                speak("Excel has opened")
                excel()
                time.sleep(5)
            else:
                speak(f"This is the google result of {stt}")
                list_of_splitted_text=stt.split(" ")
                else_text="+".join(list_of_splitted_text)
                else_text=str(else_text)
                google_result_by_chrome(else_text)  
                time.sleep(5)  
        except Exception as e:
            print("I'm not able to understand what you are saying,say clearly")
            speak("I'm not able to understand what you are saying,say clearly")
            time.sleep(2)
    speak("Thank you for using me")
    time.sleep(2)
    print("Thank you for using me")
