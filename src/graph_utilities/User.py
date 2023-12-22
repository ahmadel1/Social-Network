class Post:
    topic = ""
    body = ""
    def __init__(self):
        pass
    def setTopic(self,topic):
        self.topic = topic
    def setBody(self,body):
        self.body = body
    def getTopic(self):
        return self.topic
    def getBody(self):
        return self.body

class User:
    name = ""
    id = 0
    posts = []
    followers = []
    suggestions = []
    def __str__(self) -> str:
        pass
    def __init__(self,name,id):
        self.name = name
        self.id = id
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
    def addPost(self,topic,body):
        post = Post()
        post.setTopic(topic)
        post.setBody(body)
        self.posts.append({"Topic":post.topic,"Body":post.body})
    def getPosts(self):
        return self.posts
    
    
    


user1 = User("Ahmed Ali",1)
user2 = User("Ali Khalid",2)
user1.addFollower(2)
user1.addPost("Color","This is a mixture of green,blue and red colors")
user1.addPost("Car","This is a red car")


print(user1.getFollowers())
print(user1.getPosts())
