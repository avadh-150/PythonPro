
from openai import ChatCompletion


import pyttsx3
import os
import speech_recognition as sr
import webbrowser
import openai

# from config import apikey
import datetime
import random
import numpy as np
apikey="Put the OpenAI KEY"
openai.api_key = apikey

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    
    engine.runAndWait()
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.2
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}") 
            return  query
        except Exception as e: 
            return "I wasn't got it,Could you please! Say again"
     
def chat(prompt):
    try:
        response = ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=400
        )
        chat_response = response.choices[0].message.content.strip()
        return chat_response
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    
    print("Hello i'm A.I")
    say("Hello i'M Jarvis, How May I Help You")
    print("Listening...")

    while True:
        query=takeCommand()
        sites=[["youtube","https://youtube.com/"],["wikipedia","https://www.wikipedia.org/"], ["google","https://google.com"],["Insta","https://instagram.com/"],["chat GPT","https://chat.openai.com/"],["black box","https://www.blackbox.ai/"]]
        for site in sites:
             if f"Open {site[0]}".lower() in query.lower():#google.lower() in youtube.lower()
                 say(f"Ok,Opening {site[0]}")
                 webbrowser.open(site[1])
        if "open music".lower() in query.lower():
            musicPath="C:/Users/Avadh/Downloads/musicx.mp3"   
            say("Opening music")
            # os.startfile(musicPath) to find and open the  file
            os.system(musicPath)

        if "hey Jarvis" in query:
            say("Hello Sir")    
            for i in range(5):  # Generate 5 responses
                prompt = takeCommand()
                response = chat(prompt)
                if response:
                    with open(f"Openai/{prompt} {random.randint(1, 2343434356)}.txt", "w") as f:
                        f.write(f"Prompt: {prompt}\n\n {response}")
                else:
                    print("Error generating response. Please try again.")   
                print(response)
                say(response)
           
        if "what's the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir The Time Is {hour} Hour,{minute} minutes")
        
        elif "generate".lower() in query.lower():
            chat(prompt=query)

        
        elif "exit".lower() in query.lower():
            say("Have Nice Day, Sir")
            exit()
        
        if not os.path.exists("Openai"):
            os.mkdir("Openai")





        






        # say(text)
#webDriver package Used to open login Account.................. 
