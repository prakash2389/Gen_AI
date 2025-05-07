from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load data
dataset = load_dataset("imdb")

# Tokenize data
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
def tokenize_function(example):
    return tokenizer(example["text"], padding="max_length", truncation=True)


dataset = {"text" :["I am positive", "I am negative", "I am neutral"], "label": [1, 0, 2]}
tokens = tokenizer(dataset["text"], padding="max_length", truncation=True)
tokens['input_ids'][0]
tokens['token_type_ids'][0]
tokens['attention_mask'][0]

dataset = ["I am positive", "I am negative", "I am neutral"]
tokens = tokenizer(dataset, padding="max_length", max_length= 20, truncation=True, return_tensors = "pt")

from transformers import AutoModelForSequenceClassification
model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased")
t =tokens['input_ids']

outputs = model(**tokens, output_hidden_states=True, output_attentions=True)

outputs.hidden_states[0].size()
outputs.last_hidden_state

outputs.attentions[0].size()
