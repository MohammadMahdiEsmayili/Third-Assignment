from SocialMedia import SocialMedia


class Twitter(SocialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.tweets = []

    def createNewTweet(self, tweet):
        if len(tweet) < 280:
            self.tweets.append({"tweet": tweet})
        else:
            print("The length of tweet is not acceptable")

    def getTweets(self):
        return self.tweets
