# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit,QLineEdit,QVBoxLayout,QHBoxLayout
from PySide6.QtGui import QIcon, QTextCursor, QTextCharFormat,QColor, QTextBlockFormat,QPalette
from PySide6.QtCore import QSize,QTimer
from ui_form import Ui_MainWindow

from src import xml_methods

class OutputCapture:
    def __init__(self, line_edit):
        self.line_edit = line_edit

    def write(self, text):
        # Append new text and a newline character to the existing content
        self.line_edit.setText(self.line_edit.text() + text + '\n')
class MainWindow(QMainWindow):
    file_path="import_path"
    output_path = ""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(1000,700)
        self.setup_resizable_layout()

        self.output_capture = OutputCapture(self.ui.lineEdit)
        sys.stdout = self.output_capture


        #self.resize(600,800)

        # Set the icon for the 'Import' button
        icon = QIcon("icons/icons8-import-50.png")
        icon_size = QSize(64, 64)
        icon_size_small=QSize(54,54)
        self.ui.importButton.setIcon(icon)
        self.ui.importButton.setIconSize(icon_size)
        self.ui.beautify.setIcon(QIcon("icons/icons8-makeup-brush-50.png"))
        self.ui.compress.setIcon(icon)
        self.ui.compress.setIconSize(icon_size)
        self.ui.compress.setIcon(QIcon("icons/icons8-compress-64.png"))

        self.ui.decompress.setIcon(icon)
        self.ui.decompress.setIconSize(icon_size)
        self.ui.decompress.setIcon(QIcon("icons/icons8-decompress-64.png"))

        self.ui.check.setIcon(icon)
        self.ui.check.setIconSize(icon_size)
        self.ui.check.setIcon(QIcon("icons/icons8-check-64.png"))

        self.ui.minify.setIcon(icon)
        self.ui.minify.setIconSize(icon_size)
        self.ui.minify.setIcon(QIcon("icons/icons8-minimize-arrow-symbol-with-shrink-inward-function-64.png"))

        self.ui.beautify.setIconSize(icon_size)
        self.ui.fix.setIcon(QIcon("icons/icons8-fix-48.png"))
        self.ui.fix.setIconSize(icon_size)
        self.ui.json.setIcon(QIcon("icons/icons8-json-48.png"))
        self.ui.json.setIconSize(icon_size)

        self.ui.save.setIconSize(icon_size_small)
        self.ui.save.setIcon(QIcon("icons/icons8-save-64.png"))

        self.ui.undo.setIconSize(icon_size_small)
        self.ui.undo.setIcon(QIcon("icons/icons8-undo-54.png"))

        self.ui.redo.setIconSize(icon_size_small)
        self.ui.redo.setIcon(QIcon("icons/icons8-redo-54.png"))


        # Connect the 'Import' button to the custom method
        self.ui.importButton.clicked.connect(self.on_importButton_clicked)
        self.ui.beautify.clicked.connect(self.on_beautify_clicked)
        self.ui.fix.clicked.connect(self.on_fix_clicked)
        self.ui.json.clicked.connect(self.on_json_clicked)

        self.ui.save.clicked.connect(self.save)

        self.ui.compress.clicked.connect(self.compress)
        self.ui.decompress.clicked.connect(self.decompress)
        self.ui.minify.clicked.connect(self.minify)
        self.ui.check.clicked.connect(self.check)
    def setup_resizable_layout(self):
            # Add a layout to the central widget for resizable behavior
            central_widget = self.centralWidget()
            main_layout = QVBoxLayout(central_widget)
            main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins to allow resizing from all edges

            # Create a vertical layout for plainTextEdit, plainTextEdit_2, and vertical layout with buttons
            v_layout = QHBoxLayout()

            v_layout.addWidget(self.ui.plainTextEdit)


            # Create a vertical layout for undo, save, redo buttons
            undo_save_redo_layout = QVBoxLayout()
            undo_save_redo_layout.addWidget(self.ui.undo)
            undo_save_redo_layout.addWidget(self.ui.save)
            undo_save_redo_layout.addWidget(self.ui.redo)

            # Add the vertical layout with undo, save, redo to the main vertical layout
            v_layout.addLayout(undo_save_redo_layout)
            v_layout.addWidget(self.ui.plainTextEdit_2)


            # Add the vertical layout to the main layout
            main_layout.addLayout(v_layout)

            # Create a horizontal layout for the remaining buttons
            h_layout = QHBoxLayout()

            # Add the remaining buttons to the horizontal layout
            h_layout.addWidget(self.ui.importButton)
            h_layout.addWidget(self.ui.beautify)
            h_layout.addWidget(self.ui.fix)
            h_layout.addWidget(self.ui.json)
            h_layout.addWidget(self.ui.compress)
            h_layout.addWidget(self.ui.decompress)
            h_layout.addWidget(self.ui.minify)
            h_layout.addWidget(self.ui.check)
            main_layout.addWidget(self.ui.lineEdit)
            main_layout.addWidget(self.ui.lineEdit_2)
            main_layout.addLayout(h_layout)
    def save_text_in_file(self):
                # Get the text from the QPlainTextEdit
                text_to_save = self.ui.plainTextEdit.toPlainText()

                # Get the file path using QFileDialog
                self.file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.xml);;All Files (*)')

                if self.file_path:
                    # Save the text to the file
                    with open(self.file_path, 'w') as file:
                        file.write(text_to_save)

    def compress(self):
        self.output_path=self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        xml_methods.compress(self.file_path,self.output_path)
        print("compress pressed")
    def decompress(self):
        self.output_path=self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        xml_methods.decompress(self.file_path,self.output_path)
        print("decompress pressed")
    def minify(self):
        self.output_path=self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        xml_methods.minify_xml(self.file_path,self.output_path)
        print("minify pressed")
    def save(self):
        self.save_text_in_file()

        print("save pressed")
    def check(self):
        self.output_path=self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        xml_methods.check_xml(self.file_path,self.output_path)
        print("on check pressed")

    def open_python_file(self):
             # Assume output_path is the path to the file
             # Read the content of the Python file and display it in the QPlainTextEdit
        try:
            with open(self.output_path, 'r+') as file:
                content = file.read()
                self.ui.plainTextEdit_2.setPlainText(content)
        except FileNotFoundError:
                print(f"File not found: {self.output_path}")
        except Exception as e:
                print(f"Error reading file: {e}")
    def on_fix_clicked(self):
        self.output_path=self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        xml_methods.fix_xml(self.file_path,self.output_path)
        self.open_python_file()


    def on_beautify_clicked(self):
        self.output_path=self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()

        xml_methods.beautify_xml(self.file_path,self.output_path)
        self.open_python_file()

    def on_json_clicked(self):
        self.output_path=self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.clear()
        xml_methods.xml_to_json(self.file_path,self.output_path)
        self.open_python_file()




    def on_importButton_clicked(self):
        file_dialog = QFileDialog(self)
        self.file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.xml)")
        self.output_path=self.ui.lineEdit_2.text()

        if self.file_path:
            print(f"Selected file: {self.file_path}")

            with open(self.file_path, 'r') as file:
                file_content = file.read()

            self.ui.plainTextEdit.setPlainText(file_content)
            self.focus_on_line(40)

    def focus_on_line(self, line_number):

                cursor = self.ui.plainTextEdit.textCursor()
                cursor.movePosition(QTextCursor.Start)

                # Move the cursor to the beginning of the specified line
                for _ in range(line_number-1 ):
                    cursor.movePosition(QTextCursor.NextBlock)




                self.ui.plainTextEdit.setTextCursor(cursor)

                # Clear any previous selections
                self.ui.plainTextEdit.setExtraSelections([])

                # Create a QTextEdit.ExtraSelection to highlight the line
                selection = QTextEdit.ExtraSelection()
                selection.format.setBackground(QColor(255, 0, 0))  # Set a red background color
                selection.format.setProperty(QTextBlockFormat.FullWidthSelection, True)
                selection.cursor = self.ui.plainTextEdit.textCursor()
                selection.cursor.clearSelection()

                # Add the selection to the QTextEdit
                self.ui.plainTextEdit.setExtraSelections([selection])
                self.ui.plainTextEdit.setReadOnly(True)

def read():
    return widget.ui.lineEdit_2.text()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    #delay_function()
    print("write output path")
   # delay_function()
    #widget.output_path=widget.ui.lineEdit_2.text()
    sys.exit(app.exec())
