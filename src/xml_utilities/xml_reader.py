import re

'''
class Node:
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.parents = [parent]
        self.children = []
        if(parent != None):
            parent.add_child(self)
    def add_parent(self,parent):
        self.parents.append(parent)
        parent.add_child(self)
    def get_parent(self):
        if(len(self.parents) == 1):
            return self.parent
        else:
            return self.parents
    def add_child(self,child):
        self.children.append(child)
    def add_children(self,children:list):
        self.children = self.children + children
    def get_child(self,index):
        return self.children[index]
    def get_children(self,i=0):
        children_to_return = []
        while(i < len(self.children)):
            children_to_return.append(self.get_child(i))
            i+=1
        return children_to_return
    def get_siblings(self):
        parent = self.get_parent()
        siblings = list()
        if(type(self.get_parent()) == Node):
            siblings.append(parent.get_children())
        else:
            pass
        return siblings
    
# def get_node_bydata(root:Node,data):
#     if(root.data == data):
#         return root
#     for child in root.get_children():
#         return get_node_bydata(child,data)

def get_children(root:Node,list=[],i=0):
    if(i == len(root.get_children())):
        return list
    list.append(root.get_child(i).data)
    i+=1
    return get_children(root,list,i)
        


users = Node("users",None)
user = Node("user",users)
id = Node("id",user)
name = Node("name",user)
posts = Node("posts",user)
followers = Node("followers",user)
post = Node("post",posts)
body = Node("body",post)
topics = Node("topics",post)
topic = Node("topic",topics)
follower = Node("follower",followers)
id.add_parent(follower)

# print(get_node_bydata(users,"followers").get_parent().data)
# # print(id_.parent.data)
# # print(type(users))
# id_node = get_node_bydata(user,"id")
# # print(id.get_parent())
# # print(get_node_bydata(users,"id"))
# # print(id_node.get_parent().data)

'''

# l = get_children(follower)
# # print(get_node_bydata(users,"id").get_parent())
# print((name.get_siblings())[0][0].data)
# # print(user.children[0].data)
# # print(users.get_children()[0].data)





def get_parent(data):
    for tag in xml_structure.keys():
        if(data in xml_structure.get(tag)):
            return tag


file = open("sample.xml")
file = file.read()
file = file.replace(">",">\n")
file = file.replace("<","\n<")
     
lines = re.split("\n",file)
lines = [line.strip() for line in lines]
lines = list(filter(lambda x:x != "",lines))
# print(lines)

xml_structure = {
    "users":["user"],
    "user":["id","name","posts","followers"],
    "posts":["post"],
    "post":["body","topics"],
    "topics":["topic"],
    "followers":["follower"],
    "follower":["id"],
    "id":[],
    "name":[],
    "body":[],
    "topic":[]
}

# print(get_parent("id"))

def get_children(tag,children=[]):
    if(tag == ""):
        return
    for child in xml_structure.get(tag):
        children.append(child)
        get_children(child)
    return children
    
# print("children_function",get_children("post"))

stack = []
parent = ""
current_tag = ""
ln = 0
fix = []
fix_index = []
skip = 0
last = ""
s = 0

for n in range(len(lines)):
    line = lines[n]
    if(len(parent) and len(stack)):
        print("stack:",stack[-1])
        # print("fix:",fix[-1])
        print("parent:",parent)
        print("line:",line)
    ln+=1
    if(line[0] == "<" and line[1] != "/" and line[-1] == ">"):
        # If tag name isn't expected 
        if(parent != "" and get_parent(line[1:-1]) == get_parent(parent)):
            lines.insert(ln-1,"</"+stack.pop()+">")
            parent = stack[-1]
            continue
        if(line[1:-1] == parent):
            lines.insert(ln-1,"</"+parent+">")
            stack.pop()
            parent = stack[-1]
            continue
        
        if(parent in xml_structure.keys() and line[1:-1] not in xml_structure.get(parent)):
            if(len(xml_structure.get(parent)) == 0):
                lines.insert(ln-1,"</"+parent+">")
                stack.pop()
                parent = stack[-1]
                continue
            else:
                print("tag " + line[1:-1] + " isn't a child of " + parent,end=" ")
                print(",line:",ln)
                print("Which one did you mean:[",end="")
                for child in xml_structure.get(parent):
                    print(child,end=" ")
                print("\b]?")
                chosen = input()
                #Change tag:
                if(len(xml_structure.get(parent)) > 0):
                    lines[ln-1] = lines[ln-1].replace(line[1:-1],chosen)
                    print("replaced",line[1:-1])
                    stack.append(chosen)
                    # print("stack:",stack[-1])
                    last = "open"
                    parent = chosen
                    print("_____________")
                    continue
        stack.append(line[1:-1])
        parent = stack[-1]
                
    elif(line[0:2] == "</" and line[-1] == ">"):
        if(line[2:-1] == stack[-1]):
            stack.pop()
        elif(line[2:-1] not in stack):
            line = line.replace(line," ")
        else:
            lines.insert(ln-1,"</"+stack.pop()+">")
    if(len(stack)):
        parent = stack[-1]
    else:
        parent = ""
    print("_____________")
    
    





print(lines)

new = open("output.xml","w")
wstack = []
ut1 = -1
ut2 = -1
unmatching_tags = []
skip_loops = 0
ind = "\t"
indentations = ""

for i in range(len(lines)):
    if(skip_loops != 0):
        skip_loops -= 1
        continue
    line = lines[i]
    if(line[0] == "<" and line[1] != "/" and line[-1] == ">"):
        if(len(lines[i+1]) <= 4 and lines[i+1][0] != "<"):
            new.write(indentations)
            new.write(line)
            new.write(lines[i+1])
            new.write(lines[i+2])
            skip_loops=2
        else:
            new.write(indentations)
            new.write(line)
            indentations+=ind
    elif(line[0] == "<" and line[1] == "/" and line[-1] == ">"):
        indentations = indentations.replace(ind,"",1)
        new.write(indentations)
        new.write(line)
    else:
        new.write(indentations)
        new.write(line)
    # if(line[0] == "#" and ut1 == -1):
    #     ut1 = i
    # elif(line[0] == "#" and ut1 != -1):
    #     ut2 = i
    #     unmatching_tags.append((ut1,ut2))
    #     ut1 = -1
    #     ut2 = -1
    new.write("\n")
