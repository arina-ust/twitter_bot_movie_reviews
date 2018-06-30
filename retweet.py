#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 21:40:43 2018

@author: Arina

Twitter bot for retweeting tweets that contain specified keywords.

Intial version: implementing a slightly changed code from
https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library
"""

from time import sleep

import tweepy
from credentials import consumer_key, consumer_secret, access_token, access_token_secret
from keywords import keywords


def authorize_api():
    """Perform user's authentication and return the API to work with."""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def retweet(api):
    """Retweet tweets that contain keywords from the latest 20 tweets of the
    home timeline."""
    for tweet in tweepy.Cursor(api.home_timeline, count=20, include_entities=True,
                               tweet_mode='extended').items(25):
        try:
            for keyword in keywords:
                if (keyword in tweet.full_text) and (not has_duplicate_url(api, tweet)):
                    try:
                        tweet.retweet()
                        sleep(5)
                    except tweepy.TweepError as exception:
                        print(exception)
        except StopIteration:
            break

def has_duplicate_url(api, tweet):
    """Check if this tweet has the same url as recently retweeted ones."""
    url_to_check = tweet.entities['urls'][0]['url']
    for my_tweet in tweepy.Cursor(api.user_timeline, count=20, include_rts=True,
                                  tweet_mode='extended').items(35):
        if url_to_check == my_tweet.retweeted_status.entities['urls'][0]['url']:
            return True
    return False

def handler(event, context):
    """Handler function for AWS lambda"""
    retweet(authorize_api())

# for local runs
#handler(None, None)