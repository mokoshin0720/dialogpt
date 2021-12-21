# from runner.runner import run
# from dataset.dataset import trn_df, val_df
from train.main import train

if __name__ == "__main__":
    train('microsoft/DialoGPT-small', 3)