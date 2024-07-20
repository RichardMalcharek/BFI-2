# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainzMKuhb.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QStackedWidget, QWidget)

class Ui_frm_main(object):
    def setupUi(self, frm_main):
        if not frm_main.objectName():
            frm_main.setObjectName(u"frm_main")
        frm_main.setEnabled(True)
        frm_main.resize(1000, 650)
        frm_main.setMinimumSize(QSize(1000, 650))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        frm_main.setFont(font)
        self.centralwidget = QWidget(frm_main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_start = QWidget()
        self.pg_start.setObjectName(u"pg_start")
        self.gridLayout_4 = QGridLayout(self.pg_start)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.btn_start = QPushButton(self.pg_start)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QSize(250, 50))
        self.btn_start.setMaximumSize(QSize(250, 50))

        self.gridLayout_4.addWidget(self.btn_start, 0, 0, 1, 1)

        self.lb_empty = QLabel(self.pg_start)
        self.lb_empty.setObjectName(u"lb_empty")

        self.gridLayout_4.addWidget(self.lb_empty, 0, 1, 1, 1)

        self.lb_txt = QLabel(self.pg_start)
        self.lb_txt.setObjectName(u"lb_txt")
        self.lb_txt.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lb_txt.setWordWrap(True)

        self.gridLayout_4.addWidget(self.lb_txt, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.pg_start)
        self.pg_inv = QWidget()
        self.pg_inv.setObjectName(u"pg_inv")
        self.gridLayout_10 = QGridLayout(self.pg_inv)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.lb_empty_3 = QLabel(self.pg_inv)
        self.lb_empty_3.setObjectName(u"lb_empty_3")

        self.gridLayout_10.addWidget(self.lb_empty_3, 1, 4, 12, 1)

        self.slct_a4 = QRadioButton(self.pg_inv)
        self.slct_a4.setObjectName(u"slct_a4")
        sizePolicy.setHeightForWidth(self.slct_a4.sizePolicy().hasHeightForWidth())
        self.slct_a4.setSizePolicy(sizePolicy)
        self.slct_a4.setMinimumSize(QSize(350, 20))
        self.slct_a4.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_10.addWidget(self.slct_a4, 6, 1, 1, 1)

        self.slct_a3 = QRadioButton(self.pg_inv)
        self.slct_a3.setObjectName(u"slct_a3")
        sizePolicy.setHeightForWidth(self.slct_a3.sizePolicy().hasHeightForWidth())
        self.slct_a3.setSizePolicy(sizePolicy)
        self.slct_a3.setMinimumSize(QSize(350, 20))
        self.slct_a3.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_10.addWidget(self.slct_a3, 5, 1, 1, 1)

        self.lb_question = QLabel(self.pg_inv)
        self.lb_question.setObjectName(u"lb_question")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lb_question.sizePolicy().hasHeightForWidth())
        self.lb_question.setSizePolicy(sizePolicy1)
        self.lb_question.setMinimumSize(QSize(700, 100))
        self.lb_question.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.lb_question.setWordWrap(True)

        self.gridLayout_10.addWidget(self.lb_question, 1, 0, 1, 2)

        self.prog_bar = QProgressBar(self.pg_inv)
        self.prog_bar.setObjectName(u"prog_bar")
        self.prog_bar.setEnabled(True)
        sizePolicy.setHeightForWidth(self.prog_bar.sizePolicy().hasHeightForWidth())
        self.prog_bar.setSizePolicy(sizePolicy)
        self.prog_bar.setMinimumSize(QSize(400, 50))
        self.prog_bar.setMaximumSize(QSize(400, 50))
        self.prog_bar.setSizeIncrement(QSize(0, 0))
        self.prog_bar.setAutoFillBackground(False)
        self.prog_bar.setValue(24)
        self.prog_bar.setTextVisible(True)
        self.prog_bar.setInvertedAppearance(False)

        self.gridLayout_10.addWidget(self.prog_bar, 10, 1, 1, 1)

        self.lb_empty_4 = QLabel(self.pg_inv)
        self.lb_empty_4.setObjectName(u"lb_empty_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(50)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lb_empty_4.sizePolicy().hasHeightForWidth())
        self.lb_empty_4.setSizePolicy(sizePolicy2)
        self.lb_empty_4.setMinimumSize(QSize(50, 100))
        self.lb_empty_4.setMaximumSize(QSize(16777215, 100))

        self.gridLayout_10.addWidget(self.lb_empty_4, 3, 0, 5, 1)

        self.btn_next = QPushButton(self.pg_inv)
        self.btn_next.setObjectName(u"btn_next")
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        self.btn_next.setMinimumSize(QSize(250, 50))
        self.btn_next.setMaximumSize(QSize(250, 50))

        self.gridLayout_10.addWidget(self.btn_next, 8, 1, 1, 1)

        self.label_2 = QLabel(self.pg_inv)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_10.addWidget(self.label_2, 1, 3, 12, 1)

        self.slct_a5 = QRadioButton(self.pg_inv)
        self.slct_a5.setObjectName(u"slct_a5")
        sizePolicy.setHeightForWidth(self.slct_a5.sizePolicy().hasHeightForWidth())
        self.slct_a5.setSizePolicy(sizePolicy)
        self.slct_a5.setMinimumSize(QSize(350, 20))
        self.slct_a5.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_10.addWidget(self.slct_a5, 7, 1, 1, 1)

        self.slct_a1 = QRadioButton(self.pg_inv)
        self.slct_a1.setObjectName(u"slct_a1")
        sizePolicy.setHeightForWidth(self.slct_a1.sizePolicy().hasHeightForWidth())
        self.slct_a1.setSizePolicy(sizePolicy)
        self.slct_a1.setMinimumSize(QSize(350, 20))
        self.slct_a1.setMaximumSize(QSize(16777215, 20))
        self.slct_a1.setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.gridLayout_10.addWidget(self.slct_a1, 3, 1, 1, 1)

        self.btn_finish = QPushButton(self.pg_inv)
        self.btn_finish.setObjectName(u"btn_finish")
        sizePolicy.setHeightForWidth(self.btn_finish.sizePolicy().hasHeightForWidth())
        self.btn_finish.setSizePolicy(sizePolicy)
        self.btn_finish.setMinimumSize(QSize(250, 50))
        self.btn_finish.setMaximumSize(QSize(250, 50))

        self.gridLayout_10.addWidget(self.btn_finish, 9, 1, 1, 1)

        self.lb_empty_2 = QLabel(self.pg_inv)
        self.lb_empty_2.setObjectName(u"lb_empty_2")

        self.gridLayout_10.addWidget(self.lb_empty_2, 12, 1, 1, 2)

        self.slct_a2 = QRadioButton(self.pg_inv)
        self.slct_a2.setObjectName(u"slct_a2")
        sizePolicy.setHeightForWidth(self.slct_a2.sizePolicy().hasHeightForWidth())
        self.slct_a2.setSizePolicy(sizePolicy)
        self.slct_a2.setMinimumSize(QSize(350, 20))
        self.slct_a2.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_10.addWidget(self.slct_a2, 4, 1, 1, 1)

        self.lb_empty_5 = QLabel(self.pg_inv)
        self.lb_empty_5.setObjectName(u"lb_empty_5")
        sizePolicy1.setHeightForWidth(self.lb_empty_5.sizePolicy().hasHeightForWidth())
        self.lb_empty_5.setSizePolicy(sizePolicy1)

        self.gridLayout_10.addWidget(self.lb_empty_5, 2, 0, 1, 2)

        self.stackedWidget.addWidget(self.pg_inv)
        self.pg_end = QWidget()
        self.pg_end.setObjectName(u"pg_end")
        self.gridLayout_3 = QGridLayout(self.pg_end)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.grph_bar2 = QChartView(self.pg_end)
        self.grph_bar2.setObjectName(u"grph_bar2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.grph_bar2.sizePolicy().hasHeightForWidth())
        self.grph_bar2.setSizePolicy(sizePolicy3)

        self.gridLayout_3.addWidget(self.grph_bar2, 2, 0, 1, 3)

        self.grph_bar1 = QChartView(self.pg_end)
        self.grph_bar1.setObjectName(u"grph_bar1")
        sizePolicy1.setHeightForWidth(self.grph_bar1.sizePolicy().hasHeightForWidth())
        self.grph_bar1.setSizePolicy(sizePolicy1)
        self.grph_bar1.setMinimumSize(QSize(0, 250))
        self.grph_bar1.setMaximumSize(QSize(16777215, 250))
        self.grph_bar1.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

        self.gridLayout_3.addWidget(self.grph_bar1, 1, 0, 1, 3)

        self.btn_main = QPushButton(self.pg_end)
        self.btn_main.setObjectName(u"btn_main")
        sizePolicy.setHeightForWidth(self.btn_main.sizePolicy().hasHeightForWidth())
        self.btn_main.setSizePolicy(sizePolicy)
        self.btn_main.setMinimumSize(QSize(250, 50))
        self.btn_main.setMaximumSize(QSize(16777215, 50))

        self.gridLayout_3.addWidget(self.btn_main, 0, 0, 1, 1)

        self.label_4 = QLabel(self.pg_end)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 2)

        self.stackedWidget.addWidget(self.pg_end)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 1)

        frm_main.setCentralWidget(self.centralwidget)

        self.retranslateUi(frm_main)

        QMetaObject.connectSlotsByName(frm_main)
    # setupUi

    def retranslateUi(self, frm_main):
        frm_main.setWindowTitle(QCoreApplication.translate("frm_main", u"Big Five Inventory 2 (BFI-2)", None))
        self.label.setText(QCoreApplication.translate("frm_main", u"Big Five Inventory 2 (BFI-2)", None))
        self.btn_start.setText(QCoreApplication.translate("frm_main", u"Fragebogen starten", None))
        self.lb_empty.setText("")
        self.lb_txt.setText(QCoreApplication.translate("frm_main", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Arial'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Die vorliegene Python-Programmierung leitet durch die 60 Fragen der deutschen Version des Big-Five Inventory 2 und bietet am Ende eine \u00dcbersicht der errechneten Kategorisierung.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; m"
                        "argin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:700; text-decoration: underline;\">Big Five Inventory 2 (BFI-2)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:700; text-decoration: underline;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;Die deutsche Version des Big Five Inventory 2 (BFI-2) erfasst die Big Five Pers\u00f6nlichkeitseigenschaften Extraversion, Vertr\u00e4glichkeit, Gewissenhaftigkeit, Negative Emotionalit\u00e4t (fr\u00fcher: Neurotizismus) und Offenheit mit jeweils drei Facetten. Die Skala basiert auf dem Big Five Inventory 2 von Christopher "
                        "Soto und Oliver John. Die Items wurden in einem mehrstufigen Verfahren vom Englischen ins Deutsche \u00fcbertragen. Erste empirische Untersuchungen belegen die Reliabilit\u00e4t und Validit\u00e4t der Messungen.&quot;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">[Autor/in: Danner, D., Rammstedt, B., Bluemke, M., Lechner, C., Berres, S., Knopf, T., Soto, C., &amp; John, O. P.]</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://doi.org/10.6102/zis247\"><span style=\" text-decoration: underline; color:#0078d4;\">https://doi.org/10.6102/zis247</span></a></p></body></html>", None))
        self.lb_empty_3.setText("")
        self.slct_a4.setText(QCoreApplication.translate("frm_main", u"stimme eher zu", None))
        self.slct_a3.setText(QCoreApplication.translate("frm_main", u"teils, teils", None))
        self.lb_question.setText(QCoreApplication.translate("frm_main", u"Es macht mir Spass, gruendlich ueber komplexe Dinge nachzudenken und sie zu verstehen.", None))
        self.lb_empty_4.setText("")
        self.btn_next.setText(QCoreApplication.translate("frm_main", u"n\u00e4chste Frage", None))
        self.label_2.setText("")
        self.slct_a5.setText(QCoreApplication.translate("frm_main", u"stimme voll und ganz zu", None))
        self.slct_a1.setText(QCoreApplication.translate("frm_main", u"stimme \u00fcberhaupt nicht zu", None))
        self.btn_finish.setText(QCoreApplication.translate("frm_main", u"Fragebogen abschlie\u00dfen", None))
        self.lb_empty_2.setText("")
        self.slct_a2.setText(QCoreApplication.translate("frm_main", u"stimme eher nicht zu", None))
        self.lb_empty_5.setText("")
        self.btn_main.setText(QCoreApplication.translate("frm_main", u"zur\u00fcck zur Startseite", None))
        self.label_4.setText("")
    # retranslateUi

