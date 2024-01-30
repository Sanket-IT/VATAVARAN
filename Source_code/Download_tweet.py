import tweepy
import pandas as pd
from numpy import unicode
import os
from Source_code import Path_file as pf
from datetime import date

# The class to authenticate Twitter application to have twitter Application program interface(API)
# Step 1 to authenticate Twitter application to have twitter API
class authenticate:

    # Credentials for Twitter Application (The application created as twitter developer)
    consumer_key = "4pGM2Oc47rsdU9zoPWS65B9Z7" # Consumer key
    consumer_secret = "TnftL6K8ezxjU1CInHPcMWnd4ceOWpjdtuadQkDyN9Cm5ldqDh" # Consumer secrete
    access_token = "1418503648292708352-XBG4URl95Z4b9NETMN49DsmurfYTMc" # access token
    access_token_secret = "DFz806uA3hwBEPKkYJKfNOepYgdCQMgNO3lrNpHTFhxts" # Access_token_secret

# The method authenticates the credentials of user in order to connect to Twitter
    def authenticator(self):

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        # return authorization handler
        return auth

#Class to download tweets
class save_to_csv:

    #def get_tweets(self,api,listOfTweets, keyword, numOfTweets):
    def get_tweets(self,api,listOfTweets, keyword):

        # iterate through all tweets containing the given word, api search mode
        #for tweet in tweepy.Cursor(api.search, q=keyword, lang="en").items(numOfTweets ):

        for tweet in tweepy.Cursor(api.search, q=keyword,until=date.today(),lang="en").items():

            # create column heads for storing details of tweet
            # Add tweets in this format
            dict1 = { 'Screen Name ': tweet.user.screen_name,
                     'User Name ': tweet.user.name,
                     'Tweet Created At': unicode(tweet.created_at),
                     'Tweet Text': tweet.text,
                     'User Location': unicode(tweet.user.location),
                     'Retweet Count': unicode(tweet.retweet_count),
                     'Retweeted': unicode(tweet.retweeted),
                     'Phone Type': unicode(tweet.source),
                     'Favorite Count':unicode(tweet.favorite_count),
                     'Favorited ':unicode(tweet.favorited),
                     'Replied': unicode(tweet.in_reply_to_status_id_str)
                     }
            # create list of dictionaries
            listOfTweets.append(dict1)

            #print(listOfTweets)
        return listOfTweets

#Class to save tweets in csv file
class Startpoint:
    def Access(self,Topic_name):
        #Authenticate the user
        au =authenticate() # Creating the object of authenticate
        authentication=au.authenticator() # Function to authenticate and return authorization

        #API to manipulate data
        api = tweepy.API(authentication, wait_on_rate_limit = True, wait_on_rate_limit_notify= True )

        # Accept Topic,no of tweet,and csv name from use
        #Topic=input("Enter the Topic: ")
        Topic=Topic_name
        subjectname=Topic
        #Tweet_no=int(input("Enter no of Tweets: "))

        #creating object of
        STCSV=save_to_csv()

        # passing parameter to get_tweet method
        #Tweet_list=STCSV.get_tweets(api,list(),Topic,Tweet_no)
        Tweet_list=STCSV.get_tweets(api,list(),Topic)
        df = pd.DataFrame(Tweet_list) # the single tweet is saved as dictionary and saved it in list and this added into dataframe

        os.chdir(pf.DOWNLOAD_CSV)
        # created csv
        df.to_csv(Topic+'.csv')
        return Topic,subjectname





