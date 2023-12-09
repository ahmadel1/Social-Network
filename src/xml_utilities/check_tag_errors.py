from collections import *
import re

def check_for_errors(filename):
    file = open(filename)
    lines = file.readlines()
    tags = []
    for line in lines:
        line = line.replace(">",">\n")
        line = line.replace("<","\n<")
        tags = tags + re.findall("<.*>",line)
        
    not_closed = []
    not_opened = []

    tag_num = {}
    tag_count = {}
    last_4_tag = {}

    for tag in tags:
        if(tag_num.get(tag) == None or tag_num.get(tag) == []):
            if(last_4_tag.get(tag) == None):
                tag_num[tag] = [1]
                last_4_tag[tag] = 1
            else:
                tag_num[tag] = [last_4_tag[tag]+1]
                last_4_tag[tag] = last_4_tag[tag]+1
        else:
            tag_num[tag].append(last_4_tag[tag]+1)
            last_4_tag[tag] = tag_num.get(tag)[-1]
            
        if(tag[0:2] == "</"):
            if(tag[2:-1] in not_closed):
                not_closed.remove(tag[2:-1])
                last_4_tag[tag] = tag_num[tag].pop()
                new_tag = tag.replace("/","")
                last_4_tag[new_tag] = tag_num[new_tag].pop()
            else:
                not_opened.append(tag[2:-1])
        else:
            not_closed.append(tag[1:-1])


    # print(tags)
    # print(not_closed)
    # print(not_opened)
    # print(tag_num)
    errors = {}

    for n in range(len(lines)):
        for tag in tag_num.keys():
            found = re.findall(tag,lines[n])
            if(found):
                if(tag_count.get(tag) == None):
                    tag_count[tag] = 1
                else:
                    tag_count[tag] = tag_count.get(tag) + 1
                
                if(tag_num.get(tag) == []):
                    continue
                elif(tag_count[tag] == tag_num.get(tag)[0]):
                    tag_num.get(tag).pop(0)
                    # print(found,n+1)
                    if(errors.get(n+1) == None):
                        errors[n+1] = []
                    errors[n+1].extend(found)
                    # if(found[0][1] != "/"):
                    #     print("At line:",n+1,found[0],"Not closed")
                    # else:
                    #     print("At line:",n+1,found[0],"Not opened")

    return (errors)

a = []

for i in check_for_errors("sample.xml").items():
    a.extend([tag + f" is not opened at line " + str(i[0]) if tag[1] == "/" else tag + f" is not closed at line " + str(i[0]) for tag in i[1]])
    
for i in a:
    print(i)