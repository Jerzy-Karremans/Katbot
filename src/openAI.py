import os
import openai
import json

with open("./config/api_keys.json", "r") as f:
  jsonString = json.load(f)
  apiKey = jsonString["openApi"]
  
openai.api_key = apiKey

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="You: What have you been up to?\nFriend: Watching old movies.\nYou: Did you watch anything interesting?\nFriend:",
  temperature=0.5,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0,
  stop=["You:"]
)

print(response["choices"][0]["text"])