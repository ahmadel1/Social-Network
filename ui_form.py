# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QMainWindow,
    QPlainTextEdit, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1348, 788)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(140, -40, 1221, 631))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.plainTextEdit = QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setTabChangesFocus(False)
        self.plainTextEdit.setTabStopDistance(40.000000000000000)

        self.horizontalLayout_2.addWidget(self.plainTextEdit)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.undo = QPushButton(self.verticalLayoutWidget)
        self.undo.setObjectName(u"undo")

        self.verticalLayout_2.addWidget(self.undo)

        self.save = QPushButton(self.verticalLayoutWidget)
        self.save.setObjectName(u"save")

        self.verticalLayout_2.addWidget(self.save)

        self.redo = QPushButton(self.verticalLayoutWidget)
        self.redo.setObjectName(u"redo")

        self.verticalLayout_2.addWidget(self.redo)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.plainTextEdit_2 = QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setTabStopDistance(40.000000000000000)

        self.horizontalLayout_2.addWidget(self.plainTextEdit_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.importButton = QPushButton(self.verticalLayoutWidget)
        self.importButton.setObjectName(u"importButton")

        self.horizontalLayout.addWidget(self.importButton)

        self.beautify = QPushButton(self.verticalLayoutWidget)
        self.beautify.setObjectName(u"beautify")

        self.horizontalLayout.addWidget(self.beautify)

        self.json = QPushButton(self.verticalLayoutWidget)
        self.json.setObjectName(u"json")

        self.horizontalLayout.addWidget(self.json)

        self.fix = QPushButton(self.verticalLayoutWidget)
        self.fix.setObjectName(u"fix")

        self.horizontalLayout.addWidget(self.fix)

        self.compress = QPushButton(self.verticalLayoutWidget)
        self.compress.setObjectName(u"compress")

        self.horizontalLayout.addWidget(self.compress)

        self.decompress = QPushButton(self.verticalLayoutWidget)
        self.decompress.setObjectName(u"decompress")

        self.horizontalLayout.addWidget(self.decompress)

        self.minify = QPushButton(self.verticalLayoutWidget)
        self.minify.setObjectName(u"minify")

        self.horizontalLayout.addWidget(self.minify)

        self.check = QPushButton(self.verticalLayoutWidget)
        self.check.setObjectName(u"check")

        self.horizontalLayout.addWidget(self.check)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.undo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.redo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.importButton.setText(QCoreApplication.translate("MainWindow", u" Import", None))
        self.beautify.setText(QCoreApplication.translate("MainWindow", u"   Beautify", None))
        self.json.setText(QCoreApplication.translate("MainWindow", u" Json", None))
        self.fix.setText(QCoreApplication.translate("MainWindow", u" Fix", None))
        self.compress.setText(QCoreApplication.translate("MainWindow", u" Compress", None))
        self.decompress.setText(QCoreApplication.translate("MainWindow", u" Decompress", None))
        self.minify.setText(QCoreApplication.translate("MainWindow", u" Minify", None))
        self.check.setText(QCoreApplication.translate("MainWindow", u" Check", None))
    # retranslateUi

