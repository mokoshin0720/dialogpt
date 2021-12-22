from train.config import *
from data.df import * 
from data.dataset import * 

if __name__ == "__main__":
    # train('microsoft/DialoGPT-small', 100)
    model, tokenizer, optimizer = prepare_train('microsoft/DialoGPT-small')
    df = prepare_df()
    d = MyDataset(df, tokenizer)
    print(d[0])
    print(len(d))