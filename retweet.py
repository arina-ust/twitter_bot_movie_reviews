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
from newspaper import Article

from credentials import consumer_key, consumer_secret, access_token, access_token_secret
from keywords import main_keywords, tweet_keywords, author, lang


def authorize_api():
    """Perform user's authentication and return the API to work with."""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


def retweet(api):
    """Retweet tweets that contain keywords from the latest 25 tweets of the
    home timeline."""
    for tweet in tweepy.Cursor(api.home_timeline, count=25, include_entities=True,
                               tweet_mode='extended').items(25):
        try:
            for keyword in main_keywords:
                if valid_tweet(api, tweet, keyword):
                    post_retweet(tweet)
                    return
            for keyword in tweet_keywords:
                if valid_tweet(api, tweet, keyword):
                    article = Article(get_url(tweet), language=lang)
                    article.download()
                    article.parse()
                    if (author in article.authors):
                        post_retweet(tweet)
                        return
        except StopIteration:
            break


def valid_tweet(api, tweet, keyword):
    """Check if the tweet contains the keyword and that this tweet
    has not been previously retweeted."""
    return (keyword in tweet.full_text) and (not has_duplicate_url(api, tweet))

def has_duplicate_url(api, tweet):
    """Check if this tweet has the same url as recently retweeted ones."""
    url_to_check = get_url(tweet)
    for my_tweet in tweepy.Cursor(api.user_timeline, count=20, include_rts=True,
                                  tweet_mode='extended').items(20):
        if url_to_check == my_tweet.retweeted_status.entities['urls'][0]['url']:
            return True
    return False


def get_url(tweet):
    """Extract url from the tweet."""
    return tweet.entities['urls'][0]['url']


def post_retweet(tweet):
    """Retweet this tweet."""
    try:
        tweet.retweet()
        sleep(5)
    except tweepy.TweepError as exception:
        print(exception)


def handler(event, context):
    """Handler function for AWS lambda"""
    retweet(authorize_api())

# for local runs
#handler(None, None)
