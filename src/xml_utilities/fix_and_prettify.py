from collections import *
import re


def binary_search(num,list:list,s,e):
    mid = int((s+e)/2)
    if(list[mid] == num):
        return mid
    if(s >= e):
        return mid-1
    if(num <= list[mid]):
        return binary_search(num,list,s,mid)
    else:
        return binary_search(num,list,mid+1,e) 


def fix_and_prettify(filename,output_path):
    file = open(filename)
    file = file.read()
    file2 = file
    file2 = file2.replace(" ","")
    end_lines = [i for i in range(len(file2)) if file2[i] == "\n"]
    tags = re.findall("<[a-z]*>|</[a-z]*>",file2)
    # print(re.findall("<[a-z]*>|</[a-z]*>",file2))
    conflict_fixes = []

    for i in range(len(re.findall("<[a-z]*>|</[a-z]*>",file2))):
        if(i == len(tags)-1):
            continue
        tag = tags[i]
        next_tag = tags[i+1]
        if(tag[0] == "<" and tag[1] != "/" and next_tag[0:2] == "</"):
            if(tag[1:-1] == next_tag[2:-1]):
                # print(tag,next_tag)
                ind = file2.index(tag)
                file2 = list(file2)
                file2[ind] = "$"
                file2 = "".join(file2)
                # print(file2.index(tag))
            else:
                ind = file2.index(tag)
                print("Conflict between tags at line:",binary_search(ind,end_lines,0,len(end_lines)-1)+2)
                print(tag,next_tag)
                choose = input("Choose One:")
                conflict_fixes.append(choose)
                # print(file2.index(tag))
                # print(file2[file2.index(tag)])
        else:
            ind = file2.index(tag)
            file2 = list(file2)
            file2[ind] = "$"
            file2 = "".join(file2)

    file = file.replace(">",">\n")
    file = file.replace("<","\n<")
        
    lines = re.split("\n",file)
    lines = [line.strip() for line in lines]
    lines = list(filter(lambda x:x != "",lines))
    lines_copy = lines.copy()
    open_tags = list()
    closing_tags = list()
    lines_dict={}
    number_of_line = 0
    stack = []
    req_tag = ""
    prev_line="<"
    last_tag = 0
    last_tag_type = ""
    skip = 0
    flag = 0
    x_line = 0
    num_inserts = 0
    d = 0

    for line in lines:
        line = line.strip()
        if(skip):
            skip = 0
            number_of_line+=1
            last_tag = number_of_line
            continue
        number_of_line+=1
        if(len(stack)):
            req_tag = stack[-1]
        if(line[0] == "<" and line[1] != "/" and line[-1] == ">"):
            if(prev_line[0] != "<"):
                lines.insert(number_of_line-1,"</"+stack.pop()+">")
            else:
                stack.append(line[1:-1])
                open_tags.append(line[1:-1])
                lines_dict[line[1:-1]] = number_of_line
            last_tag = number_of_line
            last_tag_type = "o"
        elif(line[0] == "<" and line[1] == "/" and line[-1] == ">"):
            if(line[2:-1] == req_tag):
                stack.pop()
            else:
                if(line[2:-1] not in stack):
                    if(last_tag_type == "o"):
                        chosen = conflict_fixes.pop(0)
                        lines[last_tag-1] = "<"+chosen+">"
                        lines[number_of_line-1] = "</"+chosen+">"
                        stack.pop()
                    elif(last_tag_type == "c"):
                        lines.insert(last_tag,"<"+line[2:-1]+">")
                        skip = 1
                else: 
                    lines.insert(number_of_line-1,"</"+stack.pop()+">")
                    # print("l",line)
            closing_tags.append(line[2:-1]) 
            last_tag = number_of_line
            last_tag_type = "c"
        prev_line = line

    if(len(stack) and lines[-1] != stack[-1]):
        l = len(stack)
        for i in range(l):
            lines.append("</"+stack.pop()+">")
    elif(len(stack) == 0):
        print("All good")

    # output_file_path = "output.xml"
    new = open(output_path,"w")
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
        new.write("\n")
    
    return output_path