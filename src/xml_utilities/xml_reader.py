from collections import *
import re

file = open("sample.xml")
file = file.read()
file = file.replace(">",">\n")
file = file.replace("<","\n<")
     
lines = re.split("\n",file)
lines = [line.strip() for line in lines]
lines = list(filter(lambda x:x != "",lines))
print(lines)

lines_copy = lines.copy()
open_tags = list()
closing_tags = list()
lines_dict={}
number_of_line = 0
stack = []
req_tag = ""
prev_line="<"
last_tag = 0
unmatchingTags = []

for line in lines:
    line = line.strip()
    print(line)
    number_of_line+=1
    if(len(stack)): req_tag = stack[-1]
    # print(req_tag)
    if(line[0] == "<" and line[1] != "/" and line[-1] == ">"):
        if(prev_line[0] != "<"):
            lines.insert(number_of_line-1,"</"+stack.pop()+">")
            # print(line)
        else:
            stack.append(line[1:-1])
            open_tags.append(line[1:-1])
            lines_dict[line[1:-1]] = number_of_line
        last_tag = number_of_line
    elif(line[0] == "<" and line[1] == "/" and line[-1] == ">"):
        if(line[2:-1] == req_tag):
            stack.pop()
        else:
            if(line[2:-1] not in stack):
                print("Unmatching tags at:",last_tag)
                unmatchingTags.append((last_tag,number_of_line))
                lines[last_tag-1] = "#"+lines[last_tag-1]
                lines[number_of_line-1] = "#"+lines[number_of_line-1]
                # lines.insert(last_tag,"<"+line[2:-1]+">")
                stack.pop()
            else: 
                lines.insert(number_of_line-1,"</"+stack.pop()+">")
                # print("l",line)
        closing_tags.append(line[2:-1]) 
        last_tag = number_of_line
    prev_line = line


if(len(stack) and lines[-1] != stack[-1]):
    l = len(stack)
    for i in range(l):
        lines.append("</"+stack.pop()+">")
elif(len(stack) == 0):
    print("All good")

print(lines)
print(len(lines))
print(unmatchingTags)

new = open("output.xml","w")
wstack = []
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
    new.write("\n")
    
##############################################

# print(open_tags)
# print(closing_tags)
# print(len(closing_tags))

# for tag in closing_tags:
#     print(tag)
#     open_tags.remove(tag)

# print(open_tags)
# print(closing_tags)

# print(lines_dict)

# for i in open_tags:
#     print(i,lines_dict.get(i))















# stack = deque()
# estack= deque()
# # print(lines)

# for line in lines:
#     if(line[0] == "<" and line[1] != "/" and line[-1] == ">"):
#         stack.append(line[1:-1])
#     elif(line[0] == "<" and line[1] == "/" and line[-1] == ">" and
#     len(list(stack)) and line[2:line.index(">")] == list(stack)[-1]):
#         stack.pop() 

#     print(stack)

# print(stack)
# print(list(stack)[-1])
# print(line)
# print(line[2:line.index(">")])
# print(line[2:line.index(">")] == list(stack)[-1])
# print(stack) 