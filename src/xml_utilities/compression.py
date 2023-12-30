import os
import pickle

project_directory = os.path.dirname(os.path.abspath(__file__))
input_file = f"{project_directory}/Sample files/sample.xml"
output_file = f"{project_directory}/Sample files/sample-compressed-lzw.pkl"
decompressed_file = f"{project_directory}/Sample files/sample-decompressed-lzw.xml"

TERMINAL = True  

def get_file_size(file_path):
    file_size_bytes = os.path.getsize(file_path)
    file_size_kb = file_size_bytes / 1024
    file_size_mb = file_size_kb / 1024  
    return f"File Size: {file_size_bytes} bytes, ({file_size_kb:.2f}) KB"


def compress(input_file, output_file):
    with open(input_file, 'r') as f:
        original_data = f.read()

    dictionary = {chr(i): i for i in range(256)}
    current_code = 256
    max_code_size = 12 
    compressed_data = []
    buffer = ""

    for symbol in original_data:
        buffer_symbol = buffer + symbol
        if buffer_symbol in dictionary:
            buffer = buffer_symbol
        else:
            compressed_data.append(dictionary[buffer])
            if current_code < 2**max_code_size:
                dictionary[buffer_symbol] = current_code
                current_code += 1
            buffer = symbol

    compressed_data.append(dictionary[buffer])

    with open(output_file, 'wb') as f:
        pickle.dump((compressed_data, max_code_size), f)

    output_message = f"input size: {get_file_size(input_file)}\n output size: {get_file_size(output_file)}"
    return output_message
    


def decompress(input_file, output_file):
    with open(input_file, 'rb') as f:
        compressed_data, max_code_size = pickle.load(f)

    dictionary = {i: chr(i) for i in range(256)}
    current_code = 256
    buffer = chr(compressed_data[0])
    decompressed_data = buffer

    for code in compressed_data[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == current_code:
            entry = buffer + buffer[0]
        else:
            entry = buffer + buffer[0]
            if current_code < 2**max_code_size:
                dictionary[current_code] = entry
                current_code += 1

        decompressed_data += entry
        if current_code < 2**max_code_size:
            dictionary[current_code] = buffer + entry[0]
            current_code += 1
        buffer = entry

    with open(output_file, 'w') as f:
        f.write(decompressed_data)

    output_message = f"input size: {get_file_size(input_file)} bytes\n output size: {get_file_size(output_file)} bytes"
    return output_message


