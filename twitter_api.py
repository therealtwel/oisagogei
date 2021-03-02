import tweepy
import re

consumer_key = '0siCW7gRvpI6kVEdpIWVeYiEP'
consumer_secret = 'kwFH6bIu7pFZqpnTEnwHwruK5SeBhQOQXDpX5Jlb4bgEADqvC1'
access_token = '1366413277459316738-M9htNHlBNo1sH6VaXIhERhfUXXG4OM'
access_token_secret = '7H6qzuv2lPQIZHWd10K48tiTpJhRERF6WPNDuryry9WP1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

username = input("Enter the name of a Twitter user: @")

"""Getting the entire text from the requested user's last 10 posts via Twitter's API"""
public_tweets = api.user_timeline(screen_name = username, count = 10, include_rts = True)
entire_text = ""
for tweet in public_tweets:
    entire_text+=" "+tweet.text

"""Splitting the text and sorting it to easily locate longest and shortest words"""    
all_words_list = entire_text.split()
sortedwords = sorted(all_words_list, key=len)

"""removing twitter links as they clog up the longest words"""
link = re.compile("t.co")
word_kept = False
while not word_kept:
    if link.search(sortedwords[-1]):
        sortedwords.pop(-1)
    else:
        word_kept = True   
    
print("The 5 shortest words in this user's tweets:")
for i in range (5):
    print(sortedwords[i])
    
print("The 5 longest words in this user's tweets:")
for i in range (-1,-6,-1):
    print(sortedwords[i])
