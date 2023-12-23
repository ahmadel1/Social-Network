from .post import *


class User:
    name = ""
    id = ""
    posts = None
    followers = None
    following = None

    def __str__(self) -> str:
        return f"User {self.name} (ID: {self.id})"


    def __init__(self):
        self.posts = list()
        self.following = list()
        self.followers = list()

    def addFollower(self, follower_id):
        self.followers.append(follower_id)

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getFollowers(self):
        return self.followers

    def hasFollower(self, follower_id):
        return follower_id in self.followers

    def addPost(self, post):
        self.posts.append(post)

    def getPosts(self):
        return self.posts

    def getFollowing(self):
        return self.following

    def setFollowingArray(self, users):
        for user in users:
            if user.hasFollower(self.id):
                self.following.append(user.id)
