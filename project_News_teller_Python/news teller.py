import requests
import json
from time import strftime

today=(strftime("%d %B %Y"))

def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.Spvoice")
    speak.speak(str)

r=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=29538248ccd245ae85475b8a70f6a2a2")
# print(r.json()) # does not raise an error because response is a json object. 

data=((json.loads(r.text)))
articles=data["articles"]

print(f"Today is {today} and the news are....")
speak(f"Today is {today} and the news are....")
for item in articles:
    description=(item["description"])
    print(description)
    speak(description)

print("Thank You for listening.")
speak("Thank You for listening.")