import openai
import json
import speech_recognition as sr
import pyttsx3
from elevenlabs import generate, play,set_api_key

def load_api_keys():
    with open("./config/api_keys.json", "r") as f:
        json_string = json.load(f)
        open_ai_api_key = json_string["openApi"]
        set_api_key(json_string["elevenlabs"])
        usingEleven = bool(json_string["usingEleven"])
    return open_ai_api_key, usingEleven

def prompt_gpt(message,api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"You: {message} friend:",
        temperature=0.5,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0,
        stop=["You:", "je: "]
    )
    return response["choices"][0]["text"]

def play_eleven_audio(message):
    audio = generate(
    text=message,
    voice="Bella",
    model="eleven_monolingual_v1"
    )

    play(audio)

def speech_to_text(r):
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=0.1)
        audio = r.listen(mic)
        text = r.recognize_google(audio)
        text = text.lower()
    return text

def setup_speech_engine():
    engine = pyttsx3.init()
    return engine

def main():
    r = sr.Recognizer()
    engine = setup_speech_engine()
    open_api_key,usingEleven = load_api_keys()
    while True:
        try:
            text = speech_to_text(r)
            if text == "" or text =="you" or text.isalpha() or text == "thank you.":
                print("misinput                                                                                                    |")
                continue
            print("You: " + text)
            response = prompt_gpt(text,open_api_key)
            print("GPT: " + response)
            if usingEleven:
                play_eleven_audio(response)
            else:
                engine.say(response)
                engine.runAndWait()
        except sr.UnknownValueError:
            print("I didn't catch that. Please try again.")
            continue
        except sr.RequestError:
            print("An error occurred while processing the speech.")
            break

if __name__ == '__main__':
    _,usingEleven = load_api_keys()
    if usingEleven:
        play_eleven_audio("sound test")
    else:
        engine = setup_speech_engine()
        engine.say("sound test")
        engine.runAndWait()
    main()