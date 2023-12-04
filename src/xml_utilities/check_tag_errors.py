from collections import *
import re

file = open("readme.xml")
lines = file.readlines()
tags = []
for line in lines:
    line = line.replace(">",">\n")
    line = line.replace("<","\n<")
    tags = tags + re.findall("<.*>",line)
    
not_closed = []
not_opened = []

for tag in tags:
    if(tag[0:2] == "</"):
        if(tag[2:-1] in not_closed):
            not_closed.remove(tag[2:-1])
        else:
            not_opened.append(tag[2:-1])
    else:
        not_closed.append(tag[1:-1])


# print(tags)
# print(not_closed)
# print(not_opened)

for x in range(len(lines)):
    line = lines[x]
    for tag in not_closed:
        if("<"+tag+">" in line):
            print("At Line:" + str(x+1),"Tag:",tag,"is not closed.")
            not_closed.remove(tag)
            break
print("\n") 
for x in range(len(lines)):
    line = lines[x]
    for tag in not_opened:
        if("</"+tag+">" in line):
            print("At Line:" + str(x+1),"Tag:",tag,"is not opened.")
            not_opened.remove(tag)
            break




