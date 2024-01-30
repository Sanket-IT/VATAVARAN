from wordcloud import STOPWORDS
from nltk.corpus import stopwords
s1=set(stopwords.words('english'))
s2=set(STOPWORDS)
set3=s1.union(s2)
print(set3)
print(len(set3))



def Wordcloud(self,cleaned_csv,topic):
        os.chdir(pf.CLEANED_CSV)
        df = pd.read_csv(cleaned_csv, usecols=['Remove url'])
        answer = [''.join(df.values[:, i]) for i in range(len(df.columns))]
        # answer.append(list())
        print(answer)

        # Python program to generate WordCloud
        # importing all necessery modules
        # Reads 'Youtube04-Eminem.csv' file
        comment_words = ' '
        stopwords = set(STOPWORDS)
        # iterate through the csv file

        for val in answer:
        # typecaste each val to string
            val = str(val)

        # split the value
        tokens = val.split()

        # Converts each token into lowercase
        for i in range(len(tokens)):
            tokens[i] = tokens[i].lower()

        for words in tokens:
            comment_words = comment_words + words + ' '

        wordcloud = WordCloud(width=900, height=900,
        background_color = 'black',
        stopwords = set3,
        min_font_size = 20,
        max_font_size=200,mode="RGBA" ).generate(comment_words)

        # plot the WordCloud image
        plt.figure(figsize=(8, 8), facecolor=None)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.tight_layout(pad=0)
        os.chdir(pf.WORD_CLOUD)
        plt.savefig(topic+'cloud.png')

#present.Wordcloud(cleaned_csv_tweet, subject)

x=[cnt0,cnt1,cnt2,cnt3,cnt4,cnt5,cnt6]
        labs = ['Disaster', 'Rain', 'Thunder','Cloudy','Fog','Snow','Clear']
        plt.pie(x, labels=labs)
        os.chdir(pf.PIE_CHART)
        plt.savefig(subjectname+'.png')
