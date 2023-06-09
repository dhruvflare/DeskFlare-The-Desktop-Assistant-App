# imports

import json
import speech_recognition as sr
import wikipedia
import win32com.client
import webbrowser
import AppOpener
import datetime
import textwrap
import requests
import time

# speaker setup
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# world variables
sites = [
    ["youtube", "https://www.youtube.com/"],
    ["google", "https://www.google.com/"],
    ["mail", "https://mail.google.com/mail/u/0/#inbox"],
    ["chatgpt", "https://chat.openai.com/"]
]

apps = [
    "spotify",
    "discord",
    "pycharm community edition",
    "pycharm",
    "github desktop",
    "file explorer"
]


def jokes(f = r"https://official-joke-api.appspot.com/random_joke"):
    data = requests.get(f)
    tt = json.loads(data.text)
    print(tt["setup"])
    say(tt["setup"])
    time.sleep(2)
    print(tt["punchline"], "\n")
    say(tt["punchline"])



def get_weather(location = "New Delhi, Delhi"):
    params = {
        'access_key': '864b4eae76492fc120c2709e2bfa112a',
        'query': location
    }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    print(api_response)
    a = f"Current temperature in {api_response['location']['name']} is {api_response['current']['temperature']}℃"
    print(a)
    say(a)

def get_precipitation_chance(location = "New Delhi, Delhi"):

    params = {
        'access_key': '864b4eae76492fc120c2709e2bfa112a',
        'query': location
    }
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    print(api_response)
    a = f"Chance of rain in {api_response['location']['name']} is {api_response['hourly']['chanceofrain']}%"
    print(a)
    say(a)

# all functions
def say(text):
    speaker.Speak(text)


def take_command(lan='en-us'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language=lan)
            print(f'user said {query}')
            return query

        except Exception:
            print("Could not recognise, please say again...")
            return " "


def main():
    say('hello, i am DeskFlare AI')
    text = ''
    language = 'en-us'
    while True:

        if text.lower() == " ":
            text = "unrecognised"
            continue

        elif text.lower() == "exit":
            break

        elif "say" in text.lower():
            buffer = text.lower().partition('say')
            say(buffer[2])

        elif text.lower() == 'speak hindi':
            language = 'en-in'

        elif text.lower() == 'speak english':
            language = 'en-us'

        elif 'tell me a joke' in text.lower():
            jokes()


        elif "what is your name" in text.lower():
            say("my name is deskFlare AI")

        elif "what is your age" in text.lower():
            say("I am a bot, i am not a human")

        elif "current weather" in text.lower():
            get_weather()

        elif "weather in" in text.lower():
            buffer = text.lower().partition('weather in')
            q = buffer[2]
            get_weather(location=q)

        elif "chance of rain" in text.lower():
            get_precipitation_chance()

        elif "what is your gender" in text.lower() or "what is your profession" in text.lower():
            say("I am a bot, i am not a human")

        elif "search for" in text.lower():
            say("searching sir")
            buffer = text.lower().partition('search for')
            q = buffer[2]
            webbrowser.open(f"https://www.google.com/search?q={q}")

        elif "open" in text.lower():

            for site in sites:
                if f"open {site[0]}" in text.lower():
                    say(f"opening {site[0]} sir")
                    webbrowser.open(site[1])

            for app in apps:
                if f"open {app}" in text.lower():
                    say(f"opening {app} sir")
                    AppOpener.open(app, match_closest=True)

        elif "the time" in text.lower():
            timeval = datetime.datetime.now().strftime("%H:%M")
            say(f"sir, the time is {timeval}")

        elif "what is" in text.lower():
            try:
                buffer = text.lower().partition('what is')
                q = buffer[2]
                wiki = wikipedia.summary(q, sentences=5)
                wrapper = textwrap.TextWrapper(width=70)
                string = wrapper.fill(text=wiki)
                print(string)
                say(wikipedia.summary(q, sentences=2))
            except Exception:
                say("sorry, i could not find anything")

        elif "who is" in text.lower():
            try:
                buffer = text.lower().partition('who is')
                q = buffer[2]
                wiki = wikipedia.summary(q, sentences=5)
                wrapper = textwrap.TextWrapper(width=70)
                string = wrapper.fill(text=wiki)
                print(string)
                say(wikipedia.summary(q, sentences=2))
            except Exception:
                say("sorry, i could not find anything")




        print(f"listening..[{language}]")
        text = take_command(lan=language)



if __name__ == '__main__':
    main()




'''sample api responses'''

'''weatherstack api'''
# {
#     "request": {
#         "type": "City",
#         "query": "New York, United States of America",
#         "language": "en",
#         "unit": "m"
#     },
#     "location": {
#         "name": "New York",
#         "country": "United States of America",
#         "region": "New York",
#         "lat": "40.714",
#         "lon": "-74.006",
#         "timezone_id": "America/New_York",
#         "localtime": "2019-09-07 10:05",
#         "localtime_epoch": 1567850700,
#         "utc_offset": "-4.0"
#     },
#     "current": {
#         "observation_time": "02:05 PM",
#         "temperature": 15,
#         "weather_code": 113,
#         "weather_icons": [
#             "https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
#         ],
#         "weather_descriptions": [
#             "Sunny"
#         ],
#         "wind_speed": 0,
#         "wind_degree": 0,
#         "wind_dir": "N",
#         "pressure": 1011,
#         "precip": 0,
#         "humidity": 78,
#         "cloudcover": 0,
#         "feelslike": 15,
#         "uv_index": 5,
#         "visibility": 16
#     },
#     "historical": {
#         "2008-07-01": {
#             "date": "2008-07-01",
#             "date_epoch": 1214870400,
#             "astro": {
#                 "sunrise": "05:29 AM",
#                 "sunset": "08:31 PM",
#                 "moonrise": "03:24 AM",
#                 "moonset": "07:37 PM",
#                 "moon_phase": "Waning Crescent",
#                 "moon_illumination": 4
#             },
#             "mintemp": 0,
#             "maxtemp": 0,
#             "avgtemp": 19,
#             "totalsnow": 0,
#             "sunhour": 14.5,
#             "uv_index": 4,
#             "hourly": [
#                 {
#                     "time": "0",
#                     "temperature": 27,
#                     "wind_speed": 7,
#                     "wind_degree": 201,
#                     "wind_dir": "SSW",
#                     "weather_code": 113,
#                     "weather_icons": [
#                         "https://assets.weatherstack.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png"
#                     ],
#                     "weather_descriptions": [
#                         "Sunny"
#                     ],
#                     "precip": 1.8,
#                     "humidity": 80,
#                     "visibility": 9,
#                     "pressure": 1011,
#                     "cloudcover": 15,
#                     "heatindex": 25,
#                     "dewpoint": 20,
#                     "windchill": 24,
#                     "windgust": 11,
#                     "feelslike": 25,
#                     "chanceofrain": 0,
#                     "chanceofremdry": 0,
#                     "chanceofwindy": 0,
#                     "chanceofovercast": 0,
#                     "chanceofsunshine": 0,
#                     "chanceoffrost": 0,
#                     "chanceofhightemp": 0,
#                     "chanceoffog": 0,
#                     "chanceofsnow": 0,
#                     "chanceofthunder": 0,
#                     "uv_index": 6
#                 },
#                 {   "time": "300", ...   },
#                 {   "time": "600", ...   },
#                 // 6 more items
#             ]
#         }
#     }
# }