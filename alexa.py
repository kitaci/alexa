from sys import exit
import math
#import google
from googlesearch import search
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyaudio
import time
import requests,json

listner=sr.Recognizer()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        engine.say("Hello how may I help you .")
        engine.runAndWait()
        listner.adjust_for_ambient_noise(source)
        voice = listner.listen(source)
        try:
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
        except LookupError:
            print("Couldn't understand the audio")
    return command 

def run_alexa():
    command = take_command()
    print(command)
    if 'play'in command:
        song = command.replace('play','')
        talk('playing...'+song)
        pywhatkit.playonyt(song)
    elif 'who is' in command:
         person = command.replace('who is','')
         info = wikipedia.summary(person,1)
         print(info)
         talk(info)
    elif 'date' in command:
        dt = str(datetime.date.today())
        print(dt)
        talk("today's date is " + dt)
    elif 'are you single' in command:
        talk('I am in a relationship with wi-fi')
    elif 'joke' in command:
        jk = pyjokes.get_joke()
        print(jk)
        talk(jk)
    elif 'weather' in command:
        api_key = "b49fc337dde81490958f556094103567"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        city_name = "Mumbai"
        complete_url = base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x = response.json()
        if x["cod"]!="404":
            y = x["main"]
            current_temprature = y["temp"]-273.15
            vals = math.trunc(current_temprature)
            print("Temprature in celcius = "+ str(vals) )
            talk(vals)
        else:
            print("City not found")
    
    elif 'stop' in command:
        exit()

    elif 'search' in command:
        query = command.replace('search','')
        for j in search(query,tld = 'co.in',num = 10,stop = 10,pause = 2):
            print(j)


    
    
    else:
        talk('pleas say the command again')



if __name__ == "__main__":
    run_alexa()