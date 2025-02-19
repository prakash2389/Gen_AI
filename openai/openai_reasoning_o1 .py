from openai import OpenAI

api_key = "********************************************"
client = OpenAI(api_key=api_key)

prompt = """
A shop sells custom-made bracelets. They charge $15 for the basic bracelet, 
plus $2 for each charm added. A customer spent $21 total on their bracelet. 
You need to buy atleast 2 bracelet.
How many charms did they add to their bracelet?
"""

response = client.chat.completions.create(
    model="o3-mini",
    reasoning_effort="medium",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response.choices[0].message.content)