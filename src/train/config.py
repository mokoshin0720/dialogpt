from transformers import AutoTokenizer, AutoModelForCausalLM, AdamW, GPT2LMHeadModel, GPT2TokenizerFast

def prepare_train(model_name: str) -> (GPT2LMHeadModel, GPT2TokenizerFast, AdamW):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    optimizer = AdamW(model.parameters(), lr=1e-5)
    return model, tokenizer, optimizer