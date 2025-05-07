
# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("document-question-answering", model="fxmarty/tiny-doc-qa-vision-encoder-decoder")

# Define the document and the question
document = """The Apollo program, also known as Project Apollo, was the third United States
human spaceflight program carried out by the National Aeronautics and Space Administration (NASA),
which succeeded in landing the first humans on the Moon from 1969 to 1972."""

question = "What was the goal of the Apollo program?"

# Get the answer
answer = pipe(question=question, context=document)
print(answer)
# {'score': 0.9999999403953552, 'start': 63, 'end': 90, 'answer': 'succeeded in landing the first humans on the Moon'}




