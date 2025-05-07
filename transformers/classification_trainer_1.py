from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset

# Load data
dataset = load_dataset("imdb")

# Tokenize data
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

def tokenize_function(data):
    return tokenizer(data["text"], padding="max_length", truncation=True)

tokenized_datasets = dataset.map(tokenize_function, batched=True, cache_file_names=None)

model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    logging_dir="./logs",
    save_total_limit=2,
)

from transformers import Trainer

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets["train"][:1000],
    eval_dataset=tokenized_datasets["test"][1000:2000],
    tokenizer=tokenizer,
)
trainer.train()
