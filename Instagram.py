from SocialMedia import SocialMedia


class Instagram(SocialMedia):
    def __init__(self, name):
        super().__init__(name)
        self.posts = []

    def publishNewPost(self, post):
        if len(post) < 2200:
            self.posts.append({"post": post})
        else:
            print("The length of post is not acceptable")

    def getPosts(self):
        return self.posts
