from pathlib import Path
from openai import OpenAI

api_key = "********************************************"
client = OpenAI(api_key=api_key)

speech_file_path = r"D:\openai\speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="what can you tell about palm oil industry in india. How import and export are there for palm oil industry in india?",
)
response.stream_to_file(speech_file_path)