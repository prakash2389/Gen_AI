from openai import OpenAI

api_key = "********************************************"
client = OpenAI(api_key=api_key)

audio_file=open(r"D:\openai\palm_oil.wav", "rb")
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

print(transcription.text)

"""The palm oil industry in India plays a significant role in the country's economy. 
India is one of the largest importers of palm oil globally, as domestic production is limited. 
The country heavily relies on imports from countries like Indonesia and Malaysia to meet its demand. 
These imports are mainly used for edible purposes and in food processing. 
India also produces some palm oil domestically, primarily in states like Andhra Pradesh, Tamil Nadu, 
Karnataka, and others, but the production levels fall short of the domestic demand. 
As far as exports are concerned, India doesn't export palm oil in significant quantities, 
given its reliance on imports to satisfy domestic consumption needs. To reduce this dependence on imports, 
the Indian government has been encouraging the expansion of domestic palm oil cultivation, aiming 
for greater self-sufficiency."""
