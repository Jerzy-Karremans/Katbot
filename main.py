import speech_recognition as sr
import pyttsx3
from src.gpt import gpt

def setup_speech_engine():
    engine = pyttsx3.init()
    return engine

def speech_to_text(r):
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=0.1)
        audio = r.listen(mic)
        text = r.recognize_whisper_api(audio, api_key=api_key)
        text = text.lower()
    return text

def main():
    r = sr.Recognizer()
    engine = setup_speech_engine()

    while True:
        try:
            text = speech_to_text(r)
            print("You: " + text)
            response = gpt.prompt_gpt(text)
            print("GPT: " + response)
            engine.say(response)
            engine.runAndWait()
        except sr.UnknownValueError:
            print("I didn't catch that. Please try again.")
            continue
        except sr.RequestError:
            print("An error occurred while processing the speech.")
            break

api_key = gpt.load_api_key()
if __name__ == "__main__":
    main()