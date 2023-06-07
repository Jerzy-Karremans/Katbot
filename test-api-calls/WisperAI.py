import os
import openai

openai.api_key = os.getenv("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")

audio_file= open("C:/Users/jerzy/source/repos/Katbot/test-api-calls/test.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)