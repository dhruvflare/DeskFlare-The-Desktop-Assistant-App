# imports
# import pyaudio
import speech_recognition as sr
# import wikipedia
import win32com.client
import webbrowser
# import openai
import AppOpener
import datetime

import wikipedia

speaker = win32com.client.Dispatch("SAPI.SpVoice")

sites = [
    ["youtube", "https://www.youtube.com/"],
    ["google", "https://www.google.com/"],
    ["mail", "https://mail.google.com/mail/u/0/#inbox"],
    ["chatgpt", "https://chat.openai.com/"]
]

apps = [
    "spotify",
    "discord"
]


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
            say("Could not recognise, please say again...")
            return " "


def main():
    say('hello i am deskFlare AI')
    text = ''
    language = 'en-us'
    while True:

        if text.lower() != " ":
            continue

        elif text.lower() != "exit":
            break

        elif text.lower() == 'speak hindi':
            language = 'en-in'

        elif text.lower() == 'speak english':
            language = 'en-us'

        elif "search for" in text.lower():
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
                    AppOpener.open(app)

        elif "the time" in text.lower():
            timeval = datetime.datetime.now().strftime("%H:%M")
            say(f"sir, the time is {timeval}")

        elif "what is" in text.lower():
            buffer = text.lower().partition('what is')
            q = buffer[2]
            # print(wikipedia.summary(q, sentences=2))
            say(wikipedia.summary(q, sentences=5))

        elif "who is" in text.lower():
            buffer = text.lower().partition('who is')
            q = buffer[2]
            # print(wikipedia.summary(q, sentences=2))
            say(wikipedia.summary(q, sentences=5))

        elif "what is your name" in text.lower():
            say("my name is deskFlare AI")


        elif "what is your age" in text.lower():
            say("I am a bot, i am not a human")


        elif "what is your gender" in text.lower() or "what is your profession" in text.lower():
            say("I am a bot, i am not a human")

        print(f"listening..[{language}]")
        text = take_command(lan=language)


if __name__ == '__main__':
    main()
