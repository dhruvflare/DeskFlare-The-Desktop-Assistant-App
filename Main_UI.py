# imports
# import pyaudio
import speech_recognition as sr
# import wikipedia
import win32com.client
import webbrowser
# import openai
import AppOpener
import datetime

speaker = win32com.client.Dispatch("SAPI.SpVoice")

sites = [
                ["youtube", "https://www.youtube.com/"],
                ["google", "https://www.google.com/"],
                ["mail", "https://mail.google.com/mail/u/0/#inbox"]
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
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language=lan)
            print(f'user said {query}')
            return query

        except Exception:
            return "Could not recognise, please say again..."


def main():
    say('hello i am deskFlare AI')
    text = ''
    language = 'en-us'
    while text.lower() != "exit":

        if text.lower() == 'speak hindi':
            language = 'en-in'

        elif text.lower() == 'speak english':
            language = 'en-us'

        elif "search for" in text.lower():
            buffer = text.lower().split()
            q = ''
            for i in range(len(buffer)):
                if buffer[i - 1] == 'search' and buffer[i] == 'for':
                    q = '+'.join(str(e) for e in buffer[i + 1:])
                    break
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

        print(f"listening..[{language}]")
        text = take_command(lan=language)
        # say(text)


if __name__ == '__main__':
    main()
