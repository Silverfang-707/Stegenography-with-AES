# Import necessary libraries
import pandas as pd
from tqdm import tqdm

import os
import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
)
from peft import LoraConfig, PeftModel
from trl import SFTTrainer
# Load and display the first few rows of the dataset
df = pd.read_csv("llm.csv")
df.head()
# Preprocess the dataset by removing hyperlinks and mentions
for i in range(len(df)):
    l = df['response'][i]
    text = l.replace("<hyperlink>","")
    l = text.replace("<mention>","")
    df['response'][i] = l
# Here test set is the validation set

# Split the data into train and test sets, with 90% in the train set
train_df = df.sample(frac=0.9, random_state=42)
test_df = df.drop(train_df.index)

# Save the dataframes to .jsonl files
train_df.to_json('train.jsonl', orient='records', lines=True)
test_df.to_json('test.jsonl', orient='records', lines=True)
# Set up model configuration and training parameters
model_name = "NousResearch/llama-2-7b-chat-hf"
dataset_name = "/content/train.jsonl"
new_model = "llama-2-7b-custom"
lora_r = 64
lora_alpha = 16
lora_dropout = 0.1
use_4bit = True
bnb_4bit_compute_dtype = "float16"
bnb_4bit_quant_type = "nf4"
use_nested_quant = False
output_dir = "./results"
num_train_epochs = 2
fp16 = False
bf16 = False
per_device_train_batch_size = 4
per_device_eval_batch_size = 4
gradient_accumulation_steps = 1
gradient_checkpointing = True
max_grad_norm = 0.3
learning_rate = 2e-4
weight_decay = 0.001
optim = "paged_adamw_32bit"
lr_scheduler_type = "constant"
max_steps = -1
warmup_ratio = 0.03
group_by_length = True
save_steps = 25
logging_steps = 5
max_seq_length = None
packing = False
device_map = {"": 0}
# Load datasets
train_dataset = load_dataset('json', data_files='/content/train.jsonl', split="train")
valid_dataset = load_dataset('json', data_files='/content/test.jsonl', split="train")

# Preprocess datasets
train_dataset_mapped = train_dataset.map(lambda examples: {'text': [prompt + ' [/INST] ' + response for prompt, response in zip(examples['prompt'], examples['response'])]}, batched=True)
valid_dataset_mapped = valid_dataset.map(lambda examples: {'text': [prompt + ' [/INST] ' + response for prompt, response in zip(examples['prompt'], examples['response'])]}, batched=True)
# Configure quantization parameters
compute_dtype = getattr(torch, bnb_4bit_compute_dtype)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=use_4bit,
    bnb_4bit_quant_type=bnb_4bit_quant_type,
    bnb_4bit_compute_dtype=compute_dtype,
    bnb_4bit_use_double_quant=use_nested_quant,
)

# Load pre-trained model
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map=device_map
)
model.config.use_cache = False
model.config.pretraining_tp = 1
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

# Configure LoRA-specific parameters
peft_config = LoraConfig(
    lora_alpha=lora_alpha,
    lora_dropout=lora_dropout,
    r=lora_r,
    bias="none",
    task_type="CAUSAL_LM",
)
training_arguments = TrainingArguments(
    output_dir=output_dir,
    num_train_epochs=num_train_epochs,
    per_device_train_batch_size=per_device_train_batch_size,
    gradient_accumulation_steps=gradient_accumulation_steps,
    optim=optim,
    save_steps=save_steps,
    logging_steps=logging_steps,
    learning_rate=learning_rate,
    weight_decay=weight_decay,
    fp16=fp16,
    bf16=bf16,
    max_grad_norm=max_grad_norm,
    max_steps=max_steps,
    warmup_ratio=warmup_ratio,
    group_by_length=group_by_length,
    lr_scheduler_type=lr_scheduler_type,
    report_to="all",
    evaluation_strategy="steps",
    eval_steps=50  # Evaluate every 50 steps
)
# Set supervised fine-tuning parameters
trainer = SFTTrainer(
    model=model,
    train_dataset=train_dataset_mapped,
    eval_dataset=valid_dataset_mapped, 
    peft_config=peft_config,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    tokenizer=tokenizer,
    args=training_arguments,
    packing=packing,
)

# Train the model
trainer.train()
# Save the fine-tuned model
trainer.model.save_pretrained(new_model)
# Suppress logging messages to avoid unnecessary output
logging.set_verbosity(logging.CRITICAL)

# Create text generation pipelines using the specified model and tokenizer
# Define two pipelines with different maximum lengths
pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=250)
pipe2 = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=500)

# Initialize an empty list to store generated text
generated_text = []

# Iterate over the test data
for i in tqdm(range(len(final_test_data))):
    # Extract the prompt from the test data
    prompt = final_test_data['prompt'].iloc[i]
    
    # Attempt to generate text using the first pipeline with a max length of 250
    try:
        result = pipe(prompt)
        # Append the generated text to the list, extracting the relevant part after '[/INST]'
        generated_text.append(result[0]['generated_text'].split('[/INST]')[1])
    except:
        # If an exception occurs, try the second pipeline with a max length of 500
        try:
            result = pipe2(prompt)
            # Append the generated text to the list, extracting the relevant part after '[/INST]'
            generated_text.append(result[0]['generated_text'].split('[/INST]')[1])
        except:
            # If both pipelines fail, append a default placeholder text
            generated_text.append("ABCD1234@#")

# The 'generated_text' list now contains the generated text for each prompt in the test data
# Assign the generated text to a new column 'generated_text' in the 'final_test_data' DataFrame
final_test_data['generated_text'] = generated_text

# Reset the index of the DataFrame for a cleaner representation in the CSV file
final_test_data = final_test_data.reset_index(drop=True)

# Save the DataFrame to a CSV file at the specified path
final_test_data.to_csv('/content/drive/MyDrive/llama2_finetune_output_1128.csv', index=False)
# Set the path where the merged model will be saved
model_path = "llama-2-7b-custom" 

# Reload the base model in FP16 and configure settings
base_model = AutoModelForCausalLM.from_pretrained(
    model_name,
    low_cpu_mem_usage=True,  
    return_dict=True,        
    torch_dtype=torch.float16,  
    device_map=device_map,    
)

# Instantiate a PeftModel using the base model and the new model
model = PeftModel.from_pretrained(base_model, new_model)  # Combine the base model and the fine-tuned weights

# Merge the base model with LoRA weights and unload unnecessary parts
model = model.merge_and_unload()  # Finalize the model by merging and unloading any redundant components

# Reload the tokenizer to save it
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True) 
tokenizer.pad_token = tokenizer