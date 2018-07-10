import tweepy

consumer_key = 'GL9tcAonfq02uVO9P4HmkzZKo'
consumer_secret = '2mAEKL51npVgpat2jm3uk0s13udQOd9G4FxY2drNTTgNMi0Ot3'
access_token = '200545877-7YdSwAA3kYSs9wiLzFre5MsrV9fZvP3kg3yphyDF'
access_token_secret = 'xUz3W6rFrm0AeVaXA9UNpFScAF8LfaHJayV6ZXS6v4Fut'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()

print(public_tweets)

