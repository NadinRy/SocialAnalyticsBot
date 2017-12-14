import tweepy


class TwitterCrawler:
    def __init__(self):
        self.consumer_key = "JaLm8Ft9Wft5b02m1bAmHsa0S"
        self.consumer_secret = "PVHzVhWlCEwVakVAwUbcGXNTYJWHHYKkAf1BYSiMxMMOD7FyvY"
        self.access_key = "527809087-BKtvl8pdHUOKFP4QD3UoqW7JWAjWLKqChMXl3a2h"
        self.access_secret = "VBZqCinjj9Yafj36bn9QiydyToy4ScRBhLd0sYIDEk1hL"
        self.api = tweepy.API(self.auth)

    @property
    def auth(self):
        """Установка соединения."""
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_key, self.access_secret)
        return auth

    def tweet_search(self, query):
        """Поиск твитов."""
        text = ''
        results = self.api.search(q=query, lang='en', rpp=99)
        for tweet in results:
            text += tweet.text
        return text

