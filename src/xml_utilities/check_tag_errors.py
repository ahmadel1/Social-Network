import re

def check_for_errors(xml_content):
    lines = xml_content
    copy = lines
    lines = lines.split("\n")
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
            if(tag[2:-1] not in stack):
                copy = copy.replace(tag,"<#"+tag[2:-1]+"#>",1)
            elif(tag[2:-1] in  stack):
                required_tag = stack.pop(stack.index(tag[2:-1]))
                if(stack.count(required_tag) >= 1):
                    copy = copy.replace("<"+required_tag+">","<%"+required_tag+">",stack.count(required_tag)+1)
                    copy = copy.replace("<%"+required_tag+">","<"+required_tag+">",stack.count(required_tag))
                else:
                    copy = copy.replace("<"+required_tag+">","*",1)
                copy = copy.replace(tag,"*",1)
        i = i +1

    
    copy_lines = copy.split("\n")
    errors = []
    
    for c in range(len(copy_lines)):
        line = copy_lines[c]
        for tag in re.findall("<[0-9A-Za-z#]*>",line):
            errors.append(c+1)
    return errors
