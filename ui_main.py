# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainkwXiLM.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSlider, QStackedWidget, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(1246, 831)
        self.gridLayout = QGridLayout(main)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lb_Header = QLabel(main)
        self.lb_Header.setObjectName(u"lb_Header")
        font = QFont()
        font.setPointSize(20)
        self.lb_Header.setFont(font)

        self.gridLayout.addWidget(self.lb_Header, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_start = QWidget()
        self.pg_start.setObjectName(u"pg_start")
        self.label = QLabel(self.pg_start)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 140, 131, 81))
        self.pushButton = QPushButton(self.pg_start)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(430, 460, 211, 51))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton.setFont(font1)
        self.stackedWidget.addWidget(self.pg_start)
        self.pg_questions = QWidget()
        self.pg_questions.setObjectName(u"pg_questions")
        self.horizontalSlider = QSlider(self.pg_questions)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(140, 510, 881, 22))
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(5)
        self.horizontalSlider.setPageStep(5)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.stackedWidget.addWidget(self.pg_questions)
        self.pg_stats = QWidget()
        self.pg_stats.setObjectName(u"pg_stats")
        self.stackedWidget.addWidget(self.pg_stats)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)


        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"Form", None))
        self.lb_Header.setText(QCoreApplication.translate("main", u"Big Five Inventory 2 (BFI-2)", None))
        self.label.setText(QCoreApplication.translate("main", u"Info Box !!!", None))
        self.pushButton.setText(QCoreApplication.translate("main", u"starte Fragebogen", None))
    # retranslateUi

