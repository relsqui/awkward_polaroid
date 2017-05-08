#!/usr/bin/python3

import tweepy
import random

from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

with open("for_consuming") as f:
    photos = f.read().splitlines()

random.shuffle(photos)
photo_file = grams.pop()
comment = random.choice([
        "Hmm ...",
        "Oh my.",
        "Awkward.",
        "Remember this party?",
        "What was happening here?",
        "What was his name ...",
        "What was her name ...",
        "What was their name ...",
        "Oh dear.",
        "Huh.",
        "Uh ...",
        "I totally forgot about this.",
        "Oh geeze.",
        "I'm going to pretend I never found this.",
        "This one's going in my scrapbook.",
        "Don't tell them we found this photo!",
        "...",
        "Goodness."
    ])

#tweet = twitter.update_with_media(photo_file, comment)
print("I would tweet " + photo_file + " and say: " + comment)

with open("for_consuming", "w") as f:
    f.write("\n".join(grams))

with open("tweet_history", "a") as f:
    f.write("{0}\t{1}\n".format(tweet.id, to_tweet))
