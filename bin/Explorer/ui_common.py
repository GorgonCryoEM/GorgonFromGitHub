# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'common.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_Common(object):

    def setupUi(self, Common):
        Common.setObjectName(_fromUtf8("Common"))
        Common.resize(416, 339)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Common.sizePolicy().hasHeightForWidth())
        Common.setSizePolicy(sizePolicy)
        self.gridlayout = QtGui.QGridLayout(Common)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem, 2, 0, 1, 1)
        self.gridlayout1 = QtGui.QGridLayout()
        self.gridlayout1.setObjectName(_fromUtf8("gridlayout1"))
        self.pushButtonCenter = QtGui.QPushButton(Common)
        self.pushButtonCenter.setObjectName(_fromUtf8("pushButtonCenter"))
        self.gridlayout1.addWidget(self.pushButtonCenter, 0, 0, 1, 1)
        self.pushButtonClose = QtGui.QPushButton(Common)
        self.pushButtonClose.setObjectName(_fromUtf8("pushButtonClose"))
        self.gridlayout1.addWidget(self.pushButtonClose, 0, 1, 1, 1)
        self.gridlayout.addLayout(self.gridlayout1, 1, 0, 1, 1)
        self.tabWidget = QtGui.QTabWidget(Common)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.gridLayout = QtGui.QGridLayout(self.tab)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem1 = QtGui.QSpacerItem(20, 16, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.spinbox3d = Info(self.tab)
        self.spinbox3d.setObjectName(_fromUtf8("spinbox3d"))
        self.groupBoxDisplayStyle = QtGui.QGroupBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxDisplayStyle.sizePolicy().hasHeightForWidth())
        self.groupBoxDisplayStyle.setSizePolicy(sizePolicy)
        self.groupBoxDisplayStyle.setObjectName(_fromUtf8("groupBoxDisplayStyle"))
        self.gridlayout2 = QtGui.QGridLayout(self.groupBoxDisplayStyle)
        self.gridlayout2.setObjectName(_fromUtf8("gridlayout2"))
        self.radioButtonWireframe = QtGui.QRadioButton(self.groupBoxDisplayStyle)
        self.radioButtonWireframe.setObjectName(_fromUtf8("radioButtonWireframe"))
        self.buttonGroup = QtGui.QButtonGroup(Common)
        self.buttonGroup.setObjectName(_fromUtf8("buttonGroup"))
        self.buttonGroup.addButton(self.radioButtonWireframe)
        self.gridlayout2.addWidget(self.radioButtonWireframe, 0, 0, 1, 1)
        self.radioButtonFlat = QtGui.QRadioButton(self.groupBoxDisplayStyle)
        self.radioButtonFlat.setObjectName(_fromUtf8("radioButtonFlat"))
        self.buttonGroup.addButton(self.radioButtonFlat)
        self.gridlayout2.addWidget(self.radioButtonFlat, 0, 1, 1, 1)
        self.radioButtonSmooth = QtGui.QRadioButton(self.groupBoxDisplayStyle)
        self.radioButtonSmooth.setChecked(True)
        self.radioButtonSmooth.setObjectName(_fromUtf8("radioButtonSmooth"))
        self.buttonGroup.addButton(self.radioButtonSmooth)
        self.gridlayout2.addWidget(self.radioButtonSmooth, 0, 2, 1, 1)
        self.checkBoxBoundingBox = QtGui.QCheckBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxBoundingBox.sizePolicy().hasHeightForWidth())
        self.checkBoxBoundingBox.setSizePolicy(sizePolicy)
        self.checkBoxBoundingBox.setChecked(True)
        self.checkBoxBoundingBox.setObjectName(_fromUtf8("checkBoxBoundingBox"))
        self.pushButtonBoundingBoxColor = ColoredPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBoundingBoxColor.sizePolicy().hasHeightForWidth())
        self.pushButtonBoundingBoxColor.setSizePolicy(sizePolicy)
        self.pushButtonBoundingBoxColor.setText(_fromUtf8(""))
        self.pushButtonBoundingBoxColor.setObjectName(_fromUtf8("pushButtonBoundingBoxColor"))
        self.pushButtonModelColor = ColoredPushButton(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonModelColor.sizePolicy().hasHeightForWidth())
        self.pushButtonModelColor.setSizePolicy(sizePolicy)
        self.pushButtonModelColor.setText(_fromUtf8(""))
        self.pushButtonModelColor.setObjectName(_fromUtf8("pushButtonModelColor"))
        self.checkBoxModelVisible = QtGui.QCheckBox(self.tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxModelVisible.sizePolicy().hasHeightForWidth())
        self.checkBoxModelVisible.setSizePolicy(sizePolicy)
        self.checkBoxModelVisible.setChecked(True)
        self.checkBoxModelVisible.setObjectName(_fromUtf8("checkBoxModelVisible"))
        
        self.gridLayout.addWidget(self.groupBoxDisplayStyle, 0, 0, 1, -1)
        self.gridLayout.addWidget(self.checkBoxBoundingBox, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.pushButtonBoundingBoxColor, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.checkBoxModelVisible, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.pushButtonModelColor, 1, 1, 1, 1)
