# coding: utf-8

from decouple import config
import tweepy

CKEY = config('CKEY')
CSECRET = config('CSECRET')
ATOKEN = config('ATOKEN')
ASECRET = config('ASECRET')

if __name__ == "__main__":
    oauth_keys = {
            'consumer_key': CKEY,
            'consumer_secret': CSECRET,
            'access_token_key': ATOKEN,
            'access_token_secret': ASECRET
            }

    auth = tweepy.OAuthHandler(oauth_keys['consumer_key'],
                               oauth_keys['consumer_secret'])
    api = tweepy.API(auth)
    co_working = tweepy.Cursor(api.search, q='coworking',
            geocode='-22.9325728,-43.2410248,15km').items(10)
