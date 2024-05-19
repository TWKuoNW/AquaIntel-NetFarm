# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AquaPlayerUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AquaPlayer(object):
    def setupUi(self, AquaPlayer):
        if not AquaPlayer.objectName():
            AquaPlayer.setObjectName(u"AquaPlayer")
        AquaPlayer.resize(1251, 938)
        self.centralwidget = QWidget(AquaPlayer)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line_9 = QFrame(self.centralwidget)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_9)

        self.verticalLayout_a = QVBoxLayout()
        self.verticalLayout_a.setObjectName(u"verticalLayout_a")
        self.verticalLayout_a.setSizeConstraint(QLayout.SetMinimumSize)
        self.layout_A1 = QVBoxLayout()
        self.layout_A1.setObjectName(u"layout_A1")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labTitle = QLabel(self.centralwidget)
        self.labTitle.setObjectName(u"labTitle")
        sizePolicy.setHeightForWidth(self.labTitle.sizePolicy().hasHeightForWidth())
        self.labTitle.setSizePolicy(sizePolicy)
        self.labTitle.setMinimumSize(QSize(0, 20))
        self.labTitle.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily(u"\u5fae\u8edf\u6b63\u9ed1\u9ad4")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labTitle.setFont(font)

        self.horizontalLayout_4.addWidget(self.labTitle, 0, Qt.AlignHCenter)


        self.layout_A1.addLayout(self.horizontalLayout_4)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.layout_A1.addWidget(self.line_5)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_4)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.labNameTitle = QLabel(self.centralwidget)
        self.labNameTitle.setObjectName(u"labNameTitle")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labNameTitle.sizePolicy().hasHeightForWidth())
        self.labNameTitle.setSizePolicy(sizePolicy1)
        self.labNameTitle.setMinimumSize(QSize(0, 30))
        self.labNameTitle.setMaximumSize(QSize(16777215, 40))
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8edf\u6b63\u9ed1\u9ad4")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.labNameTitle.setFont(font1)

        self.verticalLayout_3.addWidget(self.labNameTitle)

        self.labName = QLabel(self.centralwidget)
        self.labName.setObjectName(u"labName")
        sizePolicy1.setHeightForWidth(self.labName.sizePolicy().hasHeightForWidth())
        self.labName.setSizePolicy(sizePolicy1)
        self.labName.setMinimumSize(QSize(0, 30))
        self.labName.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_3.addWidget(self.labName)


        self.horizontalLayout_16.addLayout(self.verticalLayout_3)

        self.line_7 = QFrame(self.centralwidget)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labIPTitle = QLabel(self.centralwidget)
        self.labIPTitle.setObjectName(u"labIPTitle")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.labIPTitle.sizePolicy().hasHeightForWidth())
        self.labIPTitle.setSizePolicy(sizePolicy2)
        self.labIPTitle.setMinimumSize(QSize(0, 30))
        self.labIPTitle.setMaximumSize(QSize(16777215, 40))
        self.labIPTitle.setFont(font1)

        self.verticalLayout_2.addWidget(self.labIPTitle)

        self.labIP = QLabel(self.centralwidget)
        self.labIP.setObjectName(u"labIP")
        sizePolicy2.setHeightForWidth(self.labIP.sizePolicy().hasHeightForWidth())
        self.labIP.setSizePolicy(sizePolicy2)
        self.labIP.setMinimumSize(QSize(100, 30))
        self.labIP.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_2.addWidget(self.labIP)


        self.horizontalLayout_16.addLayout(self.verticalLayout_2)

        self.line_8 = QFrame(self.centralwidget)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMinimumSize(QSize(0, 0))
        self.line_8.setFrameShape(QFrame.VLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_8)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labStatusTitle = QLabel(self.centralwidget)
        self.labStatusTitle.setObjectName(u"labStatusTitle")
        sizePolicy1.setHeightForWidth(self.labStatusTitle.sizePolicy().hasHeightForWidth())
        self.labStatusTitle.setSizePolicy(sizePolicy1)
        self.labStatusTitle.setMinimumSize(QSize(0, 30))
        self.labStatusTitle.setMaximumSize(QSize(16777215, 40))
        self.labStatusTitle.setFont(font1)

        self.verticalLayout_4.addWidget(self.labStatusTitle)

        self.labStatus = QLabel(self.centralwidget)
        self.labStatus.setObjectName(u"labStatus")
        sizePolicy1.setHeightForWidth(self.labStatus.sizePolicy().hasHeightForWidth())
        self.labStatus.setSizePolicy(sizePolicy1)
        self.labStatus.setMinimumSize(QSize(0, 30))
        self.labStatus.setMaximumSize(QSize(16777215, 40))

        self.verticalLayout_4.addWidget(self.labStatus)


        self.horizontalLayout_16.addLayout(self.verticalLayout_4)


        self.layout_A1.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.labNameKeyinTitle = QLabel(self.centralwidget)
        self.labNameKeyinTitle.setObjectName(u"labNameKeyinTitle")
        sizePolicy1.setHeightForWidth(self.labNameKeyinTitle.sizePolicy().hasHeightForWidth())
        self.labNameKeyinTitle.setSizePolicy(sizePolicy1)
        self.labNameKeyinTitle.setMinimumSize(QSize(0, 30))
        self.labNameKeyinTitle.setMaximumSize(QSize(16777215, 40))
        self.labNameKeyinTitle.setFont(font1)

        self.horizontalLayout_14.addWidget(self.labNameKeyinTitle, 0, Qt.AlignHCenter)

        self.txtName = QLineEdit(self.centralwidget)
        self.txtName.setObjectName(u"txtName")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.txtName.sizePolicy().hasHeightForWidth())
        self.txtName.setSizePolicy(sizePolicy3)
        self.txtName.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_14.addWidget(self.txtName)


        self.layout_A1.addLayout(self.horizontalLayout_14)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.labIPKeyinTitle = QLabel(self.centralwidget)
        self.labIPKeyinTitle.setObjectName(u"labIPKeyinTitle")
        sizePolicy1.setHeightForWidth(self.labIPKeyinTitle.sizePolicy().hasHeightForWidth())
        self.labIPKeyinTitle.setSizePolicy(sizePolicy1)
        self.labIPKeyinTitle.setMinimumSize(QSize(0, 30))
        self.labIPKeyinTitle.setMaximumSize(QSize(16777215, 40))
        self.labIPKeyinTitle.setFont(font1)

        self.horizontalLayout.addWidget(self.labIPKeyinTitle, 0, Qt.AlignHCenter)

        self.txtIP = QLineEdit(self.centralwidget)
        self.txtIP.setObjectName(u"txtIP")
        sizePolicy3.setHeightForWidth(self.txtIP.sizePolicy().hasHeightForWidth())
        self.txtIP.setSizePolicy(sizePolicy3)
        self.txtIP.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.txtIP)


        self.layout_A1.addLayout(self.horizontalLayout)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)

        self.btnConn = QPushButton(self.centralwidget)
        self.btnConn.setObjectName(u"btnConn")
        self.btnConn.setMinimumSize(QSize(100, 30))
        self.btnConn.setMaximumSize(QSize(16777215, 40))

        self.horizontalLayout_13.addWidget(self.btnConn)


        self.layout_A1.addLayout(self.horizontalLayout_13)


        self.verticalLayout_a.addLayout(self.layout_A1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_a.addWidget(self.line_3)

        self.layout_A2 = QVBoxLayout()
        self.layout_A2.setObjectName(u"layout_A2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.labDeviceStatus = QLabel(self.centralwidget)
        self.labDeviceStatus.setObjectName(u"labDeviceStatus")
        self.labDeviceStatus.setMinimumSize(QSize(0, 0))
        self.labDeviceStatus.setMaximumSize(QSize(16777215, 40))
        self.labDeviceStatus.setFont(font)

        self.verticalLayout.addWidget(self.labDeviceStatus, 0, Qt.AlignHCenter)


        self.layout_A2.addLayout(self.verticalLayout)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.labDev1 = QLabel(self.centralwidget)
        self.labDev1.setObjectName(u"labDev1")
        sizePolicy1.setHeightForWidth(self.labDev1.sizePolicy().hasHeightForWidth())
        self.labDev1.setSizePolicy(sizePolicy1)
        self.labDev1.setMinimumSize(QSize(100, 60))

        self.horizontalLayout_9.addWidget(self.labDev1)

        self.labDev1Status = QLabel(self.centralwidget)
        self.labDev1Status.setObjectName(u"labDev1Status")
        sizePolicy1.setHeightForWidth(self.labDev1Status.sizePolicy().hasHeightForWidth())
        self.labDev1Status.setSizePolicy(sizePolicy1)
        self.labDev1Status.setMinimumSize(QSize(40, 0))

        self.horizontalLayout_9.addWidget(self.labDev1Status)

        self.cbAutoFeeder = QCheckBox(self.centralwidget)
        self.cbAutoFeeder.setObjectName(u"cbAutoFeeder")

        self.horizontalLayout_9.addWidget(self.cbAutoFeeder)

        self.horizontalLayout_9.setStretch(0, 2)
        self.horizontalLayout_9.setStretch(1, 2)
        self.horizontalLayout_9.setStretch(2, 1)

        self.layout_A2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.labDev2 = QLabel(self.centralwidget)
        self.labDev2.setObjectName(u"labDev2")
        sizePolicy1.setHeightForWidth(self.labDev2.sizePolicy().hasHeightForWidth())
        self.labDev2.setSizePolicy(sizePolicy1)
        self.labDev2.setMinimumSize(QSize(100, 60))

        self.horizontalLayout_8.addWidget(self.labDev2)

        self.labDev2Status = QLabel(self.centralwidget)
        self.labDev2Status.setObjectName(u"labDev2Status")
        sizePolicy1.setHeightForWidth(self.labDev2Status.sizePolicy().hasHeightForWidth())
        self.labDev2Status.setSizePolicy(sizePolicy1)
        self.labDev2Status.setMinimumSize(QSize(40, 0))
        self.labDev2Status.setAutoFillBackground(False)

        self.horizontalLayout_8.addWidget(self.labDev2Status)

        self.cbProbioticSprayer = QCheckBox(self.centralwidget)
        self.cbProbioticSprayer.setObjectName(u"cbProbioticSprayer")

        self.horizontalLayout_8.addWidget(self.cbProbioticSprayer)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 2)
        self.horizontalLayout_8.setStretch(2, 1)

        self.layout_A2.addLayout(self.horizontalLayout_8)

        self.layout_A2.setStretch(1, 1)
        self.layout_A2.setStretch(2, 1)

        self.verticalLayout_a.addLayout(self.layout_A2)

        self.line_6 = QFrame(self.centralwidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_a.addWidget(self.line_6)

        self.layout_A3 = QVBoxLayout()
        self.layout_A3.setObjectName(u"layout_A3")
        self.labSensorType = QLabel(self.centralwidget)
        self.labSensorType.setObjectName(u"labSensorType")
        sizePolicy.setHeightForWidth(self.labSensorType.sizePolicy().hasHeightForWidth())
        self.labSensorType.setSizePolicy(sizePolicy)
        self.labSensorType.setMinimumSize(QSize(0, 20))
        self.labSensorType.setMaximumSize(QSize(16777215, 40))
        self.labSensorType.setFont(font)

        self.layout_A3.addWidget(self.labSensorType, 0, Qt.AlignHCenter)

        self.tempLayout = QHBoxLayout()
        self.tempLayout.setObjectName(u"tempLayout")
        self.labTemp = QLabel(self.centralwidget)
        self.labTemp.setObjectName(u"labTemp")
        sizePolicy1.setHeightForWidth(self.labTemp.sizePolicy().hasHeightForWidth())
        self.labTemp.setSizePolicy(sizePolicy1)
        self.labTemp.setMinimumSize(QSize(0, 60))

        self.tempLayout.addWidget(self.labTemp, 0, Qt.AlignVCenter)

        self.labTempValue = QLabel(self.centralwidget)
        self.labTempValue.setObjectName(u"labTempValue")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(3)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labTempValue.sizePolicy().hasHeightForWidth())
        self.labTempValue.setSizePolicy(sizePolicy4)

        self.tempLayout.addWidget(self.labTempValue)

        self.tempLayout.setStretch(0, 1)
        self.tempLayout.setStretch(1, 1)

        self.layout_A3.addLayout(self.tempLayout)

        self.humLayout = QHBoxLayout()
        self.humLayout.setObjectName(u"humLayout")
        self.labHum = QLabel(self.centralwidget)
        self.labHum.setObjectName(u"labHum")
        sizePolicy1.setHeightForWidth(self.labHum.sizePolicy().hasHeightForWidth())
        self.labHum.setSizePolicy(sizePolicy1)
        self.labHum.setMinimumSize(QSize(0, 60))

        self.humLayout.addWidget(self.labHum)

        self.labHumValue = QLabel(self.centralwidget)
        self.labHumValue.setObjectName(u"labHumValue")
        sizePolicy4.setHeightForWidth(self.labHumValue.sizePolicy().hasHeightForWidth())
        self.labHumValue.setSizePolicy(sizePolicy4)

        self.humLayout.addWidget(self.labHumValue)

        self.humLayout.setStretch(0, 1)
        self.humLayout.setStretch(1, 1)

        self.layout_A3.addLayout(self.humLayout)

        self.DOLayout = QHBoxLayout()
        self.DOLayout.setObjectName(u"DOLayout")
        self.labDO = QLabel(self.centralwidget)
        self.labDO.setObjectName(u"labDO")
        sizePolicy1.setHeightForWidth(self.labDO.sizePolicy().hasHeightForWidth())
        self.labDO.setSizePolicy(sizePolicy1)
        self.labDO.setMinimumSize(QSize(0, 60))

        self.DOLayout.addWidget(self.labDO)

        self.labDOValue = QLabel(self.centralwidget)
        self.labDOValue.setObjectName(u"labDOValue")
        sizePolicy4.setHeightForWidth(self.labDOValue.sizePolicy().hasHeightForWidth())
        self.labDOValue.setSizePolicy(sizePolicy4)

        self.DOLayout.addWidget(self.labDOValue)

        self.DOLayout.setStretch(0, 1)
        self.DOLayout.setStretch(1, 1)

        self.layout_A3.addLayout(self.DOLayout)

        self.pHLayout = QHBoxLayout()
        self.pHLayout.setObjectName(u"pHLayout")
        self.labPH = QLabel(self.centralwidget)
        self.labPH.setObjectName(u"labPH")
        sizePolicy1.setHeightForWidth(self.labPH.sizePolicy().hasHeightForWidth())
        self.labPH.setSizePolicy(sizePolicy1)
        self.labPH.setMinimumSize(QSize(0, 60))

        self.pHLayout.addWidget(self.labPH)

        self.labPHValue = QLabel(self.centralwidget)
        self.labPHValue.setObjectName(u"labPHValue")
        sizePolicy4.setHeightForWidth(self.labPHValue.sizePolicy().hasHeightForWidth())
        self.labPHValue.setSizePolicy(sizePolicy4)

        self.pHLayout.addWidget(self.labPHValue)

        self.pHLayout.setStretch(0, 1)
        self.pHLayout.setStretch(1, 1)

        self.layout_A3.addLayout(self.pHLayout)

        self.ORPLayout = QHBoxLayout()
        self.ORPLayout.setObjectName(u"ORPLayout")
        self.labORP = QLabel(self.centralwidget)
        self.labORP.setObjectName(u"labORP")
        sizePolicy1.setHeightForWidth(self.labORP.sizePolicy().hasHeightForWidth())
        self.labORP.setSizePolicy(sizePolicy1)
        self.labORP.setMinimumSize(QSize(0, 60))

        self.ORPLayout.addWidget(self.labORP)

        self.labORPValue = QLabel(self.centralwidget)
        self.labORPValue.setObjectName(u"labORPValue")
        sizePolicy4.setHeightForWidth(self.labORPValue.sizePolicy().hasHeightForWidth())
        self.labORPValue.setSizePolicy(sizePolicy4)

        self.ORPLayout.addWidget(self.labORPValue)

        self.ORPLayout.setStretch(0, 1)
        self.ORPLayout.setStretch(1, 1)

        self.layout_A3.addLayout(self.ORPLayout)


        self.verticalLayout_a.addLayout(self.layout_A3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_a)

        self.line_10 = QFrame(self.centralwidget)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.VLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_10)

        self.verticalLayout_b = QVBoxLayout()
        self.verticalLayout_b.setObjectName(u"verticalLayout_b")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.labVideo0 = QLabel(self.centralwidget)
        self.labVideo0.setObjectName(u"labVideo0")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.labVideo0.sizePolicy().hasHeightForWidth())
        self.labVideo0.setSizePolicy(sizePolicy5)
        self.labVideo0.setMinimumSize(QSize(320, 240))
        self.labVideo0.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.horizontalLayout_10.addWidget(self.labVideo0, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_b.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.cbxQuality = QComboBox(self.centralwidget)
        self.cbxQuality.addItem("")
        self.cbxQuality.addItem("")
        self.cbxQuality.addItem("")
        self.cbxQuality.addItem("")
        self.cbxQuality.setObjectName(u"cbxQuality")
        self.cbxQuality.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_15.addWidget(self.cbxQuality)

        self.btnStrVideo0 = QPushButton(self.centralwidget)
        self.btnStrVideo0.setObjectName(u"btnStrVideo0")
        self.btnStrVideo0.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_15.addWidget(self.btnStrVideo0)


        self.verticalLayout_b.addLayout(self.horizontalLayout_15)

        self.verticalLayout_b.setStretch(0, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_b)

        self.line_11 = QFrame(self.centralwidget)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShape(QFrame.VLine)
        self.line_11.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_11)

        self.verticalLayout_c = QVBoxLayout()
        self.verticalLayout_c.setObjectName(u"verticalLayout_c")
        self.labVideo1 = QLabel(self.centralwidget)
        self.labVideo1.setObjectName(u"labVideo1")
        self.labVideo1.setMinimumSize(QSize(320, 240))
        self.labVideo1.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_c.addWidget(self.labVideo1, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.cbxQuality_2 = QComboBox(self.centralwidget)
        self.cbxQuality_2.setObjectName(u"cbxQuality_2")

        self.horizontalLayout_5.addWidget(self.cbxQuality_2)

        self.btnStrVideo1 = QPushButton(self.centralwidget)
        self.btnStrVideo1.setObjectName(u"btnStrVideo1")

        self.horizontalLayout_5.addWidget(self.btnStrVideo1)


        self.verticalLayout_c.addLayout(self.horizontalLayout_5)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_c.addWidget(self.line_2)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(320, 240))
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.verticalLayout_c.addWidget(self.label, 0, Qt.AlignTop)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.cbxQuality_3 = QComboBox(self.centralwidget)
        self.cbxQuality_3.setObjectName(u"cbxQuality_3")

        self.horizontalLayout_6.addWidget(self.cbxQuality_3)

        self.btnStrVideo2 = QPushButton(self.centralwidget)
        self.btnStrVideo2.setObjectName(u"btnStrVideo2")

        self.horizontalLayout_6.addWidget(self.btnStrVideo2)


        self.verticalLayout_c.addLayout(self.horizontalLayout_6)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_c.addWidget(self.line)

        self.pteComm = QPlainTextEdit(self.centralwidget)
        self.pteComm.setObjectName(u"pteComm")

        self.verticalLayout_c.addWidget(self.pteComm)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.lineEditSend = QLineEdit(self.centralwidget)
        self.lineEditSend.setObjectName(u"lineEditSend")
        self.lineEditSend.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_7.addWidget(self.lineEditSend)

        self.btnSend = QPushButton(self.centralwidget)
        self.btnSend.setObjectName(u"btnSend")

        self.horizontalLayout_7.addWidget(self.btnSend)


        self.verticalLayout_c.addLayout(self.horizontalLayout_7)

        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName(u"btnClear")

        self.verticalLayout_c.addWidget(self.btnClear)


        self.horizontalLayout_2.addLayout(self.verticalLayout_c)

        self.line_14 = QFrame(self.centralwidget)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.VLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line_14)

        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(3, 3)
        AquaPlayer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AquaPlayer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1251, 25))
        AquaPlayer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AquaPlayer)
        self.statusbar.setObjectName(u"statusbar")
        AquaPlayer.setStatusBar(self.statusbar)

        self.retranslateUi(AquaPlayer)

        QMetaObject.connectSlotsByName(AquaPlayer)
    # setupUi

    def retranslateUi(self, AquaPlayer):
        AquaPlayer.setWindowTitle(QCoreApplication.translate("AquaPlayer", u"\u667a\u6167\u990a\u6b96\u5100\u9336\u677f", None))
        self.labTitle.setText(QCoreApplication.translate("AquaPlayer", u"\u990a\u6b96\u5834\u72c0\u614b", None))
        self.labNameTitle.setText(QCoreApplication.translate("AquaPlayer", u"\u540d\u7a31", None))
        self.labName.setText(QCoreApplication.translate("AquaPlayer", u"\u672a\u77e5", None))
        self.labIPTitle.setText(QCoreApplication.translate("AquaPlayer", u"IP", None))
        self.labIP.setText(QCoreApplication.translate("AquaPlayer", u"192.168.100.100", None))
        self.labStatusTitle.setText(QCoreApplication.translate("AquaPlayer", u"\u72c0\u614b", None))
        self.labStatus.setText(QCoreApplication.translate("AquaPlayer", u"\u7b49\u5f85", None))
        self.labNameKeyinTitle.setText(QCoreApplication.translate("AquaPlayer", u"\u540d\u7a31", None))
        self.labIPKeyinTitle.setText(QCoreApplication.translate("AquaPlayer", u"IP", None))
        self.btnConn.setText(QCoreApplication.translate("AquaPlayer", u"\u9023\u7dda", None))
        self.labDeviceStatus.setText(QCoreApplication.translate("AquaPlayer", u"\u8a2d\u5099\u72c0\u614b", None))
        self.labDev1.setText(QCoreApplication.translate("AquaPlayer", u"\u81ea\u52d5\u6295\u9935\u5668", None))
        self.labDev1Status.setText(QCoreApplication.translate("AquaPlayer", u"\u95dc\u9589", None))
        self.cbAutoFeeder.setText(QCoreApplication.translate("AquaPlayer", u"\u555f\u52d5", None))
        self.labDev2.setText(QCoreApplication.translate("AquaPlayer", u"\u76ca\u751f\u83cc\u5674\u7051\u5668", None))
        self.labDev2Status.setText(QCoreApplication.translate("AquaPlayer", u"\u95dc\u9589", None))
        self.cbProbioticSprayer.setText(QCoreApplication.translate("AquaPlayer", u"\u555f\u52d5", None))
        self.labSensorType.setText(QCoreApplication.translate("AquaPlayer", u"\u611f\u6e2c\u5668\u8cc7\u6599", None))
        self.labTemp.setText(QCoreApplication.translate("AquaPlayer", u"\u6eab\u5ea6", None))
        self.labTempValue.setText(QCoreApplication.translate("AquaPlayer", u"0.0", None))
        self.labHum.setText(QCoreApplication.translate("AquaPlayer", u"\u6fd5\u5ea6", None))
        self.labHumValue.setText(QCoreApplication.translate("AquaPlayer", u"0.0", None))
        self.labDO.setText(QCoreApplication.translate("AquaPlayer", u"\u6eb6\u6c27", None))
        self.labDOValue.setText(QCoreApplication.translate("AquaPlayer", u"0.0", None))
        self.labPH.setText(QCoreApplication.translate("AquaPlayer", u"pH\u503c", None))
        self.labPHValue.setText(QCoreApplication.translate("AquaPlayer", u"0.0", None))
        self.labORP.setText(QCoreApplication.translate("AquaPlayer", u"ORP", None))
        self.labORPValue.setText(QCoreApplication.translate("AquaPlayer", u"0.0", None))
        self.labVideo0.setText(QCoreApplication.translate("AquaPlayer", u"video0", None))
        self.cbxQuality.setItemText(0, QCoreApplication.translate("AquaPlayer", u"1920*1080", None))
        self.cbxQuality.setItemText(1, QCoreApplication.translate("AquaPlayer", u"1280*1024", None))
        self.cbxQuality.setItemText(2, QCoreApplication.translate("AquaPlayer", u"640*480", None))
        self.cbxQuality.setItemText(3, QCoreApplication.translate("AquaPlayer", u"320*240", None))

        self.btnStrVideo0.setText(QCoreApplication.translate("AquaPlayer", u"\u958b\u59cb", None))
        self.labVideo1.setText(QCoreApplication.translate("AquaPlayer", u"Video1", None))
        self.btnStrVideo1.setText(QCoreApplication.translate("AquaPlayer", u"\u958b\u59cb", None))
        self.label.setText(QCoreApplication.translate("AquaPlayer", u"Video2", None))
        self.btnStrVideo2.setText(QCoreApplication.translate("AquaPlayer", u"\u958b\u59cb", None))
        self.btnSend.setText(QCoreApplication.translate("AquaPlayer", u"\u767c\u9001", None))
        self.btnClear.setText(QCoreApplication.translate("AquaPlayer", u"\u6e05\u9664", None))
    # retranslateUi

