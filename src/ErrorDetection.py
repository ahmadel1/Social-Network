import xml.etree.ElementTree as ET

def parse_and_check_errors(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        print("XML file is well-formed.")
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return

    stack = []

    for event, element in ET.iterparse(xml_file, events=('start', 'end')):
        if event == 'start':
            stack.append(element.tag)
        elif event == 'end':
            if not stack:
                print(f"Error: Closing tag '{element.tag}' without corresponding opening tag.")
            elif stack[-1] != element.tag:
                print(f"Error: Mismatched tag '{element.tag}' (expected '{stack[-1]}').")
            else:
                stack.pop()

    if stack:
        print(f"Error: Unclosed tag(s): {', '.join(stack)}")
    
    print("The File Is Without Any Errors")

if __name__ == "__main__":
    xml_file_path = "sample.xml"  # Replace with the path to your XML file
    parse_and_check_errors(xml_file_path)
