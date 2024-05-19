# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SensorDataPlotUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(803, 417)
        Form.setMinimumSize(QSize(0, 20))
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.pushButton)

        self.btnUpdate = QPushButton(Form)
        self.btnUpdate.setObjectName(u"btnUpdate")
        self.btnUpdate.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btnUpdate)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u62c9\u53d6\u6578\u64da", None))
        self.btnUpdate.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u66f2\u7dda\u5716", None))
    # retranslateUi

