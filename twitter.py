import tweepy
consumer_key="cbHbgztcsgGZ2JB3lUuSYnLaB"
consumer_secret="jJtBBMV9GdoA2SquWMe93e1DyfD2tdtbJXP4I3xTutikXoxNCb"
access_token="1404428071-uDf5CZO63xSb0XVDXA2tmn6aUA8BZAltc7nU5si"
access_token_secret="ASEq0nhEL9e7nbzO2DpkKxfUtKsvFMg17ymfVKb4cnMb3"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth) 

# Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
public_tweets = api.home_timeline()
# foreach through all tweets pulled
for tweet in public_tweets:
   # printing the text stored inside the tweet object
   print(tweet.text)




