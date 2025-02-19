from openai import OpenAI
api_key = "********************************************"
client = OpenAI(api_key=api_key)

completion = client.chat.completions.create(
    # model="gpt-4o",
    # model="gpt-4o-mini",
    model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "20*30 + 3"
        }
    ],
    response_format={
        "type": "text"
    }
)

print(completion.choices[0].message.content)

### 2 + 3 equals 5.

