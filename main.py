from Instagram import Instagram
from Twitter import Twitter

I = Instagram(name="mahdi")
print("Enter the body of post:")
iBody = input()
I.publishNewPost(iBody)
post = I.getPosts()
for p in post:
    print(p)

T = Twitter(name="mahdi2")
print("Enter the body of tweet:  ")
tBody = input()
T.createNewTweet(tBody)
tweet = T.getTweets()
for t in tweet:
    print(t)
