import json
import tweepy


class TwitterClient:
    def __init__(self, conf_file):
        with open(conf_file, 'r') as conf_json:
            conf = json.load(conf_json)
            api_key = conf['api_key']
            api_secret_key = conf['api_secret_key']
            access_token = conf['access_token']
            access_token_secret = conf['access_token_secret']

            auth = tweepy.OAuthHandler(api_key, api_secret_key)
            auth.set_access_token(access_token, access_token_secret)

            self.api = tweepy.API(auth)

    def get_follower_count(self, username):
        return self.api.get_user(username).followers_count
