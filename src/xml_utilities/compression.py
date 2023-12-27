import os
import pickle
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox

project_directory = os.path.dirname(os.path.abspath(__file__))
app = QApplication([])

def get_file_size(file_path):
    file_size_bytes = os.path.getsize(file_path)
    file_size_kb = file_size_bytes / 1024
    file_size_mb = file_size_kb / 1024
    size_str = f"{file_size_bytes} bytes ({file_size_kb:.2f} KB)"
    return size_str


def show_popup(title, message):
    app = QApplication([])
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    msg_box.exec_()


def get_file_path(title):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    file_path, _ = QFileDialog.getOpenFileName(None, title, "", "All Files (*);;XML Files (*.xml);;Pickle Files (*.pkl)", options=options)
    return file_path


def save_file_path(title):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    file_path, _ = QFileDialog.getSaveFileName(None, title, "", "All Files (*);;XML Files (*.xml);;Pickle Files (*.pkl)", options=options)
    return file_path


def compress():
    input_file = get_file_path("Select Input File")
    output_file = save_file_path("give Name of Output File") + ".pkl"

    if input_file and output_file:
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
                if current_code < 2 ** max_code_size:
                    dictionary[buffer_symbol] = current_code
                    current_code += 1
                buffer = symbol

        compressed_data.append(dictionary[buffer])

        with open(output_file, 'wb') as f:
            pickle.dump((compressed_data, max_code_size), f)

        original_size = f"Original file Size: {get_file_size(input_file)}"
        compressed_size = f"Compressed file Size: {get_file_size(output_file)}"
        show_popup("Compression Successful", f"{original_size}\n{compressed_size}")


def decompress():
    input_file = get_file_path("Select Input File")
    output_file = save_file_path("give Name of Output File") + ".xml"

    if input_file and output_file:
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
                if current_code < 2 ** max_code_size:
                    dictionary[current_code] = entry
                    current_code += 1

            decompressed_data += entry
            if current_code < 2 ** max_code_size:
                dictionary[current_code] = buffer + entry[0]
                current_code += 1
            buffer = entry

        with open(output_file, 'w') as f:
            f.write(decompressed_data)

        original_size = f"Original file Size: {get_file_size(input_file)}"
        compressed_size = f"Decompressed file Size: {get_file_size(output_file)}"
        show_popup("Decompression Successful", f"{original_size}\n{compressed_size}")


