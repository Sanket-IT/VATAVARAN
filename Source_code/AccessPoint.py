import os
from Source_code.Cleaning_of_Tweets import cleaning
from Source_code.Download_tweet import Startpoint
from Source_code.Graphical_repre import DrawGraphs
from Source_code.Naive_Bayse_Implementation import Train_algo
#from flask_restful import Resource


class Execution_Point:
    def __init__(self, topicname):
        self.topicname=topicname
        print(topicname)


    def Start_Excution(self):
        #Call Download_tweet
        start=Startpoint()
        store_topic,subject=start.Access(self.topicname)

        #Call cleaning_of_Tweets
        cln=cleaning(store_topic)
        cleaned_csv_tweet=cln.clean_Tweet(store_topic)

        #train model
        train=Train_algo(cleaned_csv_tweet)
        naive=train.train_naive(cleaned_csv_tweet,subject)

        #Generate Graph
        present = DrawGraphs(naive, subject)
        x=present.Graph_result(naive, subject)
        return x



