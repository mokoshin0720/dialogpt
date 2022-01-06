from train.config import *
from train.main import *
from data.df import *
from data.dataset import * 
from data.loader import *

if __name__ == "__main__":
    model, tokenizer, optimizer = prepare_train('microsoft/DialoGPT-small')
    df = prepare_df()
    dataset = MyDataset(df, tokenizer)
    train_loader = prepare_loader(dataset)
    model_train(
        model=model,
        tokenizer=tokenizer,
        optimizer=optimizer,
        train_dataloader=train_loader,
    )