from tokenizer import load_and_process_dataset
from trainer import create_and_train_model


def testing_model(trainer, tokenizer):
    input_text = "Pergunta: Como cancelar meu plano? Resposta:"
    inputs = tokenizer(input_text, return_tensors="pt")

    outputs = trainer.model.generate(
        inputs["input_ids"],
        max_length=128,
        num_return_sequences=1,
        temperature=0,
        top_k=50,
        top_p=0.95,
    )

    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Generated text: ", generated_text)


if __name__ == "__main__":
    tokenized_datasets, tokenizer = load_and_process_dataset()
    trainer = create_and_train_model(tokenized_datasets, tokenizer)
    testing_model(trainer, tokenizer)
