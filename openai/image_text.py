from openai import OpenAI
client = OpenAI(api_key=***********************************************)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", 
                 "text": "What's in this image?"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://images.squarespace-cdn.com/content/v1/54a832fee4b0ac4256e4ceef/1456351027993-IZI4JHMHCLSNFM8UGYQH/20160219_0297.JPG?format=2500w",
                    },
                },
            ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0].message.content)

"""The image shows a pelican in flight over water. The bird has a light gray body, a long beak, and distinctive features. The background consists of rippling water."""


