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


def open_file(input_path):
    try:
        with open(input_path, 'r+') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{input_path}' not found.")
        return
    except Exception as e:
        print(f"Error: Unable to read the file '{input_path}'.")
        return

def seperate(file):
        file = file.replace(">",">\n").replace("<","\n<") 
        lines = re.split("\n",file)
        lines = [line.strip() for line in lines]
        lines = list(filter(lambda x:x != "",lines))
        return lines

def beautify(input_path, output_path, lines = None):
    if input_path == None:
        lines = lines
    else: 
        file = open_file(input_path)
        lines = seperate(file)

    output_file = open(output_path,"w")
    skip_loops, indentations = 0, ""
    for i in range(len(lines)):
        if(skip_loops != 0):
            skip_loops -= 1
            continue
        line = lines[i]
        if(line[0] == "<" and line[1] != "/" and line[-1] == ">"):
            if(len(lines[i+1]) <= 4 and lines[i+1][0] != "<"):
                output_file.write("".join([indentations, lines[i], lines[i+1], lines[i+2]]))
                skip_loops=2
            else:
                output_file.write("".join([indentations, line]))
                indentations+='\t'
        elif(line[0] == "<" and line[1] == "/" and line[-1] == ">"):
            indentations = indentations.replace('\t',"",1)
            output_file.write("".join([indentations, line]))
        else:
            output_file.write("".join([indentations, line]))
        output_file.write("\n")
               
    output_file.close()



def get_conflicts(file):
    file_content = file.replace(" ","")
    end_lines = [i for i in range(len(file_content)) if file_content[i] == "\n"]
    tags = re.findall("<[a-z]*>|</[a-z]*>",file_content)
    conflict_fixes = []
    for i in range(len(tags)-1):
        tag = tags[i]
        next_tag = tags[i+1]
        if tag[0] == "<" and tag[1] != "/" and next_tag[0:2] == "</":
            if tag[1:-1] == next_tag[2:-1]:
                ind = file_content.index(tag)
                file_content = list(file_content)
                file_content[ind] = "$"
                file_content = "".join(file_content)
            else:
                ind = file_content.index(tag)
                print("Conflict between tags at line:",binary_search(ind,end_lines,0,len(end_lines)-1)+2)
                print(tag,next_tag)
                choose = input("Choose One:")
                conflict_fixes.append(choose)
        else:
            ind = file_content.index(tag)
            file_content = list(file_content)
            file_content[ind] = "$"
            file_content = "".join(file_content)
    return conflict_fixes
    

def fix(input_path, output_path):
    file = open_file(input_path)
    conflict_fixes = get_conflicts(file) 
    lines = seperate(file)

    open_tags, closing_tags, lines_dict, stack = list(), list(), {}, []
    number_of_line, last_tag, skip  = 0, 0, 0
    req_tag, prev_line, last_tag_type = "" , "<", ""

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

    beautify(input_path=None, output_path=output_path, lines = lines)
    return output_path


