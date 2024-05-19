from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
        
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(640, 480)
        self.verticalLayout_1 = QVBoxLayout(Form)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        
        # self.verticalLayout_1.addWidget(self.mplcanvas)
        self.verticalLayout_1.addWidget(self.pushButton)

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))