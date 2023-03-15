# sentiment_analysis
A study conducted to analyse the public sentiment towards the app of BPI.

The dataset consists of tweets that mention the word app referring to BPI.
To conduct this, the model was fine-tuned on twitter-XLM-roBERTa-base which is a multilingual XLM-roBERTa-base model trained on ~198M tweets and finetuned for sentiment analysis. The sentiment fine-tuning was done on 8 languages (Ar, En, Fr, De, Hi, It, Sp, Pt) but it can be used for more languages (see paper for details). https://arxiv.org/abs/2104.12250

You can find the model repository in https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment

