import xml.etree.ElementTree as ET
import json
from xmlTree import *


def xml_to_json(root_element):
    result = {}
    for child in root_element:
        child_data = None
        # child_data can be a dictionary or a string
        if len(child) > 0:
            child_data = xml_to_json(child)
        else:
            child_data = child.text.replace("\n", "").replace("\t", "").strip()

        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data

    return result


def create_json_string(xml_string):
    root_element = ET.fromstring(xml_string)
    json_dict = xml_to_json(root_element)
    return json.dumps(json_dict, indent=2)


def create_json_file(file_path, data):
    file_path = file_path + "/sample-json.json"
    with open(file_path, "w") as json_file:
        json_file.write(data)
    json_file.close()


def get_xml_string(file_path):
    with open(file_path, "r") as xml_file:
        xml_string = xml_file.read()
    xml_file.close()
    return xml_string


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
    xml_tree.root = xml_tree.root.children[0]
    return xml_tree


### test ###

xml_string = get_xml_string("src/xml_utilities/Sample files/sample.xml")

# json_string = create_json_string(xml_string)

# create_json_file("src/xml_utilities/Sample files", json_string)

xml_string = xml_string.replace("\n", "").replace("\t", "").replace("  ", "").strip()

xml_tree = create_tree(xml_string)

print(xml_tree.root.children[0].children[2].children[0].children[1].children[1].text)
