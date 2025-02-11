import json
from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments

# Carregar o dataset a partir de um arquivo JSON


def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Converter a lista de dicionários em um dicionário com listas de valores
    formatted_data = {"pergunta": [], "resposta": []}
    for item in data:
        formatted_data["pergunta"].append(item["pergunta"])
        formatted_data["resposta"].append(item["resposta"])

    return Dataset.from_dict(formatted_data)


# Carregar o modelo e o tokenizer
model_name = "Salesforce/codegen-350M-mono"
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Adicionar um token de padding
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(model_name)

# Carregar o dataset
dataset = load_dataset('dataset.json')

# Tokenizar o dataset


def tokenize_function(examples):
    return tokenizer(examples['pergunta'], examples['resposta'], padding="max_length", truncation=True)


tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Configurar os argumentos de treinamento
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=3,
    weight_decay=0.01,
)

# Inicializar o Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
    eval_dataset=tokenized_datasets,
)

# Treinar o modelo
trainer.train()
