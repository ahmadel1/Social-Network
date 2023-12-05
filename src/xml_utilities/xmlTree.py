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
