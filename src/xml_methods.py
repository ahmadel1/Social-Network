from .xml_utilities.xmlToJson import *
from .xml_utilities.fix_and_prettify import *
from .xml_utilities.compression import *
from .xml_utilities.check_tag_errors import *
from .xml_utilities.minify import *



def xml_to_json(input_path, output_path):
    try:
        convert_xml_to_json(input_path, output_path)
        print(f"Conversion successful. JSON data written to {output_path}")
    except Exception as e:
        print(f"Error converting XML to JSON: {e}")

def beautify_xml(input_path, output_path):
    try:
        beautify(input_path, output_path)
        print(f"Beautification successful. Beautified XML written to {output_path}")
    except Exception as e:
        print(f"Error beautifying XML: {e}")

def fix_xml(input_path, output_path):
    try:
        fix(input_path, output_path)
        print(f"Fixing successful. Fixed XML written to {output_path}")
    except Exception as e:
        print(f"Error fixing XML: {e}")

def compress_xml(input_path, output_path):
    try:
        compress(input_path, output_path)
        print(f"Compression successful. Compressed XML written to {output_path}")
    except Exception as e:
        print(f"Error compressing XML: {e}")

def decompress_xml(input_path, output_path):
    try:
        decompress(input_path, output_path)
        print(f"Decompression successful. Decompressed XML written to {output_path}")
    except Exception as e:
        print(f"Error decompressing XML: {e}")

def check_xml(input_path, output_path):
    pass

def minify_xml(input_path, output_path):
    minify(input_path, output_path)

