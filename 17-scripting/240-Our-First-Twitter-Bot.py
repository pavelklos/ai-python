# 240 : Our First Twitter Bot

# You will need to PIP INSTALL tweepy for this to work and also create a twitter API.
# Run this on your own machine, not in this Repl.
# > pip install tweepy==3.8
# > pip install tweepy

import time

import tweepy

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name)  # prints your name.
print(user.screen_name)
print(user.followers_count)

search = "zerotomastery"
numberOfTweets = 2


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)


# Be nice to your followers. Follow everyone!
for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == "Usernamehere":
        print(follower.name)
        follower.follow()

# Be a narcisist and love your own tweets, or retweet anything with a keyword!
for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print("Retweeted the tweet")
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

# TODO: [twitterbot.py] --------------------------------------------------------

# import tweepy
# import time
#
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''
#
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
# api = tweepy.API(auth)
#
# user = api.me()
# # print(user)     # it gives all the details, like name, scree_name, location, and various other info.
# print(user.name)  # prints your name.
# print(user.screen_name)
# print(user.followers_count)
#
# search = "bitcoin"
# numberOfTweets = 2
#
#
# def limit_handle(cursor):
#     while True:
#         try:
#             yield cursor.next()
#
#         except tweepy.RateLimitError:
#             print("Sleeping now....")
#             time.sleep(10)  # sleeps for 10 secs
#
#
# # for follower in limit_handle(tweepy.Cursor(api.followers).items()):
# #     print(follower.name)
# #     if follower.name == 'Usernamehere':
# #         print(follower.name)
# #         follower.follow()
#
#
# for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
#     try:
#         tweet.favorite()
#         tweet.retweet()
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break
