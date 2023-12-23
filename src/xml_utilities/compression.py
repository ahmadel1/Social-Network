import os

MIN_WORD_SIZE = 5 #compress words larger than this word size
MIN_WORD_FREQ = 2 # compress words repeater more than this
TERMINAL = True # false to disable printing in termainal 


project_directory = os.path.dirname(os.path.abspath(__file__))

input_file = f"{project_directory}/Sample files/sample.xml"
output_file = f"{project_directory}/Sample files/sample-compressed.xml"
decompressed_file = f"{project_directory}/Sample files/sample-decompressed.xml"


def get_file_size(file_path):
    file_size_bytes = os.path.getsize(file_path)
    file_size_kb = file_size_bytes / 1024
    file_size_mb = file_size_kb / 1024
    if TERMINAL:
        print(f"File Size: {file_size_bytes} bytes ({file_size_kb:.2f} KB or {file_size_mb:.2f} MB)")


def compress(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    word_frequency = {}
    for line in lines:
        words = line.strip().split(" ")
        for word in set(words):
            word_frequency[word] = word_frequency.get(word, 0) + 1


    word_symbol = {}
    symbol = 0
    for word, frequency in word_frequency.items():
        if frequency >= MIN_WORD_FREQ and len(word) >= MIN_WORD_SIZE:
            word_symbol[word] = f'#{symbol}!'
            symbol += 1

    file = ''.join(lines)
    for word, symbol in word_symbol.items():
        file = file.replace(word, symbol)

    with open(output_file, 'w') as f:
        f.write(file)
        # Add mapping information to the end of the output file
        f.write('\n<!START_DICTIONARY!>\n')
        for word, symbol in word_symbol.items():
            f.write(f"{word}\n")

    if TERMINAL:
        print("Input file Size:", get_file_size(input_file))
        print("Output file Size:", get_file_size(output_file))



def decompress(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    start_dict_index = lines.index('<!START_DICTIONARY!>\n') + 1
    compressed_lines = lines[:start_dict_index-1]
    dictionary_lines = lines[start_dict_index:]

    word_symbol = {}
    for i, line in enumerate(dictionary_lines):
        word_symbol[line.strip()] = f'#{i}!'
    symbol_set = set(word_symbol.values())

    for i in range(len(compressed_lines)):
        line = compressed_lines[i]
        for word, symbol in word_symbol.items():
            line = line.replace(symbol, word)
        compressed_lines[i] = line


    decompressed_content = ''.join(compressed_lines)

    with open(output_file, 'w') as f:
        f.write(decompressed_content)

    if TERMINAL:
        print("Input file Size:", get_file_size(input_file))
        print("Output file Size:", get_file_size(output_file))

if __name__ == "__main__":
    compress(input_file, output_file)
    decompress(output_file, decompressed_file)




##  for minifying 
# def compress_spaces(line):
#     indent_count = len(line) - len(line.lstrip())
#     return '\t' * (indent_count // 4) + line.lstrip()
# lines = [compress_spaces(line) for line in lines]
