from .xmlTree import *
from ..graph_utilities.creator import *
from ..graph_utilities.dictionary import *


class XmlToJsonParser:
    def __init__(self, xml_string):
        self.xml_string = xml_string
        self.xml_tree = self.create_tree()
        self.json_dict = self.create_jsonDict(self.xml_tree.root)
        self.json_str = self.create_jsonString()

    def create_tree(self):
        xml_tree = XmlTree()
        tag_buffer = ""
        value_buffer = ""
        stack = [xml_tree.root]
        last_node = None
        current_node = None
        i = 0

        while i < len(self.xml_string):
            # check if the current character is an opening tag
            if self.xml_string[i] == "<" and self.xml_string[i + 1] != "/":
                # make a new childe node
                ### get the last node from the stack
                last_node = stack[-1]
                current_node = Node()
                xml_tree.add_node(last_node, current_node)

                # reset buffers
                tag_buffer = ""
                i = i + 1  # skip the "<" character

                # get the tag name
                while self.xml_string[i] != ">":
                    tag_buffer = tag_buffer + self.xml_string[i]
                    i = i + 1
                current_node.tag = tag_buffer
                ###push the current node to the stack
                stack.append(current_node)
            # check if the current character is a closing tag
            elif self.xml_string[i] == "<" and self.xml_string[i + 1] == "/":
                # save the value of the current node
                current_node.text = value_buffer

                # reset buffers
                tag_buffer = ""
                value_buffer = ""
                i = i + 2  # skip the "</" characters

                # get the tag name
                while self.xml_string[i] != ">":
                    tag_buffer = tag_buffer + self.xml_string[i]
                    i = i + 1

                # check if the tag name matches the current node's tag
                if tag_buffer == current_node.tag:
                    current_node = current_node.parent
                    ### pop the current node from the stack
                    stack.pop()
            else:
                value_buffer = value_buffer + self.xml_string[i]

            i = i + 1

        return xml_tree

    def create_jsonDict(self, root_element):
        json_dict = Dictionary()
        for child in root_element.children:
            child_data = None
            # child_data can be a dictionary or a string
            if len(child.children) > 0:
                # in case the child has children, call the function recursively
                child_data = self.create_jsonDict(child)
            else:
                child_data = child.text

            if child.tag in json_dict:
                if isinstance(json_dict[child.tag], list):
                    # if the child tag already exists in the json_dict, append the child data to the list if it exists
                    json_dict[child.tag].append(child_data)
                else:
                    # if it not a list, convert it to a list and append the child data
                    json_dict[child.tag] = [json_dict[child.tag], child_data]
            else:
                # if the child is a leaf node, add it to the json_dict directly
                json_dict[child.tag] = child_data

        return json_dict

    def create_jsonString(self):
        json_str = self.json_dict.convert_to_str()

        return self.prettify_jsonString(json_str)

    def prettify_jsonString(self, json_str, indent=2):
        prettified_str = ""
        level = 0
        for char in json_str:
            if char == "{" or char == "[":
                level += 1
                prettified_str += char + "\n" + " " * (level * indent)
            elif char == "}" or char == "]":
                level -= 1
                prettified_str += "\n" + " " * (level * indent) + char
            elif char == ",":
                prettified_str += char + "\n" + " " * (level * indent)
            else:
                prettified_str += char

        return prettified_str

    def create_usersArray(self):
        users_array = []

        json_users = self.json_dict["users"]["user"]
        if not isinstance(json_users, list):
            json_users = [json_users]

        for json_user in json_users:
            user_creator = UserCreator(json_user)
            users_array.append(user_creator.create_object())

        for user in users_array:
            user.setFollowingArray(users_array)

        return users_array

    def get_jsonString(self):
        return self.json_str

    def get_jsonDict(self):
        return self.json_dict

    def get_usersArray(self):
        return self.create_usersArray()
