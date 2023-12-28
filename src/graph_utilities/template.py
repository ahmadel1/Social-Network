from .User import *
from .post import *
from .dictionary import *
from abc import ABC, abstractmethod


class BFS_Template(ABC):
    def __init__(self, users, adjacency_list):
        self.users = users
        self.adjacency_list = adjacency_list

    @abstractmethod
    def process_user(self, user, target):
        pass

    def get_result(self, target=None):
        visited_nodes = Dictionary()
        queue = []

        # initialize visited_nodes
        for id, user in self.users.items():
            visited_nodes[id] = False

        for id, user in self.users.items():
            # if the user is not visited yet add it to the queue then start the bfs
            if not visited_nodes[id]:
                queue.append(id)

                while len(queue) > 0:
                    user_id = queue.pop(0)
                    # mark the user as visited
                    visited_nodes[user_id] = True
                    # get the user
                    user = self.users[user_id]

                    # call the variable step
                    self.process_user(user, target)

                    # add the user's neighbors to the queue
                    for neighbor_id in self.adjacency_list[user_id]:
                        if not visited_nodes[neighbor_id]:
                            queue.append(neighbor_id)
        return self.result


class bfs_suggestions(BFS_Template):
    def __init__(self, users, adjacency_list):
        self.result = Dictionary()  # key: user id, value: list of user objects
        super().__init__(users, adjacency_list)

    def get_followers(
        self,
        id,
        pass_id,
    ):
        followers = list()
        user = self.users[id]
        for follower_id in user.followers:
            if follower_id != pass_id:
                followers.append(self.users[follower_id])

        return followers

    def process_user(self, user, target):
        self.result[user.id] = list()
        for follower_id in user.followers:
            self.result[user.id].extend(self.get_followers(follower_id, user.id))

        return self.result


class bfs_most_influencer(BFS_Template):
    def __init__(self, users, adjacency_list):
        self.result = None  # user object
        super().__init__(users, adjacency_list)

    def process_user(self, user, target):
        if self.result == None:
            self.result = user
        elif len(user.followers) > len(self.result.followers):
            self.result = user

        return self.result


class bfs_posts(BFS_Template):
    def __init__(self, users, adjacency_list):
        self.result = list()  # list of post objects
        super().__init__(users, adjacency_list)

    def process_user(self, user, target):
        for post in user.posts:
            if post.hasKeyword(target):
                self.result.append(post)

        return self.result


class bfs_active(BFS_Template):
    def __init__(self, users, adjacency_list):
        # key: user id, value: in degree + out degree of the user
        self.result = Dictionary()
        super().__init__(users, adjacency_list)

    def process_user(self, user, target):
        self.result[user.id] = len(user.followers) + len(user.following)

        return self.result
