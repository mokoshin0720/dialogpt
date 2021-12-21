from . import config
import torch

def train(model_name: str, epochs: int):
    model, tokenizer, optimizer = config.prepare(model_name)
    text_1 = "Who was Jim Henson is is ?"
    text_2 = "Jim Henson was a puppeteer"
    encoded_1 = tokenizer.encode(text_1)
    encoded_2 = tokenizer.encode(text_2)
    
    for epoch in range(0, epochs):
        print("")
        print('======== Epoch {:} / {:} ========'.format(epoch + 1, epochs))
        print('Training...')

        total_train_loss = 0
        model.train()

        in_text = torch.tensor(encoded_1)
        out_text = torch.tensor(encoded_2)

        model.zero_grad()

        outputs = model(in_text, labels=out_text)
        loss = outputs[0]

        batch_loss = loss.item()
        total_train_loss += batch_loss

        loss.backward()

# def model_train():
    # for epoch in range(0, epochs):
    #     print("")
    #     print('======== Epoch {:} / {:} ========'.format(epoch_i + 1, epochs))
    #     print('Training...')

    #     total_train_loss = 0
    #     model.train()

    #     for step, batch in enumerate(train_dataloader):
    #         in_text = batch[?].to(device)
    #         out_text = batch[?].to(device)

    #         model.zero_grad()

    #         outputs = model(in_text, labels=out_text)
    #         loss = outputs[0]

    #         batch_loss = loss.item()
    #         total_train_loss += batch_loss

    #         loss.backward()
    #         optimizer.step()
    #         scheduler.step()