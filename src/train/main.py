from . import config
import torch

def model_train(model, tokenizer, optimizer, train_dataloader):
    epochs = 10
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    model.to(device)
    for epoch in range(0, epochs):
        print("")
        print('======== Epoch {:} / {:} ========'.format(epoch + 1, epochs))
        print('Training...')

        total_train_loss = 0
        model.train()
        
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
            # scheduler.step()
            # print(loss)
            
    model_path = 'model.pth'
    torch.save(model.state_dict(), model_path)