#         self.gridLayout.addItem(spacerItem1, 3, 1, 1, 1)
        self.gridLayout.addWidget(self.spinbox3d, 2, 0, 1, -1)
        
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.gridlayout3 = QtGui.QGridLayout(self.tab_3)
        self.gridlayout3.setObjectName(_fromUtf8("gridlayout3"))
        self.label_2 = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridlayout3.addWidget(self.label_2, 0, 0, 1, 1)
        self.labelModelName = QtGui.QLabel(self.tab_3)
        self.labelModelName.setMaximumSize(QtCore.QSize(200, 16777215))
        self.labelModelName.setWordWrap(True)
        self.labelModelName.setObjectName(_fromUtf8("labelModelName"))
        self.gridlayout3.addWidget(self.labelModelName, 0, 1, 1, 1)
        self.label = QtGui.QLabel(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridlayout3.addWidget(self.label, 1, 0, 1, 1)
        self.labelModelSize = QtGui.QLabel(self.tab_3)
        self.labelModelSize.setObjectName(_fromUtf8("labelModelSize"))
        self.gridlayout3.addWidget(self.labelModelSize, 1, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridlayout3.addItem(spacerItem2, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.gridlayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Common)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Common)
        Common.setTabOrder(self.pushButtonCenter, self.pushButtonClose)
        Common.setTabOrder(self.pushButtonClose, self.tabWidget)
        Common.setTabOrder(self.tabWidget, self.radioButtonWireframe)
        Common.setTabOrder(self.radioButtonWireframe, self.radioButtonFlat)
        Common.setTabOrder(self.radioButtonFlat, self.radioButtonSmooth)
        Common.setTabOrder(self.radioButtonSmooth, self.checkBoxBoundingBox)
        Common.setTabOrder(self.checkBoxBoundingBox, self.pushButtonBoundingBoxColor)
        Common.setTabOrder(self.pushButtonBoundingBoxColor, self.checkBoxModelVisible)
        Common.setTabOrder(self.checkBoxModelVisible, self.pushButtonModelColor)

    def retranslateUi(self, Common):
        Common.setWindowTitle(_translate("Common", "Visualization", None))
        self.pushButtonCenter.setText(_translate("Common", "Center", "Center the model"))
        self.pushButtonClose.setText(_translate("Common", "Unload Model", "Close the model"))
        self.groupBoxDisplayStyle.setTitle(_translate("Common", "Display Style:", None))
        self.radioButtonWireframe.setText(_translate("Common", "Wireframe", None))
        self.radioButtonFlat.setText(_translate("Common", "Flat", None))
        self.radioButtonSmooth.setText(_translate("Common", "Smooth", None))
        self.checkBoxBoundingBox.setText(_translate("Common", "Show outline box colored:", None))
        self.checkBoxModelVisible.setText(_translate("Common", "Show model colored:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Common", "Visualization", None))
        self.label_2.setText(_translate("Common", "File Name:", None))
        self.labelModelName.setText(_translate("Common", "...", None))
        self.label.setText(_translate("Common", "Model Size:", None))
        self.labelModelSize.setText(_translate("Common", "{X, Y, Z}", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Common", "Properties", None))

from colored_push_button import ColoredPushButton
from info import Info
