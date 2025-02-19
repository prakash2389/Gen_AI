
from pydantic import BaseModel
from openai import OpenAI

api_key = "********************************************"
client = OpenAI(api_key=api_key)

class Step(BaseModel):
    explanation: str
    result: str

class Calculate(BaseModel):
    steps: list[Step]
    answer: str

completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "system", "content": "You are a helpful math tutor. Guide the user through the solution step by step."},
        {"role": "user", "content": "If i take loan of 10 lakhs for 3 years at 12% rate of interest. how much will be the EMI?"}
    ],
    response_format=Calculate,
)

Calculate_reasoning = completion.choices[0].message

# If the model refuses to respond, you will get a refusal message
if (Calculate_reasoning.refusal):
    print(Calculate_reasoning.refusal)
else:
    print(Calculate_reasoning.parsed)

for i, val in enumerate(Calculate_reasoning.parsed.steps):
    print(f"Step {i+1}: {val.explanation}")
    print(f"Result {i+1}: {val.result}")

# Step 1: The formula for EMI (Equated Monthly Installment) calculation is EMI = [P * r * (1+r)^n] / [(1+r)^n – 1], where P is the principal loan amount, r is the monthly interest rate, and n is the number of months for which the loan is taken.
# Result 1: Understand the EMI formula.
# Step 2: The principal loan amount P is 10 lakhs, which is Rs. 10,00,000.
# Result 2: P = 10,00,000
# Step 3: The annual interest rate is 12%, so the monthly interest rate r is 12% / 12 months = 1% = 0.01.
# Result 3: r = 0.01
# Step 4: The loan term is 3 years, which is 3 * 12 = 36 months.
# Result 4: n = 36
# Step 5: Substitute P = 10,00,000, r = 0.01, and n = 36 into the EMI formula: EMI = [10,00,000 * 0.01 * (1+0.01)^36] / [(1+0.01)^36 – 1].
# Result 5: Substitute values into EMI formula.
# Step 6: Calculate (1+0.01)^36. First, evaluate 1+0.01 = 1.01, then (1.01)^36 using a calculator.
# Result 6: (1.01)^36 ≈ 1.4307687
# Step 7: Continue with EMI calculation: EMI = [10,00,000 * 0.01 * 1.4307687] / [1.4307687 – 1].
# Result 7: Substitute (1.01)^36 ≈ 1.4307687 into EMI formula.
# Step 8: Calculate the numerator: 10,00,000 * 0.01 * 1.4307687 ≈ 14307.687.
# Result 8: Numerator = 14307.687
# Step 9: Calculate the denominator: 1.4307687 - 1 = 0.4307687.
# Result 9: Denominator = 0.4307687
# Step 10: Divide the numerator by the denominator to find EMI: 14307.687 / 0.4307687 ≈ 33214.79.
# Result 10: EMI ≈ 33214.79