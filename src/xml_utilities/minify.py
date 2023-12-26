def minify(xml_content):
    xml_content = xml_content.split('\n')
    for i in range(len(xml_content)):
        xml_content[i] = xml_content[i].strip()
    xml_content = ''.join(xml_content)
    
    return xml_content

