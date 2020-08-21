# coding: utf-8

import tweepy
import pandas as pd
from langdetect import detect
from datetime import datetime 
from datetime import timedelta
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only
env_path = Path('../.env') 
load_dotenv(dotenv_path=env_path)
import os

consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_key = os.getenv("ACCESS_KEY")
access_secret = os.getenv("ACCESS_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_key, access_secret) 
api = tweepy.API(auth) 

screenname = ["narendramodi","WHO","CDCgov","COVID19CA","CovidIndiaSeva","UK COVID-19","COVID19_USA_","ashishkjha","COVIDNewsByMIB","MoHFW_INDIA"]

tweet,tweets_dates,text_query,hyperlinks,screennames_twitter = [], [], ["CORONA","COVID"], [], []

count = 0
for i in screenname:
    tweets = api.user_timeline(screen_name=i,count=10,tweet_mode="extended")  
    for status in tweets:
        for text in text_query:
            if text in status.full_text and detect(status.full_text)=="en" and "RT" not in status.full_text:
                tweet.append(status.full_text)
                tweets_dates.append(status.created_at)
                screennames_twitter.append('@'+status.user.screen_name)
                if len(status.entities['urls']) >0:
                    hyperlinks.append(status.entities['urls'][0]['url'])
                else:
                    hyperlinks.append('#')

for i in range(len(tweet)):
    if hyperlinks[i] == '0' and 'https://' in  tweet[i]:
        somet = tweet[i].find("https://")
        hyperlinks[i] = tweet[i][somet::]
        tweet[i] = tweet[i].replace(hyperlinks[i],' ')
        

for i in range(len(tweet)):
    if hyperlinks[i] != '0':
        somet = tweet[i].find("https://")
        hyperlinks[i] = tweet[i][somet::]
        tweet[i] = tweet[i].replace(hyperlinks[i],' ')
        
df = pd.DataFrame({"Screen Name":screennames_twitter,"Tweets":tweet,"Timeframe":tweets_dates,"Links":hyperlinks})
df.to_csv('All-Tweets.csv',index=False)   
df.sort_values(by=['Timeframe'], inplace=True, ascending=False)
df = df[df["Links"] != '#']
df = df.reset_index(drop=True)
df