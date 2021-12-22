from train.config import *
from data.df import *
from data.dataset import * 
from data.loader import *

if __name__ == "__main__":
    # train('microsoft/DialoGPT-small', 100)
    model, tokenizer, optimizer = prepare_train('microsoft/DialoGPT-small')
    df = prepare_df()
    dataset = MyDataset(df, tokenizer)
    tmp = dataset[0]
    decoded1 = tokenizer.decode(tmp[0].tolist()[0])
    decoded2 = tokenizer.decode(tmp[1].tolist()[0])
    print(decoded1)
    print(decoded2)
    # prepare_loader(dataset)