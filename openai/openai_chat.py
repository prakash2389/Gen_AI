from openai import OpenAI

api_key = "***************************************************************************"

client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    # model="gpt-4o",
    model="gpt-4o-mini",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "2+3"
        }
    ]
)

print(completion.choices[0].message.content)

### 2 + 3 equals 5.

