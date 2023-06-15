import speech_recognition as sr
import json
with open("./config/api_keys.json", "r") as f:
  jsonString = json.load(f)
  apiKey = jsonString["openApi"]

r = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic, duration=0.1)
            audio = r.listen(mic)

            text = r.recognize_whisper_api(audio,api_key=apiKey)
            text = text.lower()
            print(text)
        pass
    except:
        r = sr.Recognizer()
        continue