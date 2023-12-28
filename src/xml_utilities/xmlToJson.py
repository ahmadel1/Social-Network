import json
from .xmlTree import *
from ..graph_utilities.creator import *


def xml_to_json(root_element):
    result = {}
    for child in root_element.children:
        child_data = None
        # child_data can be a dictionary or a string
        if len(child.children) > 0:
            # in case the child has children, call the function recursively
            child_data = xml_to_json(child)
        else:
            child_data = child.text

        if child.tag in result:
            if isinstance(result[child.tag], list):
                # if the child tag already exists in the result dictionary, append the child data to the list if it exists
                result[child.tag].append(child_data)
            else:
                # if it not a list, convert it to a list and append the child data
                result[child.tag] = [result[child.tag], child_data]
        else:
            # if the child is a leaf node, add it to the result dictionary directly
            result[child.tag] = child_data

    return result


def create_json_string(xml_string):
    # create a tree from the xml string
    xml_tree = create_tree(xml_string)
    # convert the tree to a dictionary
    json_dict = xml_to_json(xml_tree.root)
    return json.dumps(json_dict, indent=2)


def create_json_file(file_path, data):
    with open(file_path, "w") as json_file:
        json_file.write(data)
    json_file.close()


def get_xml_string(xml_string):
    return xml_string.replace("\n", "").replace("\t", "").replace("  ", "").strip()


def create_tree(xml_string):
    xml_tree = XmlTree()
    tag_buffer = ""
    value_buffer = ""
    stack = [xml_tree.root]
    last_node = None
    current_node = None
    i = 0

    while i < len(xml_string):
        # check if the current character is an opening tag
        if xml_string[i] == "<" and xml_string[i + 1] != "/":
            # make a new childe node
            ### get the last node from the stack
            last_node = stack[-1]
            current_node = Node()
            xml_tree.add_node(last_node, current_node)

            # reset buffers
            tag_buffer = ""
            i = i + 1  # skip the "<" character

            # get the tag name
            while xml_string[i] != ">":
                tag_buffer = tag_buffer + xml_string[i]
                i = i + 1
            current_node.tag = tag_buffer
            ###push the current node to the stack
            stack.append(current_node)
        # check if the current character is a closing tag
        elif xml_string[i] == "<" and xml_string[i + 1] == "/":
            # save the value of the current node
            current_node.text = value_buffer

            # reset buffers
            tag_buffer = ""
            value_buffer = ""
            i = i + 2  # skip the "</" characters

            # get the tag name
            while xml_string[i] != ">":
                tag_buffer = tag_buffer + xml_string[i]
                i = i + 1

            # check if the tag name matches the current node's tag
            if tag_buffer == current_node.tag:
                current_node = current_node.parent
                ### pop the current node from the stack
                stack.pop()
        else:
            value_buffer = value_buffer + xml_string[i]

        i = i + 1
    return xml_tree


def get_users_array(json_dict):
    # array of (User) objects
    users_array = []

    # array of (JSON) objects
    json_users = json_dict["users"]["user"]

    # iterate through json_users
    for json_user in json_users:
        user_creator = UserCreator(json_user)
        users_array.append(user_creator.create_object())

    # adjust (following) array for each user after creating all users
    for user in users_array:
        user.setFollowingArray(users_array)

    return users_array


def convert_xml_to_json(xml_content):
    xml_string = get_xml_string(xml_content)
    json_string = create_json_string(xml_string)
    return json_string


def get_xml_string_fromPath(file_path):
    with open(file_path, "r") as xml_file:
        xml_string = xml_file.read()
    xml_file.close()
    # remove all the new lines, tabs and spaces from the xml string
    return xml_string.replace("\n", "").replace("\t", "").replace("  ", "").strip()
### test ###

# xml_string = get_xml_string("src/xml_utilities/Sample files/sample.xml")
# # create a tree from the xml string
# xml_tree = create_tree(xml_string)
# # convert the tree to a dictionary
# json_dict = xml_to_json(xml_tree.root)
# # create user array form  (JSON) object
# users = get_users_array(json_dict)
