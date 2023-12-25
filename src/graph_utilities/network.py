from .User import *
from .post import *
from ..xml_utilities.xmlToJson import *





class SocialNetwork:
    def __init__(self, users):
        self.users = [None] * (len(users)+1)
        self.adjacency_list = [[] for _ in range(len(users)+1)]
        for user in users:
            self.users[int(user.id)] = user
        self.create_adjacency_list()

    def addUser(self, user):
        self.users.append(user)

    def addUsers(self, users):
        for user in users:
            user_id = int(user.id)
            if 0 <= user_id < len(self.users):
                self.users[user_id] = user
            else:
                print(f"Ignoring user {user.name} ({user.id}) as it has an invalid ID.")

    def create_adjacency_list(self):
        for user in self.users:
            if user:
                for follower in user.followers:
                    self.adjacency_list[int(user.id)].append(int(follower))

    def get_adjacency_list(self):
        return self.adjacency_list

    def displayNetwork(self):
        for user in self.users:
            if user:
                print(f"{user.name} ({user.id}) is followed by: {', '.join(user.followers)}")

    def get_mutuals(self, user1, user2):
        user1_followers = user1.getFollowers()
        user2_followers = user2.getFollowers()
        mutuals = []
        for follower in user1_followers:
            if follower in user2_followers:
                mutuals.append(self.users[int(follower)])
        return mutuals 
     

    def most_influencer(self):
        most_influencer = None
        max_followers = 0
        for user in self.users:
            if user == None:
                continue
            if max_followers < len(user.followers):
                most_influencer = user
                max_followers = len(user.followers)
        return most_influencer
    
    def most_active_user(self):
        users_degrees = [0]*len(self.adjacency_list)
        for i in range(len(self.adjacency_list)):
            if len(self.adjacency_list[i]) == 0:
                continue
            
            users_degrees[i] += len(self.adjacency_list[i])
            for j in self.adjacency_list[i]:
                users_degrees[j] += 1
        return self.users[users_degrees.index(max(users_degrees))]



# input_xml_path = "src/xml_utilities/Sample files/sample.xml"
# users = get_users_array_from_xml(input_xml_path)
# network = SocialNetwork(users)
# print(network.get_adjacency_list())
# print(network.get_mutuals(network.users[3], network.users[2]))
# print(network.most_influencer())
# print(network.most_active_user())
