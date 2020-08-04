import tweepy 
from tkinter import *
from collections import Counter

consumer_key = '#'
consumer_secret = '#'
access_token = '#'
access_token_secret = '#'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()
print(user.name)

verbose = True
test_mode = False

users = []
tweets = []
for tweet in tweepy.Cursor(api.user_timeline).items():
    #print(tweet.text)
    
    if tweet.retweeted:
        tweets.append(tweet)
        users.append(tweet.retweeted_status.user.screen_name)

#create dictionary of user screen_names (@'s) and their frequency values
ctr = Counter(users)

#randoms dictionary will hold screen_names of users that have only been retweeted by you once
#these are people that are most likely not close friends
randoms = dict()
for key, values in ctr.items():
    if values < 2:
        randoms[key] = values

#delete tweets that belong to randoms 
for key, values in randoms.items():
    for tweet in tweets:
        if key == tweet.retweeted_status.user.screen_name: #and ('RT @' in tweet.text)and (tweet.retweeted)
            if verbose:
                print ("Deleting %d: [%s] %s" % (tweet.id, tweet.created_at, tweet.text))
                #break
            if not test_mode:
                api.destroy_status(tweet.id)
                time.sleep(1)
                break
                
                    
