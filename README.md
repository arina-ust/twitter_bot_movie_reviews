# Twitter bot that retweets tweets containing keywords

This twitter bot retweets recent tweets from its timeline. 

The retweet is based on the keywords that are specified in the variable `main_keywords`. If a tweet contains any keyword, it is retweeted. If not, it is then checked to contain any of the keywords of `tweet_keywords` variable. This variable is a set of secondary keywords that signal that the tweet may be of interest.  
For my purposes, I'm interested in the author of an article that can be reached by a URL in that tweet. (This same author is listed among `main_keywords` as well<sup>*</sup>). Hence, 'newspaper' library is used to download and parse this information from the URL provided in the tweet of interest. If indeed `author` is the article's author, the tweet is retweeted.  
The variables `main_keywords` and `tweet_keywords`are a list of strings, the variables `author` and `lang` are a string, and they are stored in the file `keywords.py`. 
The bot does not retweet a new tweet if this tweet contains the same URL as its recent retweets.

Twitter's tokens (consumer key, consumer secret, access token, access token secret) are stored in the `credentials.py`.

The bot is built for running on AWS Lambda, but can be run locally as well.  

<sup>*</sup>As I parse Russian webpages, `author` is not the same as a keyword in `main_keywords`, because I have to take care of changing endings.

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

Newspaper docs:
- https://newspaper.readthedocs.io/en/latest/

AWS Lambda:  
- https://vickylai.com/verbose/free-twitter-bot-aws-lambda/
- https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
- https://aws.amazon.com/lambda/resources/#Getting_Started
