class Post:
    topics = []
    body = ""
    def __init__(self):
        self.topics = []
        self.body = ""
    def addTopic(self,topic):
        self.topics.append(topic)
    def setBody(self,body):
        self.body = body
    def getTopics(self):
        return self.topics
    def getBody(self):
        return self.body