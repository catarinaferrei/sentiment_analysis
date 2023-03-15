import os
import twint
import pandas as pd



def main():
    config = twint.Config()
    config.Lang = "pt"

    config.Pandas = True
    config.Store_csv = True
    config.Output = "Output_moretweet.csv"
    df = twint.storage.panda.Tweets_df

    
    config.Search = "bpi"
    config.Limit = 10000
    twint.run.Search(config)


if __name__ == "__main__":
    main()