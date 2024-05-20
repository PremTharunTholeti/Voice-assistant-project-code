import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
import time
import operator
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)
def speak(audio):
 engine.say(audio)
 engine.runAndWait()
def wishMe():
 hour = int(datetime.datetime.now().hour)
 if hour>=0 and hour<12:
   speak("Good Morning,sir!")
 elif hour>=12 and hour<18:
   speak("Good Afternoon!,sir") 
 else:
   speak("Good Evening!,sir")
 
 speak("Im Elisa. What can I do for you ?")
def takeCommand():
  r = sr.Recognizer()
  with sr.Microphone() as source:
     print("Listening....")
     speak("Listening")
     r.pause_threshold=1
     audio=r.listen(source)
  try:
      print("Recognising....")
      speak("Recognising")
      query=r.recognize_google(audio,language='en-in')
      print(f"user said:{query}\n")
  except Exception as e:
      speak("say that again please")
      print("say that again please")
      return "none"
  return query
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('search in wikipedia')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube")
            speak("What you will like to watch?")
            qrry=takeCommand().lower()
            kit.playonyt(f"{qrry}")
        elif 'Close chrome' in query:
            os.system("taskkill /f /im chrome.exe")
        elif 'close youtube' in query:
            os.system("taskkill /f /im msedge.exe")
        elif 'open google' in query:
            speak("What should I search?")
            qry=takeCommand().lower()
            webbrowser.open(f"{qry}")
            results=wikipedia.summary(qry,sentences=2)
            speak(results)
        elif 'close google' in query:
            os.system("taskkill /f /im msedge.exe")
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,the time is {strTime}")
        elif 'shutdown the system' in query:
            os.system("shutdown /s /t 5")
        elif 'restart the system' in query:
            os.system("shutdown /r /t 5")
        elif 'lock the system' in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif 'open notepad' in query:
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        elif 'close notepad' in query:
            os.system("taskkill /f /im notepad.exe")
        elif 'open command prompt' in query:
            os.system("start cmd")
        elif 'close command prompt' in query:
            os.system("taskkill /f /im cmd.exe")
        elif 'go to sleep' in query:
            speak('alright then,Im switching off')
            sys.exit()
        elif 'take screenshot' in query:
            speak('Tell me a name for the file')
            name=takeCommand().lower()
            time.sleep(3)
            img=pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("Screenshot saved")
        elif "open screenshot" in query:
            npath="E:\\PROJECTS\\python\\"f"{name}.png"
            os.startfile(npath)
        elif 'calculate' in query:
            r=sr.Recognizer()
            with sr.Microphone() as source:
                speak("Ready")
                print("Listening")
                r.adjust_for_ambient_noise(source)
                audio=r.listen(source)
            my_string=r.recognize_google(audio)
            print(my_string)
            def get_operator_fn(op):
                return{
                    '+':operator.add,
                    '-':operator.sub,
                    'x':operator.mul,
                    'divided':operator.__truediv__, 
                }[op]
            def eval_bianary_expr(op1,oper,op2):
                op1,op2=int(op1),int(op2)
                return get_operator_fn(oper)(op1,op2)
            speak("Your result is")
            speak(eval_bianary_expr(*(my_string.split())))
        elif 'What is my IP address' in query:
            speak("Checking")
            try:
                ipAdd=requests.get('https://api.ipify.org').text
                print(ipAdd)
                speak("Your IP address is")
                speak(ipAdd)
            except Exception as e:
                speak("Network is weak,Please try again sometime later")
        elif 'increase volume' in query:
            speak("increasing volume")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
            pyautogui.press("volumeup")
        elif 'decrease volume' in query:
            speak("decreasing volume")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
            pyautogui.press("volumedown")
        elif 'mute' in query:
            pyautogui.press("volumemute")
        elif 'scroll down' in query:
            pyautogui.scroll(1000)
        elif 'visual studio' in query:
            pyautogui.moveTo(46,31,2)
            pyautogui.dragRel(1857,31,2)
        elif 'rectangular spiral' in query:
            pyautogui.hotkey('win')
            time.sleep(1)
            pyautogui.write('paint')
            time.sleep(1)
            pyautogui.press('enter')
            pyautogui.moveTo(100,193,1)
            pyautogui.rightClick
            pyautogui.click()
            distance=300
            while distance>0:
                pyautogui.dragRel(distance,0,0.1,button="left")
                distance=distance-10
                pyautogui.dragRel(0,distance,0.1,button="left")
                pyautogui.dragRel(-distance,0,0.1,button="left")
                distance=distance-10
                pyautogui.dragRel(0,-distance,0.1,button="left")
        elif 'close paint' in query:
            os.system("taskkill /f /im mspaint.exe")
        elif 'what are you' in query:
            print("My name is Elisa")
            speak("My name is Elisa!")
            print("I am a voice assistant created by Prem and Satish,  I can do anything that my creator programmed me to do")
            speak(" I am a voice assistant created by Prem and Sathish,  I can do anything that my creator programmed me to do") 
        elif 'who created you' in query:
            print("I am a voice assistant created by Prem and Satish")
            speak("I am a voice assistant created by Prem and Satish")
        elif "open chrome" in query:
            speak("opening chrome")
            print("opening chrome")
            os.startfile("C:\Program Files\Google\Chrome\Application\chrome.exe")
        elif 'maximize the window' in query:
            pyautogui.hotkey('alt','space')
            time.sleep(1)
            pyautogui.press('x')
        elif "google search" in query:
            query = query.replace("google search","")
            pyautogui.hotkey('alt','d')
            pyautogui.write(f"{query}",0.1)
            pyautogui.press('enter')
        elif "youtube search" in query:
            query = query.replace("youtube search","")
            pyautogui.moveTo(750,150,2)
            pyautogui.click(x=750,y=150,clicks=1,interval=0,button='left')
            time.sleep(1)
            pyautogui.write(f"{query}",0.1)
            pyautogui.press('enter')
        elif "minimise the window" in query:
            pyautogui.hotkey('alt','space')
            time.sleep(1)
            pyautogui.press('n')
        elif "close window" in query:
            pyautogui.hotkey('ctrl','shift','w')
        elif "close chrome" in query:
            os.system("taskkill /f /im chrome.exe")