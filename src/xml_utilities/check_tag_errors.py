from collections import *
import re

def check_for_errors(filename):
    file = open(filename)
    lines = file.readlines()
    copy = lines.copy()
    copy = "".join(copy)
    print(copy)
    tags = []
    for line in lines:
        line = line.replace(">",">\n")
        line = line.replace("<","\n<")
        tags = tags + re.findall("<.*>",line)
    
    stack = []
    i = 0
    while i < len(tags):
        tag = tags[i]
        if(tag[1] != "/"):
            stack.append(tag[1:-1])
        else:
            print(tag)
            if(tag[2:-1] not in stack):
                print(tag,"not opened")
                copy = copy.replace(tag,"<#"+tag[2:-1]+"#>",1)
            elif(tag[2:-1] in  stack):
                required_tag = stack.pop(stack.index(tag[2:-1]))
                print(stack.count(required_tag))
                if(stack.count(required_tag) >= 1):
                    copy = copy.replace("<"+required_tag+">","<%"+required_tag+">",stack.count(required_tag)+1)
                    copy = copy.replace("<%"+required_tag+">","<"+required_tag+">",stack.count(required_tag))
                else:
                    copy = copy.replace("<"+required_tag+">","*",1)
                copy = copy.replace(tag,"*",1)
        i = i +1
    print(stack)

    
    copy_lines = copy.split("\n")

    errors = []
    
    for c in range(len(copy_lines)):
        line = copy_lines[c]
        for tag in re.findall("<[0-9A-Za-z#]*>",line):
            if(tag[1] == "#"):
                errors.append("</" + tag[2:-2] + "> is not opened at line " + str(c+1))
                print("</"+tag[2:-2]+"> is not opened at line",c+1)
            else:
                errors.append(tag + " is not closed at line " + str(c+1))
                print(tag,"is not closed at line",c+1)
    return errors


print(check_for_errors("sample.xml"))
