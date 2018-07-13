#from tweepy.auth import OAuthHandler

import tweepy

auth = tweepy.OAuthHandler("seDQpzrTycYZh3zoGJk56KPEJ", "mmI6xm1fTtTEgdB0KZwvb40zbwnVOxufxy8vB3su0jVJtEcpvf")
auth.set_access_token("2634719374-y6DbhuovgQEEoLPV5KZgjRN3y9LxjELXCaDa5PO", "6wu0xNK2yjU4rYczqArGzceGaPW1sjuTGj9fg18tSElQ1")


api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print (tweet.text)
