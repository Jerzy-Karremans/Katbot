import openai
import json

def load_api_key():
    with open("./config/api_keys.json", "r") as f:
        json_string = json.load(f)
        api_key = json_string["openApi"]
    return api_key

def prompt_gpt(message):
    api_key = load_api_key()
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
