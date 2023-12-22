from user import *
from post import *
from abc import ABC, abstractmethod


class ObjectCreator(ABC):
    json_dict = None

    def __init__(self, json_dict):
        self.json_dict = json_dict

    @abstractmethod
    def create_object(self):
        pass


class PostCreator(ObjectCreator):
    def __init__(self, json_dict):
        super().__init__(json_dict)

    def create_object(self):
        post = Post()
        for key, value in self.json_dict.items():
            if key == "body":
                post.body = value
            if key == "topics":
                if isinstance(value["topic"], list):
                    # iterate through array of (JSON) topics
                    for topic in value["topic"]:
                        post.topics.append(topic)
                else:
                    post.topics.append(value["topic"])
        return post


class UserCreator(ObjectCreator):
    def __init__(self, json_dict):
        super().__init__(json_dict)

    def create_object(self):
        user = User()
        for key, value in self.json_dict.items():
            if key == "id":
                user.id = value
            if key == "name":
                user.name = value
            if key == "posts":
                if isinstance(value["post"], list):
                    # iterate through array of (JSON) posts
                    for json_post in value["post"]:
                        # create new post creator object to avoid mutation
                        post_creator = PostCreator(json_post)
                        user.posts.append(post_creator.create_object())
                else:
                    post_creator = PostCreator(value["post"])
                    user.posts.append(post_creator.create_object())

            if key == "followers":
                if isinstance(value["follower"], list):
                    # iterate through array of (JSON) followers
                    for follower in value["follower"]:
                        user.followers.append(follower["id"])
                else:
                    follower = value["follower"]
                    user.followers.append(follower["id"])
        return user
