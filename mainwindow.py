# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTextEdit
from PySide6.QtGui import QIcon, QTextCursor, QTextCharFormat,QColor, QTextBlockFormat,QPalette
from PySide6.QtCore import QSize
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Set the icon for the 'Import' button
        icon = QIcon("icons/icons8-import-50.png")
        icon_size = QSize(64, 64)
        self.ui.importButton.setIcon(icon)
        self.ui.importButton.setIconSize(icon_size)
        self.ui.beautify.setIcon(QIcon("icons/icons8-makeup-brush-50.png"))
        self.ui.beautify.setIconSize(icon_size)
        self.ui.fix.setIcon(QIcon("icons/icons8-fix-48.png"))
        self.ui.fix.setIconSize(icon_size)
        self.ui.json.setIcon(QIcon("icons/icons8-json-48.png"))
        self.ui.json.setIconSize(icon_size)

        # Connect the 'Import' button to the custom method
        self.ui.importButton.clicked.connect(self.on_importButton_clicked)
        self.ui.beautify.clicked.connect(self.on_beautify_clicked)
        self.ui.fix.clicked.connect(self.on_fix_clicked)
        self.ui.json.clicked.connect(self.on_json_clicked)

    def on_fix_clicked(self):
        self.ui.plainTextEdit.appendPlainText("fixed")


    def on_beautify_clicked(self):
        self.ui.plainTextEdit.appendPlainText("beautify")

    def on_json_clicked(self):
        self.ui.plainTextEdit.appendPlainText("json")


    def on_importButton_clicked(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")

        if file_path:
            print(f"Selected file: {file_path}")

            with open(file_path, 'r') as file:
                file_content = file.read()

            self.ui.plainTextEdit.setPlainText(file_content)
            self.ui.plainTextEdit.setReadOnly(True)
            self.focus_on_line(40)

    def focus_on_line(self, line_number):
                self.ui.plainTextEdit.setReadOnly(False)

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





if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
