import tweepy
from time import sleep
from keys import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

for tweet in tweepy.Cursor(api.search, q='hackathon', r='ideathon', s='programming marathon').items(5):
    try:
        print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + ' .')

        tweet.retweet()
        print('Retweet published successfully.')

        sleep(10)

    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Reason: ')
        print(error.reason)

    except StopIteration:
        break