from collections import *
import re
from PySide6.QtCore import QTimer
from ui_form import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon

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

def beautify(xml_content, lines = False):
    if not lines:
        lines = seperate(xml_content)
    else:
        lines = lines


    beautified_content = ""
    skip_loops, indentations = 0, ""
    
    for i in range(len(lines)):
        if skip_loops != 0:
            skip_loops -= 1
            continue
        
        line = lines[i]
        
        if line[0] == "<" and line[1] != "/" and line[-1] == ">":
            if len(lines[i + 1]) <= 4 and lines[i + 1][0] != "<":
                beautified_content += "".join([indentations, lines[i], lines[i + 1], lines[i + 2]])
                skip_loops = 2
            else:
                beautified_content += "".join([indentations, line])
                indentations += '\t'
        elif line[0] == "<" and line[1] == "/" and line[-1] == ">":
            indentations = indentations.replace('\t', "", 1)
            beautified_content += "".join([indentations, line])
        else:
            beautified_content += "".join([indentations, line])
        
        beautified_content += "\n"
    
    return beautified_content


def some_function_that_needs_delay(time):
            # Start the timer with a delay of 2000 milliseconds (2 seconds)
    QTimer.singleShot(time,delayed_code)

def delayed_code():
            # This function will be called after the specified delay
    print("Delayed code executed")
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
                print(f"Conflict between tags at line: {binary_search(ind,end_lines,0,len(end_lines)-1)+2}")
                print(tag,next_tag)
                print("Choose One:")
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Conflict Resolve")
                msg_box.setText(f"Conflict between tags at line: {binary_search(ind,end_lines,0,len(end_lines)-1)+2}\nChoose a variable")
                
                yes_button = msg_box.addButton(tag, QMessageBox.ButtonRole.YesRole)
                no_button = msg_box.addButton(next_tag, QMessageBox.ButtonRole.NoRole)
                msg_box.exec()
                choose = "None"

                if msg_box.clickedButton() == yes_button:
                    print("User chose Tag")
                    if tag[1] == "/":
                        choose = tag[2:-1]
                    else:
                        choose = tag[1:-1]
                elif msg_box.clickedButton() == no_button:
                    print("User chose Next Tag")
                    if next_tag[1] == "/":
                        choose = next_tag[2:-1]
                    else:
                        choose = next_tag[1:-1]

                conflict_fixes.append(choose)
        else:
            ind = file_content.index(tag)
            file_content = list(file_content)
            file_content[ind] = "$"
            file_content = "".join(file_content)
    return conflict_fixes
    

def fix(xml_content):
    file = xml_content
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

    return beautify("",lines)

