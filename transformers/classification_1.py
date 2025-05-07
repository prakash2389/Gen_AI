##Clinical Notes Classification

## We’ll classify clinical notes into categories like
## Discharge Summary, Radiology Report, Progress Notes, etc., using fine-tuned Medical BERT.

## 1. Load Medical BERT
## 2. Prepare Data
## 3. Define Trainer
## 4. Train the Model
## 5. Evaluate

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments
from datasets import load_dataset, DatasetDict
from sklearn.model_selection import train_test_split
import torch

# Step 1: Load Medical BERT
model_name = "emilyalsentzer/Bio_ClinicalBERT"  # Medical BERT model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)  # Assume 3 classes

# Step 2: Prepare Data
# Example data
data = {
    "text": [
        "Patient discharged with prescription for hypertension.",
        "Radiology report indicates a small fracture.",
        "The patient is stable and advised for follow-up."
    ],
    "label": [0, 1, 2]  # 0: Discharge Summary, 1: Radiology Report, 2: Progress Notes
}

# Split into train and test
texts, labels = data["text"], data["label"]
train_texts, val_texts, train_labels, val_labels = train_test_split(texts, labels, test_size=0.2, random_state=42)

# Tokenize
train_encodings = tokenizer(train_texts, truncation=True, padding=True, max_length=512)
val_encodings = tokenizer(val_texts, truncation=True, padding=True, max_length=512)

# Convert to DatasetDict
train_dataset = DatasetDict({
    "input_ids": train_encodings["input_ids"],
    "attention_mask": train_encodings["attention_mask"],
    "labels": torch.tensor(train_labels)
})

train_dataset = [DatasetDict({
    "input_ids": x,
    "attention_mask": z,
    "labels": y
}) for x,y,z in zip(train_encodings['input_ids'],train_labels, train_encodings['attention_mask'])]

val_dataset = DatasetDict({
    "input_ids": val_encodings["input_ids"],
    "attention_mask": val_encodings["attention_mask"],
    "labels": torch.tensor(val_labels)
})

val_dataset = [DatasetDict({
    "input_ids": x,
    "attention_mask": z,
    "labels": y
}) for x,y,z in zip(val_encodings['input_ids'],val_labels, val_encodings['attention_mask'])]


# Step 3: Define Trainer
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    num_train_epochs=1,
    weight_decay=0.01,
    logging_dir="./logs",
    logging_steps=1,
    save_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer
)

# Step 4: Train the Model
trainer.train()

# Step 5: Evaluate
results = trainer.evaluate()
print(results)
