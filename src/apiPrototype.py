import speech_recognition as sr
import openai
import json
with open("./config/api_keys.json", "r") as f:
  jsonString = json.load(f)
  apiKey = jsonString["openApi"]

r = sr.Recognizer()
openai.api_key = apiKey

def promptGPT(message):
    return openai.Completion.create(
    model="text-davinci-003",
    prompt=f"You: {message} friend:",
    temperature=0.5,
    max_tokens=60,
    top_p=1,
    frequency_penalty=0.5,
    presence_penalty=0,
    stop=["You:","je: ","\n"]
    )
    
while True:
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=0.1)
            audio = r.listen(mic)

            text = r.recognize_whisper_api(audio,api_key=apiKey)
            text = text.lower()
            print("you: " + text)
            print("GPT: " + promptGPT(text)["choices"][0]["text"])
        pass
    except:
        print("I didnt catch that")
        r = sr.Recognizer()
        continue