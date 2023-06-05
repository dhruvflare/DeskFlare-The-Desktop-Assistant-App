# imports
import pyaudio
import speech_recognition as sr
import wikipedia
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")


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

        except Exception as e:
            return "Could not recognise, please say again..."


def main():
    say('hello i am jarvis AI')
    text = ''
    language = 'en-us'
    while text.lower() != "exit":
        if text.lower() == 'speak hindi':
            language = 'en-in'

        elif text.lower() == 'speak english':
            language = 'en-us'

        print(f"listening..[{language}]")
        text = take_command(lan=language)
        # say(text)


if __name__ == '__main__':
    main()
