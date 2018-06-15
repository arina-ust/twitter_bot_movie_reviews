#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:40:43 2018

@author: Arina

Intial version: implementing a slightly changed code from 
https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library
"""

import tweepy
from time import sleep
from credentials import *
from keywords import keywords


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

for tweet in tweepy.Cursor(api.home_timeline, count=20).items():
    print(tweet)
    print('-----------------------------')
    for keyword in keywords:    
        if keyword in tweet.text:
            try:
                tweet.retweet()
                sleep(5)
            except tweepy.TweepError as e:
                print(e)
            except StopIteration:
                break