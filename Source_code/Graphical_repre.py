import pandas as pd
import matplotlib.pyplot as plt;
from wordcloud import WordCloud, STOPWORDS
from wordcloud import STOPWORDS
from nltk.corpus import stopwords

s1=set(stopwords.words('english'))
s2=set(STOPWORDS)
set3=s1.union(s2)
set3.add('rt')
set3.add('RT')

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import os
from Source_code import Path_file as pf


class DrawGraphs():

    def __init__(self, polarityfile,subjectname):
        self.polarityfile = polarityfile
        self.subjectname = subjectname

    def Graph_result(self,polarityfile,subjectname):
        os.chdir(pf.POLARITY_CSV)
        df=pd.read_csv(polarityfile,usecols=['Sentiment'])
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt4 = 0
        cnt5 = 0
        cnt6 = 0
        for x in df['Sentiment']:
            if x == '[0]':
                cnt0 += 1
            elif x == '[1]':
                cnt1 += 1
            elif x == '[2]':
                cnt2 += 1
            elif x == '[3]':
                cnt3 += 1
            elif x == '[4]':
                cnt4 += 1
            elif x == '[5]':
                cnt5 += 1
            elif x == '[6]':
                cnt6 += 1
        print('Disaster Tweets: ', cnt0)
        print('Rain Tweets: ', cnt1)
        print('Thunder and lightning Tweets: ', cnt2)
        print('Cloudy Tweets: ',cnt3)
        print('Fog Tweets: ',cnt4)
        print('Snow Tweets: ',cnt5)
        print('Clear Weather Tweets: ',cnt6)
        sixe = df.size
        for i in range(0, sixe):
            value = df.loc[i]

        #color = ['black', 'red', 'green']
        objects = ('Disaster', 'Rain', 'Thunder','Cloudy','Fog','Snow','Clear')
        y_pos = np.arange(len(objects))
        performance = [cnt0, cnt1, cnt2,cnt3,cnt4,cnt5,cnt6]

        plt.bar(y_pos, performance, align='center', alpha=0.5)
       # plt.bar(y_pos, performance, align='center', alpha=0.5, color=['black', 'red', 'green'])
        plt.xticks(y_pos, objects)
        plt.ylabel('Sentiment')
        plt.title('Catagories')
        os.chdir(pf.BAR_CHART)
        plt.savefig(subjectname+'.png')
        plt.clf()

    




