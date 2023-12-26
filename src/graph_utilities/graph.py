from .User import *
from .post import *
from .dictionary import *
from .template import *
from ..xml_utilities.xmlToJson import *


class Graph:
    def __init__(self, users):
        self.users = Dictionary()
        self.adjacency_list = Dictionary()
        for user in users:
            self.users[user.id] = user
            self.adjacency_list[user.id] = user.following

    def get_mutuals(self, user1_id, user2_id):
        user1_followers = self.users[user1_id].getFollowers()
        user2_followers = self.users[user2_id].getFollowers()
        mutuals = []
        for follower_id in user1_followers:
            if follower_id in user2_followers:
                mutuals.append(self.users[follower_id])
        return mutuals

    def displayNetwork(self):
        for id, users in self.adjacency_list.items():
            print(f" user({id}): is connected to ({users})")

    def get_most_activer(self):
        pass

    def get_most_influencer(self):
        # instantiate the appropriate breadth-first search template class
        influencer_searcher = bfs_most_influencer(self.users, self.adjacency_list)
        return influencer_searcher.get_result()

    def get_suggestions(self):
        # instantiate the appropriate breadth-first template class
        suggestion_searcher = bfs_suggestions(self.users, self.adjacency_list)
        return suggestion_searcher.get_result()

    def search_posts(self, topic):
        # instantiate the appropriate breadth-first template class
        post_searcher = bfs_posts(self.users, self.adjacency_list)
        return post_searcher.get_result(topic)


xml_string = get_xml_string_fromPath("src/xml_utilities/Sample files/sample.xml")
# create a tree from the xml string
xml_tree = create_tree(xml_string)
# convert the tree to a dictionary
json_dict = xml_to_json(xml_tree.root)
# create user array form  (JSON) object
users = get_users_array(json_dict)

# construct the graph and test the methods
network = Graph(users)
network.displayNetwork()
posts = network.search_posts("economy")
for post in posts:
    print(post)
print(network.get_suggestions())
print(network.get_most_influencer())
print(network.get_mutuals("2", "3")[0].name)
