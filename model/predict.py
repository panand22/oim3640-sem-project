import tweepy
import pandas as pd
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import tweepy
import re
from twitterKeys import twitter_keys
from nltk.corpus import stopwords

# Twitter Authentication code
auth = tweepy.OAuthHandler(twitter_keys.consumer_key, twitter_keys.consumer_secret)
auth.set_access_token(twitter_keys.access_token, twitter_keys.access_token_secret)
api = tweepy.API(auth)


'''
Function to clean string 
Used to break down Twitter string received from inputted profile to break each word into a list and then convert it back to a comma-delimited string.
'''
def cleanString(input):
    stops = set(stopwords.words('english'))
    words = re.sub("[^\w]", " ",  input).split()
    list_words_cleaned = [w.lower() for w in words if w not in stops]
    wordsCleaned = ' '.join([str(w) for w in list_words_cleaned])
    return wordsCleaned

'''
Function to get string from Twitter API. 
Code not being called since Code was moved to app.py
'''
'''
def getString(string, api):
    if string is None:
        return 'Error'
    elif 'http' in string:
        screen_name = get_screenname(string)
        final_str = ""
        count = 0
        for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name, tweet_mode="extended").items():
            count += 1
            if count == 10:
                break
            print(final_str)
            final_str += status.full_text
    else:
        final_str = string

    return final_str
'''

'''
Function to get Twitter user screenname from Twitter profile link. 
Used in app.py to get tweets from a specific user
'''

def get_screenname(string):
    if string == "":
        return ""
    array = string.split("/")
    screen_name = array[-1].split("?")[0]
    return screen_name

'''
Main function to use inputted text to predict MBTI personality compatibility based on cleaned text
Generates table that showcases the top 5 most compatible personalities ranked by mathc score
'''

def convertToMbti(data1):
    # Splits text into individual words
    words = data1.split()

    # Reads data and creates a Pandas Dataframe from Inputted CSV file.
    ### Data is obtained from Kaggle: https://www.kaggle.com/datasets/datasnaek/mbti-type?resource=download

    datasource1 = pd.read_csv("data\Personalities.csv")
    datasource1 = pd.DataFrame(datasource1)

    # Creates empty list
    datasource2 = []

    '''
    Reads through individual words in inputted text and checks if they are also in the Personalities.csv file
    If the word is in the data file, then it adds that word to datasource2 list.
    '''
    for i in words:
        d2 = datasource1[datasource1['posts'].str.contains(str(i))]
        datasource2.append(d2)

    # Creates Pandas dataframe from datasource2 list
    datasource2 = pd.concat(datasource2, ignore_index=True)

    datasource2 = pd.DataFrame(datasource2)
    datasource2=datasource2.drop_duplicates()
    datasource2=datasource2.reset_index()
    #print(datasource.head()) test code

    # sets datasource = datasource 2 for simpliciity sake since it will be referenced a lot moving forward
    datasource=datasource2
    params = data1

    # Reads through each entry of the datasource and adds each entry to documents list
    for i in range(0, len(datasource)):
        documents = []
        documents.append(params)
        documents.append(datasource.loc[i, 'posts'])

    # Add stop_words and ngram_range to the TfidVectorizer below
            # received idea to use this library from StackOverflow: 
            # https://stackoverflow.com/questions/8897593/how-to-compute-the-similarity-between-two-text-documents

        tfidf = TfidfVectorizer(stop_words="english", ngram_range=(1, 4)).fit_transform(documents)

    # Generates similarity between two texts
        pairwise_similarity = tfidf * tfidf.T
        # Add stop word, Add ngram

        # Gets match score
        temp = pairwise_similarity.A[0][1]

        # Formats match score
        matchScore = "{0:.4f}".format(temp)
        datasource.loc[i, 'Match Score'] = matchScore

    datasource['Rank'] = datasource['Match Score'].rank(method='average', ascending=False)

    '''
    This code determines what to display for "Search Term" in the generated output table. 
    I added this code because it would take too long for all the text on a Twitter profile to show on the table. Moreover, all that text would not be pretty from a UI perspective.

    Therefore, I decided to check if the length of the inputted data was more than 200, then just display "Text too long to display" 

    If the search term is less than 200 characters, then it will display the actual search. 
    '''
    if len(data1)>200:
        datasource['Search Term'] = "Text too long to display"
    else:
        datasource['Search Term'] = data1

    datasource = datasource.sort_values('Rank', ascending=True)
    datasource = datasource.head(5)
    datasource = datasource.reset_index()

    # select columns to display
    datadisplay = datasource[
        ["type" ,"Rank",
        "Match Score","Search Term","Introversion/Extraversion","Intuitive/Observant","Thinking/Feeling","Judging/Perceiving"]]
    datadisplay.Rank = datadisplay.Rank.astype(np.int64)

    datadisplay=datadisplay.to_json(orient="records")
    return datadisplay