import torch
from transformers import GPT2Config, GPT2LMHeadModel, TrainingArguments, DataCollatorForLanguageModeling, Trainer


def create_and_train_model(tokenized_datasets, tokenizer):
    config = GPT2Config(
        vocab_size=tokenizer.vocab_size,
        n_positions=128,
        n_ctx=128,
        n_embd=768,
        n_layer=6,
        n_head=6
    )

    model = GPT2LMHeadModel(config)

    training_args = TrainingArguments(
        output_dir="./results",
        overwrite_output_dir=True,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        save_total_limit=2,
        save_steps=500,
        logging_dir="./logs",
        logging_steps=100,
        evaluation_strategy="steps",
        eval_steps=100,
        warmup_steps=100,
        weight_decay=0.01,
        fp16=torch.cuda.is_available(),
    )

    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_datasets["train"],
        eval_dataset=tokenized_datasets["test"],
        data_collator=data_collator,
    )

    trainer.train()

    return trainer
