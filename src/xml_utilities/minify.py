def minify(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.readlines()
        
    for i in range(len(content)):
        content[i] = content[i].strip()
    content = ''.join(content)
    
    with open(output_file, 'w') as f:
        f.write(content)

