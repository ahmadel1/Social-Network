import json
from xmlTree import *

def same(root):
    # if(root.tag[-1] == "s"):
    #     return 1
    # else:
    #     return 0
    if(len(root.children) == 1 and root.tag == root.children[0].tag+"s"):
        return 1
    children = []
    for child in root.children:   
        if(child.tag in children):
            return 1
        else:
            children.append(child.tag)
    return 0

def xml_to_json(root_element):
    if(same(root_element)):
        res = []
        for child in root_element.children:
            res.append(xml_to_json(child))
        return res
    elif(len(root_element.children) > 0):
        res = {}
        for child in root_element.children:
            res[child.tag] = xml_to_json(child)
        return res
    elif(len(root_element.children) == 0):
        return root_element.text

def create_json_string(xml_string):
    # create a tree from the xml string
    xml_tree = create_tree(xml_string)
    # convert the tree to a dictionary
    print(xml_tree.root.children[0].tag)
    total_res = []
    json_dict = xml_to_json(xml_tree.root)
    print("json:",json_dict)
    return json.dumps(json_dict, indent=2)


def create_json_file(file_path, data):
    file_path = file_path + "sample-json.json"
    with open(file_path, "w") as json_file:
        json_file.write(data)
    json_file.close()


def get_xml_string(file_path):
    with open(file_path, "r") as xml_file:
        xml_string = xml_file.read()
    xml_file.close()
    # remove all the new lines, tabs and spaces from the xml string
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


### test ###

xml_string = get_xml_string("../xml_part/sample.xml")

json_string = create_json_string(xml_string)

create_json_file("", json_string)
