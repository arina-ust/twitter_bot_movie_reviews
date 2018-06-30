# Twitter bot that retweets tweets containing keywords

This twitter bot retweets recent tweets from its timeline. 

The retweet is based on the keywords that are specified in the variable `keywords` that, in turn, is stored in the file `keywords.py`. The variable `keywords` is a list of strings.  
The bot does not retweet a new tweet if this tweet contains the same URL as its recent retweets.

Twitter's tokens (consumer key, consumer secret, access token, access token secret) are stored in the `credentials.py`.

The bot is built for running on AWS Lambda, but can be run locally as well.

------------------------------------------
__Useful links__  
Basic tutorials:  
- https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app
- https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library

Twitter and Tweepy docs:  
- https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/intro-to-tweet-json
- http://docs.tweepy.org/en/v3.6.0/api.html
- https://gist.github.com/dev-techmoe/ef676cdd03ac47ac503e856282077bf2
- https://gist.github.com/jaymcgrath/367c521f1dd786bc5a05ec3eeeb1cb04

AWS Lambda:  
- https://vickylai.com/verbose/free-twitter-bot-aws-lambda/
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
- https://aws.amazon.com/lambda/resources/#Getting_Started
