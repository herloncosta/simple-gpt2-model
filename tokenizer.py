import json
from datasets import Dataset
from transformers import AutoTokenizer


def load_and_process_dataset(filename="dataset_atendimento.json"):
    with open(filename, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    dataset = Dataset.from_dict(
        {"text": [f"Pergunta: {item['pergunta']} Resposta: {item['resposta']}" for item in dataset]})

    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    tokenizer.pad_token = tokenizer.eos_token

    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=128)

    tokenized_datasets = dataset.map(
        tokenize_function, batched=True, remove_columns=["text"])

    tokenized_datasets = tokenized_datasets.train_test_split(
        test_size=0.2)
    return tokenized_datasets, tokenizer
