import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit, QLineEdit, QVBoxLayout, QSpacerItem, QSizePolicy, QHBoxLayout, QComboBox, QMenu,QWidget,QTabWidget,QPushButton
from PySide6.QtGui import QIcon, QTextCursor, QColor, QTextBlockFormat, QAction
from PySide6.QtCore import QSize
from ui_form import Ui_MainWindow
from src import xml_methods


#class OutputCapture:
    #def __init__(self, line_edit):
       # self.line_edit = line_edit

   # def write(self, text):
        # Append new text and a newline character to the existing content
        #self.line_edit.setText(self.line_edit.text() + text + '\n')

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setMinimumSize(1000, 700)

        # Set up resizable layout
        self.setup_resizable_layout()


        # Set up output capture
       # self.output_capture = OutputCapture(self.ui.lineEdit)
        #sys.stdout = self.output_capture

        # Set up icons and connect buttons to methods
        self.setup_icons()
        self.connect_buttons()
        self.ui.plainTextEdit_2.setTabStopDistance(4 * self.ui.plainTextEdit_2.fontMetrics().horizontalAdvance(' '))
        self.undo_stack = [""]
        self.redo_stack = []
        # push any change in output to undo stack
        self.ui.plainTextEdit_2.textChanged.connect(self.push_to_undo_stack)
        self.setWindowIcon(QIcon("icons/icons8-palestine-100.png"))

    def push_to_undo_stack(self):
        if self.ui.plainTextEdit_2.toPlainText() != self.undo_stack[-1]:
            self.undo_stack.append(self.ui.plainTextEdit_2.toPlainText())
            self.redo_stack = []

    
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
        buttons = [self.ui.importButton, self.ui.beautify, self.ui.fix, self.ui.json,
                   self.ui.compress, self.ui.decompress, self.ui.minify, self.ui.check]

        for button in buttons:
            h_layout.addWidget(button)
        main_layout.addLayout(h_layout)



        # Create widgets to be added to the tabs
        widget1 = QWidget()
        widget1.setLayout(main_layout)

        Widget2=QWidget()

        layout = QHBoxLayout()



        # Add horizontal spacer to the left
        layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))

        # Create a push button
        button = QPushButton('Graph Show!', self)
        button.clicked.connect(self.on_button_click)

        button.setIconSize(QSize(60,60))
        button.setIcon(QIcon("icons/icons8-graph-60.png"))

        # Add the button to the layout
        layout.addWidget(button)

        # Add horizontal spacer to the right
        layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        Widget2.setLayout(layout)




        self.tab_widget = QTabWidget()


        # Add tabs to the QTabWidget
        self.tab_widget.addTab(widget1, "part 1")
        self.tab_widget.addTab(Widget2, "part 2")



        # Set the central widget to be the QTabWidget
        self.setCentralWidget(self.tab_widget)
    def on_button_click(self):
        print("clicked")
    def setup_icons(self):
        # Set the icon for the 'Import' button
        icon_size = QSize(64, 64)
        icon_size_small = QSize(54, 54)
        icon_paths = ["icons/icons8-import-50.png", "icons/icons8-makeup-brush-50.png",
                      "icons/icons8-compress-64.png", "icons/icons8-decompress-64.png",
                      "icons/icons8-check-64.png", "icons/icons8-minimize-arrow-symbol-with-shrink-inward-function-64.png",
                      "icons/icons8-fix-48.png", "icons/icons8-json-48.png", "icons/icons8-save-64.png",
                      "icons/icons8-undo-54.png", "icons/icons8-redo-54.png"]

        buttons = [self.ui.importButton, self.ui.beautify, self.ui.compress, self.ui.decompress,
                   self.ui.check, self.ui.minify, self.ui.fix, self.ui.json, self.ui.save,
                   self.ui.undo, self.ui.redo]

        for button, icon_path in zip(buttons, icon_paths):
            button.setIcon(QIcon(icon_path))
            button.setIconSize(icon_size if button not in [self.ui.save, self.ui.undo, self.ui.redo] else icon_size_small)

    def connect_buttons(self):
        # Connect the 'Import' button to the custom method
        self.ui.importButton.clicked.connect(self.on_importButton_clicked)
        self.ui.beautify.clicked.connect(self.on_beautify_clicked)
        self.ui.fix.clicked.connect(self.on_fix_clicked)
        self.ui.json.clicked.connect(self.on_json_clicked)
        self.ui.save.clicked.connect(self.save)
        self.ui.compress.clicked.connect(self.compress)
        self.ui.decompress.clicked.connect(self.decompress)
        self.ui.minify.clicked.connect(self.on_minify_clicked)
        self.ui.check.clicked.connect(self.check)
        self.ui.undo.clicked.connect(self.undo)
        self.ui.redo.clicked.connect(self.redo)
        
        # Add a combo box to select the active text editor
        self.editor_selection = "plainTextEdit"

    def undo(self):
        if len(self.undo_stack) > 1:
            self.redo_stack.append(self.undo_stack.pop())
            self.ui.plainTextEdit_2.setPlainText(self.undo_stack[-1])
            

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.redo_stack.pop())
            self.ui.plainTextEdit_2.setPlainText(self.undo_stack[-1])

    def save_text_in_file(self):
        # Get the text from the QPlainTextEdit
        text_to_save = self.ui.plainTextEdit_2.toPlainText()

        # Get the file path using QFileDialog
        self.file_path, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'Text Files (*.xml);;All Files (*)')

        if self.file_path:
            # Save the text to the file
            with open(self.file_path, 'w') as file:
                file.write(text_to_save)
    def compress(self):
        xml_methods.compress(self.file_path, self.output_path)
        print("compress pressed")

    def decompress(self):
        xml_methods.decompress(self.file_path, self.output_path)
        print("decompress pressed")

    def on_minify_clicked(self):
        try:
            xml_content = self.ui.plainTextEdit.toPlainText()
            minified_content = xml_methods.minify_xml(xml_content)
            print(minified_content)
            self.ui.plainTextEdit_2.setPlainText(minified_content)
            print("Minify pressed")
        except Exception as e:
            print(f"Error during minification: {e}")


    def get_selected_editor(self):
        editor_name = self.editor_selection.currentText()
        return getattr(self.ui, editor_name, None)

    def get_selected_output_editor(self):
        editor_name = self.editor_selection.currentText() + "_output"
        return getattr(self.ui, editor_name, None)

    def save(self):
        self.save_text_in_file()
        print("save pressed")

    def check(self):
        self.output_path = self.ui.lineEdit_2.text()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit.clear()
        xml_methods.check_xml(self.file_path, self.output_path)
        print("on check pressed")

    def open_python_file(self):
        try:
            with open(self.output_path, 'r+') as file:
                content = file.read()
                selected_editor = self.get_selected_editor()
                if selected_editor:
                    selected_editor.setPlainText(content)
        except FileNotFoundError:
            print(f"File not found: {self.output_path}")
        except Exception as e:
            print(f"Error reading file: {e}")

    def on_fix_clicked(self):
        xml_methods.fix_xml(self.file_path, self.output_path)
        self.open_python_file()

    def on_beautify_clicked(self):
        try:
            xml_content = self.ui.plainTextEdit.toPlainText()
            beautified_content = xml_methods.beautify_xml(xml_content)
            print(beautified_content)
            self.ui.plainTextEdit_2.setPlainText(beautified_content)
            print("Beautify pressed")
        except Exception as e:
            print(f"Error during beautification: {e}")

    def on_json_clicked(self):
        try:
            xml_content = self.ui.plainTextEdit.toPlainText()
            json_content = xml_methods.xml_to_json(xml_content)
            print(json_content)
            self.ui.plainTextEdit_2.setPlainText(json_content)
            print("JSON Conversion pressed")
        except Exception as e:
            print(f"Error during JSON conversion: {e}")

    def on_importButton_clicked(self):
        file_dialog = QFileDialog(self)
        self.file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.xml)")
        if self.file_path:
            print(f"Selected file: {self.file_path}")

            with open(self.file_path, 'r') as file:
                file_content = file.read()

            selected_editor = self.editor_selection
            if selected_editor:
                self.ui.plainTextEdit.setPlainText(file_content)
                self.focus_on_line(40)

    def focus_on_line(self, line_number):
        cursor = self.ui.plainTextEdit.textCursor()
        cursor.movePosition(QTextCursor.Start)

        # Move the cursor to the beginning of the specified line
        for _ in range(line_number-1):
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
        self.ui.plainTextEdit.setReadOnly(False)


def read():
    return widget.ui.lineEdit_2.text()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
