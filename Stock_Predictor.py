import os
import sys
import tweepy
import requests
import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from textblob import TextBlob

#login into twitter to get sentiment analysis

consumer_key ='cCPSWMppGcgKZJpxq4m5yKLF1'
consumer_secret = 'fnrGFRByL1J2cEYdnmzxSmDm4VGSxseJGO6G5JtR1TGsv5wfzA'
access_token = '2320549866-iGRZLF08ix5vICwoTjUELxQU8Acndln4dr2I2LM'
access_token_secret ='rLiDXi6rocU3KKpjsj3dLtJo1DXZSfPoRa66u8OBIr6N8'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
user = tweepy.API(auth)

#FILE_NAME== 'stock.csv'


def stock_sentiment(quote, num_tweets):
    #checking our quote like "Lupin stock" or "Apple stock" in tweets.
    
    list_of_tweets = user.search(quote, count=num_tweets);
    positive, null = 0,0
    
    for tweet in list_of_tweets:
        #saving sentiment in blob variable
        blob = TextBlob(tweet.text).sentiment
        if blob.subjectivity == 0:
            null+=1
            next
        if blob.polarity > 0:
            positive+=1
    if positive>((num_tweets-null)/2):
        return 'positive'
    else:
        return 'negative'


'''def get_historical(quote):
    #download our stock file from google finance (DATASET for training and testing)
    url = 'http://finance.google.com/finance/historical?q=AAPL&output=csv'

    #http://finance.google.com/finance/historical?q=NSE%3ALUPIN&output=cs&output=csv
    r = requests.get(url, stream=True)

    if r.status_code != 400:
        with open(FILE_NAME, 'wb') as f:
            for chunk in r:
                f.write(chunk)

        return True

def stock_prediction():

    #collecting data points from csv file
    dataset = []

    with open(FILE_NAME) as f:
        for n, line in enumerate(f):
            if n !=0:
                dataset.append(float(line.split(',')[1]))


    dataset = np.array(dataX), dataset[2:]

    #create_dataset matrix


    '''
stock_quote = input('Enter a Stock : ').upper()
print(stock_sentiment(stock_quote, num_tweets=10000))
