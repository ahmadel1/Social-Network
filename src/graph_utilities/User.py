<<<<<<< HEAD
from Post import Post

class User:
    name = ""
    id = 0
    posts = []
    followers = []
    suggestions = []
    def __str__(self):
        print("Name:",self.name)
        print("id:",self.id)
        print("followers:",self.followers)
        print("posts:",self.posts)
        return "\n"
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.followers = []
        self.suggestions = []
        self.posts = []
    def addFollower(self,follower_id):
=======
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
>>>>>>> 65dac0f05b1c975b84d961a4417c65ead7fc370f
        self.followers.append(follower_id)

    def getName(self):
        return self.name

    def getId(self):
        return self.id

    def getFollowers(self):
        return self.followers

    def hasFollower(self, follower_id):
        return follower_id in self.followers
<<<<<<< HEAD
    def addPost(self,topics,body):
        post = Post()
        for topic in topics:
            post.addTopic(topic)
        post.setBody(body)
        self.posts.append({"Topics":post.topics,"Body":post.body})
    def getPosts(self):
        return self.posts
    
    

=======

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
>>>>>>> 65dac0f05b1c975b84d961a4417c65ead7fc370f
