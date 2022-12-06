from flask import Flask, request, render_template
import tweepy
import model.predict as predict
from twitterKeys import twitter_keys
import json


# authorizing Twitter Library when app starts

auth = tweepy.OAuthHandler(twitter_keys.consumer_key, twitter_keys.consumer_secret)
auth.set_access_token(twitter_keys.access_token, twitter_keys.access_token_secret)
api = tweepy.API(auth)

app = Flask(__name__, template_folder='templates')

# Sets default page to index
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Adds routing to about page
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

# Code for main showcasing the top 5 results of a personality

'''
Function to predict personality type based on user input 
'''
@app.route('/predict', methods=['POST', 'GET'])

def prediction():
    if request.method == 'POST':
        data1 = request.form['input']
        # print("MBTI Personality type prediction:", data1)  # test code

        # checks to see if user input is none. If it is, then return "Error"
        if data1 is None:
            return 'Error'
        # If input has "twitter.com" in it, then execute code to get cleaned string of text
        elif 'twitter.com' in data1:
            screen_name = predict.get_screenname(data1)
            final_str = ""
            count = 0
            for status in tweepy.Cursor(api.user_timeline, screen_name=screen_name, tweet_mode="extended").items():
                count += 1
                if count == 10:
                    break
                # print(final_str)
                final_str += status.full_text
                cleanData = predict.cleanString(final_str) # Cleans Twitter input data
        else: # if user input is just text, then collect text as is.
            cleanData = data1
        # generate most compatible MBTI personality types based on match score
        pred = predict.convertToMbti(cleanData)
    else:
        pred = None
    # return table showcasing top 5 personalities that user input corresponds to
    return render_template('personalityFinder.html', docs=json.loads(pred),data1=data1)


if __name__ == '__main__':
    app.run(debug=True, port = 2000)