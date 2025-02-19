import base64
from openai import OpenAI

api_key = "********************************************"
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "wav"},
    messages=[
        {
            "role": "user",
            "content": "what can you tell about palm oil industry in india. How import and export are there for palm oil industry in india?"
        }
    ]
)

print(completion.choices[0])

wav_bytes = base64.b64decode(completion.choices[0].message.audio.data)
with open(r"D:\openai\palm_oil.wav", "wb") as f:
    f.write(wav_bytes)