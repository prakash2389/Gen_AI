
from openai import OpenAI

api_key = "********************************************"
client = OpenAI(api_key=api_key)


def model_run(prompt, model):
    completion = client.chat.completions.create(
        model= model,
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format={
            "type": "text"
        }
    )
    return completion.choices[0].message.content


# model="gpt-4o",
# model="gpt-4o-mini",
# model = "gpt-3.5-turbo-1106",
# model="ft:gpt-3.5-turbo-1106:personal:math-prak-022025:B2asRUju",

for i in range(1, 10):
    prompt = f"12*12"
    print(f"{i} output: {model_run(prompt, model='gpt-3.5-turbo-1106')}")

# model = "gpt-3.5-turbo-1106",
"""
1 output: The expression 12*12-12+12*12 simplifies to 144 - 12 +144, which equals 276.
2 output: To calculate this expression, you would first multiply 12 by 12, then multiply that result by 12, and finally subtract the result from the product of 12 and 12. This would be:
12 * 12 = 144
144 * 12 = 1728
12 * 12 = 144
1728 - 144 = 1584
So, the result of the expression 12*12-12+12*12 is 1584.
3 output: The given expression is: 12*12 - 12 + 12*12.
First, multiply 12 by 12: 12*12 = 144.
Then, multiply the last 12 by 12: 12*12 = 144.
Now, substitute the results into the expression: 144 - 12 + 144.
Finally, calculate the result: 144 - 12 + 144 = 276.
4 output: The result of the calculation 12*12-12+12*12 is 252.
5 output: The result of the expression 12*12-12+12*12 is 216.
6 output: 12*12-12+12*12 = 144 - 12 + 144 = 276
7 output: The expression 12*12-12+12*12 simplifies to 144-12+144, which further simplifies to 288-12, resulting in a final answer of 276.
8 output: The expression 12*12-12+12*12 simplifies to 144 - 12 + 144, which equals 276.
9 output: The expression 12*12-12+12*12 equals 228.
"""


for i in range(1, 10):
    prompt = f"12*12"
    print(f"{i} output: {model_run(prompt, model='ft:gpt-3.5-turbo-1106:personal:math-prak-022025:B2asRUju')}")

# model = 'ft:gpt-3.5-turbo-1106:personal:math-prak-022025:B2asRUju'

"""
1 output: 12*12-12+12*12 = 144 - 12 + 144
                 = 288 - 12
                 = 276
2 output: The result of the expression 12*12-12+12*12 is 252.
3 output: 12 * 12 - 12 + 12 * 12 can be calculated as follows:
144 - 12 + 144
= 276
4 output: The result of the expression 12*12-12+12*12 is 276.
5 output: 144
6 output: The result of the expression 12*12-12+12*12 is 252.
7 output: 12 * 12 - 12 + 12 * 12 equals 252.
8 output: The answer to the expression 12*12-12+12*12 is 252.
9 output: 12*12-12+12*12 = 144 - 12 + 144
                    = 288 - 12
                    = 276
"""

