# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainrvpJdh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1028, 360)
        MainWindow.setWindowIcon(QIcon('X:/Python practice/ArtPublish/resouce/icon.png'))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"#centralwidget {	\n"
                                        "	background-color: #181818;\n"
                                        "}\n"
                                        "\n"
                                        "#widget {\n"
                                        "    border-radius: 25px;\n"
                                        "    background-color: #555555;\n"
                                        "}\n"
                                        "\n"
                                        "#widget_2 {\n"
                                        "    border-radius: 25px;\n"
                                        "    background-color: #555555;\n"
                                        "}\n"
                                        "\n"
                                        "#widget_3 {\n"
                                        "    border-radius: 25px;\n"
                                        "    background-color: #555555;\n"
                                        "}\n"
                                        "\n"
                                        "#widget_4 {\n"
                                        "    border-radius: 25px;\n"
                                        "    background-color: #555555;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton { 	\n"
                                        "    font-size: 25px;\n"
                                        "    border-radius: 20px;\n"
                                        "    padding: 10px;\n"
                                        "    font-weight: bold;\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:pressed {\n"
                                        "    font-size: 50px;\n"
                                        "    border-color:red;\n"
                                        "}\n"
                                        "\n"
                                        "#assetButton {      \n"
                                        "	background-image: url(X:/Python practice/ArtPublish/resouce/key visual.jpg);\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "	\n"
                                        "}\n"
                                        "\n"
                                        "#assetButton:hover {        \n"
                                        "	border-image: url(X:/Python practice/ArtPublish/resouce/key visual_.jpg);\n"
                                        "   \n"
                                        "}\n"
                                        "\n"
                                        "#shotButton {    \n"
                                        "	background-image: url(X:/Python practice/ArtPublish/resouce/Matte Painter.jpg);\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "	\n"
                                        "}\n"
                                        "\n"
                                        "#shotButton:hover {       \n"
                                        "	border-image: url(X:/Python practice/ArtPublish/resouce"
                                                                "/Matte Painter_.jpg);\n"
                                        "}\n"
                                        "\n"
                                        "#layoutButton {    \n"
                                        "	background-image: url(X:/Python practice/ArtPublish/resouce/color script.jpg);\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "	\n"
                                        "}\n"
                                        "\n"
                                        "#layoutButton:hover {    \n"
                                        "    border-image: url(X:/Python practice/ArtPublish/resouce/color script_.jpg);\n"
                                        "}\n"
                                        "\n"
                                        "#compButton {   \n"
                                        "	background-image: url(X:/Python practice/ArtPublish/resouce/ui_ghapic mattepaint.jpg);\n"
                                        "	color: rgb(255, 255, 255);\n"
                                        "	\n"
                                        "}\n"
                                        "\n"
                                        "#compButton:hover {    \n"
                                        "    border-image: url(X:/Python practice/ArtPublish/resouce/ui_ghapic mattepaint_.jpg);\n"
                                        "}\n"
                                        "\n"
                                        "#programName {\n"
                                        "    font-size: 30px;\n"
                                        "	color: rgb(252, 252, 252);\n"
                                        "}\n"
                                        "\n"
                                        "#label {\n"
                                        "   font-size: 17px;\n"
                                        "   color: rgb(252, 252, 252);\n"
                                        "}\n"
                                        "\n"
                                        "#label_4 {\n"
                                        "   font-size: 17px;\n"
                                        "   color: rgb(252, 252, 252);\n"
                                        "}\n"
                                        "\n"
                                        "#label_2 {\n"
                                        "   font-size: 17px;\n"
                                        "   color: rgb(252, 252, 252);\n"
                                        "}\n"
                                        "\n"
                                        "#label_5 {\n"
                                        "   font-size: 17px;\n"
                                        "   color: rgb(252, 252, 252);\n"
                                        "}\n"
                                        "")
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_8 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.programName = QLabel(self.centralwidget)
        self.programName.setObjectName(u"programName")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.programName.sizePolicy().hasHeightForWidth())
        self.programName.setSizePolicy(sizePolicy)
        self.programName.setMinimumSize(QSize(0, 60))
        self.programName.setMaximumSize(QSize(16777215, 16777215))
        self.programName.setSizeIncrement(QSize(0, 0))
        self.programName.setBaseSize(QSize(0, 0))
        self.programName.setMouseTracking(False)
        self.programName.setTextFormat(Qt.PlainText)
        self.programName.setMargin(5)

        self.verticalLayout_8.addWidget(self.programName, 0, Qt.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(25, -1, 25, 20)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(0, 0))
        self.widget.setBaseSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 0)
        self.assetButton = QPushButton(self.widget)
        self.assetButton.setObjectName(u"assetButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.assetButton.sizePolicy().hasHeightForWidth())
        self.assetButton.setSizePolicy(sizePolicy1)
        self.assetButton.setStyleSheet(u"")
        self.assetButton.setIconSize(QSize(200, 200))
        self.assetButton.setFlat(False)

        self.verticalLayout.addWidget(self.assetButton)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 50))
        self.verticalLayout.addWidget(self.label, 0, Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.widget)
        
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setMinimumSize(QSize(0, 0))
        self.widget_2.setBaseSize(QSize(0, 0))
        
        
        
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 0)
        
        # Create a QGraphicsDropShadowEffect instance
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)  # Adjust the blur radius as needed
        shadow.setColor("#000000")  # Set the shadow color
        shadow.setOffset(3, 3)  # Set the offset of the shadow
 
        self.shotButton = QPushButton(self.widget_2)
        self.shotButton.setObjectName(u"shotButton")
        sizePolicy1.setHeightForWidth(self.shotButton.sizePolicy().hasHeightForWidth())
        self.shotButton.setSizePolicy(sizePolicy1)
        self.shotButton.setIconSize(QSize(200, 200))
        self.shotButton.setFlat(False)
        

        self.verticalLayout_3.addWidget(self.shotButton)

        self.label_4 = QLabel(self.widget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 50))
        self.label_4.setGraphicsEffect(shadow)

        self.verticalLayout_3.addWidget(self.label_4, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QSize(0, 0))
        self.widget_3.setBaseSize(QSize(0, 0))
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 0)
        self.layoutButton = QPushButton(self.widget_3)
        self.layoutButton.setObjectName(u"layoutButton")
        sizePolicy1.setHeightForWidth(self.layoutButton.sizePolicy().hasHeightForWidth())
        self.layoutButton.setSizePolicy(sizePolicy1)
        self.layoutButton.setIconSize(QSize(200, 200))
        self.layoutButton.setFlat(False)

        self.verticalLayout_4.addWidget(self.layoutButton)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 50))

        self.verticalLayout_4.addWidget(self.label_2, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.centralwidget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setMinimumSize(QSize(0, 0))
        self.widget_4.setBaseSize(QSize(0, 0))
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 10, 10, 0)
        self.compButton = QPushButton(self.widget_4)
        self.compButton.setObjectName(u"compButton")
        sizePolicy1.setHeightForWidth(self.compButton.sizePolicy().hasHeightForWidth())
        self.compButton.setSizePolicy(sizePolicy1)
        self.compButton.setIconSize(QSize(200, 200))
        self.compButton.setFlat(False)

        self.verticalLayout_5.addWidget(self.compButton)

        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.label_5, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget_4)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Art Publish", None))
        self.programName.setText(QCoreApplication.translate("MainWindow", u"ART PUBLISH", None))
        self.assetButton.setText(QCoreApplication.translate("MainWindow", u"ASSET", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Design Key visual", None))
        self.shotButton.setText(QCoreApplication.translate("MainWindow", u"SHOT", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Mattepaint", None))
        self.layoutButton.setText(QCoreApplication.translate("MainWindow", u"LAYOUT", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Colorscript", None))
        self.compButton.setText(QCoreApplication.translate("MainWindow", u"COMP", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"UI/Ghaphic mattepaint", None))
    # retranslateUi

