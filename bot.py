#!/usr/bin/python3

import tweepy
import random
import os

from secrets import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
twitter = tweepy.API(auth)

photo_file = os.path.join("polaroids", os.listdir("polaroids")[0])
comment = random.choice([
        "Hmm ...",
        "Remember this party?",
        "Oh dear.",
        "Huh.",
        "Uh ...",
        "I totally forgot about this.",
        "Oh geeze.",
        "This one's going in my scrapbook.",
        "...",
        "Whose house even was this?",
        "I don't remember this at all.",
        "Er ...",
        "Those were the days.",
        "I miss that crew.",
        "Nice shirt.",
        "Wait, who's that?"
    ])

tweet = twitter.update_with_media(photo_file, comment)
os.remove(photo_file)
