import requests
import json
import os
while True:
    city= input("Enter the city name: ")


    url= f"https://api.weatherapi.com/v1/current.json?key=0abf91cbba2144e5b43165627240705&q={city}"


    # print(r.text)
    
        
    r= requests.get(url)
    wdic= json.loads(r.text)
    print(wdic['current']['temp_c'])
    command=f'powershell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'The current temperature of {city} is {wdic["current"]["temp_c"]}\')"'
    os.system(command)


