class Node:
    tag = ""
    text = ""
    parent = None
    children = None

    def __init__(self, tag=""):
        self.tag = tag
        self.children = list()


class XmlTree:
    root = None

    def __init__(self, tag=""):
        self.root = Node(tag)

    def add_node(self, parent, child):
        child.parent = parent
        parent.children.append(child)

    def print_tree(self, node=None):
        if node is None:
            node = self.root

        print(node.tag + " ")
        if node.text != "":
            print("(" + node.text + ") ")

        for child in node.children:
            self.print_tree(child)

