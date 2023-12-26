class Post:
    body = ""
    topic = None

    def __init__(self):
        self.topics = list()

    def setTopic(self, topic):
        self.topic = topic

    def setBody(self, body):
        self.body = body

    def getTopic(self):
        return self.topic

    def getBody(self):
        return self.body

    def __str__(self):
        return f"Post {self.body} (Topic: {self.topics})"

    def hasTopic(self, keyword):
        return keyword in self.topics
