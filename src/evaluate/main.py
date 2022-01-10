import torch

def model_eval(model, tokenizer, optimizer, eval_dateloader):
    load_path = '../../model.pth'
    load_weights = torch.load(load_path)
    model.load_state_dict(load_weights)
    
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)
    
    model.eval()
        
    for batch in train_dataloader:
        context, reply = batch
        in_text = context.to(device)
        out_text = reply.to(device)
        optimizer.zero_grad()
        outputs = model(in_text, labels=out_text)
        loss = outputs[0]
        batch_loss = loss.item()
        total_train_loss += batch_loss
        loss.backward()
        optimizer.step()

def print_output(tokenizer, model):
    load_path = 'src/evaluate/model_tmp.pth'
    load_weights = torch.load(load_path)
    model.load_state_dict(load_weights)
    
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)
    
    model.eval()
    
    
    input_sentence = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')
    output_sentence = model.generate(
    input_sentence, max_length=1000,
    pad_token_id=tokenizer.eos_token_id
    )
    
    reply = tokenizer.decode(output_sentence[0], skip_special_tokens=True)
    print("DialoGPT: {}".format(reply))