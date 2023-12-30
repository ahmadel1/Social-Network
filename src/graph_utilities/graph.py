from .User import *
from .post import *
from .dictionary import *
from .template import *
from ..xml_utilities.xmlToJsonParser import *
from ..xml_utilities.xmlToJson import *
import networkx as nx
import matplotlib.pyplot as plt


class Graph:
    def __init__(self, xml_string):
        parser = XmlToJsonParser(xml_string)
        users_array = parser.get_usersArray()
        self.users = Dictionary()
        self.adjacency_list = Dictionary()

        # construct the graph
        for user in users_array:
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

    def get_most_active(self):
        active_searcher = bfs_active(self.users, self.adjacency_list)
        result = active_searcher.get_result()
        return self.users[max(result, key=result.__getitem__)]

    def get_most_influencer(self):
        influencer_searcher = bfs_most_influencer(self.users, self.adjacency_list)
        return influencer_searcher.get_result()

    def get_suggestions(self):
        suggestion_searcher = bfs_suggestions(self.users, self.adjacency_list)
        return suggestion_searcher.get_result()

    def search_posts(self, topic):
        post_searcher = bfs_posts(self.users, self.adjacency_list)
        return post_searcher.get_result(topic)
    
    def draw_network(self):
        G = nx.DiGraph()
        for user_id, followers in self.adjacency_list.items():
            if self.users[user_id]:
                G.add_node(self.users[user_id].id)
                G.add_edges_from((self.users[user_id].id, self.users[follower].id) for follower in followers)

        pos = nx.shell_layout(G)
        rotated_pos = {node: (y, -x) for node, (x, y) in pos.items()}

        nx.draw(G, rotated_pos, with_labels=False, node_size=700, node_color='skyblue', font_size=15, edge_color='gray', arrowsize=20,
                connectionstyle="arc3,rad=0.1")

        labels = {node: str(node) for node in G.nodes}
        nx.draw_networkx_labels(G, rotated_pos, labels, font_color='black', font_size=15, verticalalignment="center", horizontalalignment="center")

        plt.show()



def make_network(xml_string):
    xml_string = xml_string.replace("\n", "").replace("\t", "").replace("  ", "").strip()
    network = Graph(xml_string)
    return network