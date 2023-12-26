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
        self.followers.append(follower_id)
    def getName(self):
        return self.name
    def getId(self):
        return self.id
    def getFollowers(self):
        return self.followers
    def hasFollower(self,follower_id):
        return follower_id in self.followers
    def addPost(self,topics,body):
        post = Post()
        for topic in topics:
            post.addTopic(topic)
        post.setBody(body)
        self.posts.append({"Topics":post.topics,"Body":post.body})
    def getPosts(self):
        return self.posts
    
    

