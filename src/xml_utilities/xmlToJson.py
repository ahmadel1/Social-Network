import xml.etree.ElementTree as ET
import json


def xml_to_json(root_element):
    result = {}
    for child in root_element:
        child_data = None
        # child_data can be a dictionary or a string
        if len(child) > 0:
            child_data = xml_to_json(child)
        else:
            child_data = child.text.replace("\n", "").replace("\t", "").strip()

        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data

    return result


def create_json_string(xml_string):
    root_element = ET.fromstring(xml_string)
    json_dict = xml_to_json(root_element)
    return json.dumps(json_dict, indent=2)


def create_json_file(file_path, data):
    file_path = file_path + "/sample-json.json"
    with open(file_path, "w") as json_file:
        json_file.write(data)
    json_file.close()


def get_xml_string(file_path):
    with open(file_path, "r") as xml_file:
        xml_string = xml_file.read()
    xml_file.close()
    return xml_string


### test ###

xml_string = get_xml_string("src/xml_utilities/Sample files/sample.xml")

json_string = create_json_string(xml_string)

create_json_file("src/xml_utilities/Sample files", json_string)
