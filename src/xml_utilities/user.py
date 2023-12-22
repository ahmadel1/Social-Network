class User:
    id = ""
    name = ""
    posts = None
    following = None
    followers = None

    def __init__(self):
        self.posts = list()
        self.following = list()
        self.followers = list()

    def set_following_array(self, users):
        for user in users:
            if self.id in user.followers:
                self.following.append(user.id)
