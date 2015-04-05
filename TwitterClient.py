import tweepy

class TwitterClient:

    api_key = ""
    api_secret = ""
    access_token = ""
    access_token_secret = ""
    auth = ""

    def __init__(self, key, secret, token, token_secret):
        self.api_key = key
        self.api_secret = secret
        self.access_token = token
        self.access_token_secret = token_secret
        self.auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
        self.auth.set_access_token(token, token_secret)

    def getTweets(self, hashtag):
        api = tweepy.API(self.auth)
        tweets = api.search(q = "#" + hashtag, rpp = 1)

        print tweets[0].text
        return tweets[0].text