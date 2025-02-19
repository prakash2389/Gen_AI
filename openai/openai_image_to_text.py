
### Extracting image info from local or from cloud

import base64
from openai import OpenAI

api_key = "********************************************"
client = OpenAI(api_key=api_key)

# Function to encode the image
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
image_path = r"D:\openai\Supply of Goods.png"

# Getting the Base64 string
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Extract the text i in this image?",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0])


# print(response.choices[0].message.content)
# Here’s the extracted text from the image:
# | Sr No. | Description of Supply of Goods                                                                  | Supplier of Goods                                                       | Recipient of Goods                                         |
# |--------|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|----------------------------------------------------------|
# | 1.     | Cashew nuts, not shelled or peeled                                                             | Agriculturist                                                          | Any registered person                                      |
# | 2.     | Bidi wrapper leaves (tendu)                                                                    | Agriculturist                                                          | Any registered person                                      |
# | 3.     | Tobacco leaves                                                                                 | Agriculturist                                                          | Any registered person                                      |
# | 4.     | Silk yarn                                                                                      | Any person who manufactures silk yarn from raw silk or silk worm cocoons for supply of Silk Yarn | Any registered person                                      |
# | 5.     | Raw cotton                                                                                     | Agriculturist                                                          | Any registered person                                      |
# | 6.     | Supply of lottery                                                                               | State Government, Union Territory or any local authority               | Lottery distributor or selling agent                      |
# | 7.     | Used vehicles, seized and confiscated goods, old and used goods, waste and scrap               | Central Government, State Government, Union territory or a local authority | Any registered person                                      |
