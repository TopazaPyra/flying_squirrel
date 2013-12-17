# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settingsview.ui'
#
# Created: Mon Oct 21 10:47:04 2013
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_settingsView(object):
    def setupUi(self, settingsView):
        settingsView.setObjectName(_fromUtf8("settingsView"))
        settingsView.resize(400, 393)
        settingsView.setFrameShape(QtGui.QFrame.StyledPanel)
        settingsView.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(settingsView)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widget = QtGui.QWidget(settingsView)
        self.widget.setObjectName(_fromUtf8("widget"))
	self.tagEdit1 = QtGui.QLineEdit(self.widget)
        self.tagEdit1.setGeometry(QtCore.QRect(54, 10, 200, 24))
        self.tagEdit1.setObjectName(_fromUtf8("tagEdit1"))
	self.tagEdit2 = QtGui.QLineEdit(self.widget)
        self.tagEdit2.setGeometry(QtCore.QRect(54, 40, 200, 24))
        self.tagEdit2.setObjectName(_fromUtf8("tagEdit2"))
	self.tagEdit3 = QtGui.QLineEdit(self.widget)
        self.tagEdit3.setGeometry(QtCore.QRect(54, 70, 200, 24))
        self.tagEdit3.setObjectName(_fromUtf8("tagEdit3"))
	self.tagEdit4 = QtGui.QLineEdit(self.widget)
        self.tagEdit4.setGeometry(QtCore.QRect(54, 100, 200, 24))
        self.tagEdit4.setObjectName(_fromUtf8("tagEdit4"))
        self.tagEdit5 = QtGui.QLineEdit(self.widget)
        self.tagEdit5.setGeometry(QtCore.QRect(54, 130, 200, 24))
        self.tagEdit5.setObjectName(_fromUtf8("tagEdit5"))
	self.tagEdit6 = QtGui.QLineEdit(self.widget)
        self.tagEdit6.setGeometry(QtCore.QRect(54, 160, 200, 24))
        self.tagEdit6.setObjectName(_fromUtf8("tagEdit6"))
        self.tagEdit7 = QtGui.QLineEdit(self.widget)
        self.tagEdit7.setGeometry(QtCore.QRect(54, 190, 200, 24))
        self.tagEdit7.setObjectName(_fromUtf8("tagEdit7"))
	self.tagEdit8 = QtGui.QLineEdit(self.widget)
        self.tagEdit8.setGeometry(QtCore.QRect(54, 220, 200, 24))
        self.tagEdit8.setObjectName(_fromUtf8("tagEdit8"))
        self.tagEdit9 = QtGui.QLineEdit(self.widget)
        self.tagEdit9.setGeometry(QtCore.QRect(54, 250, 200, 24))
        self.tagEdit9.setObjectName(_fromUtf8("tagEdit9"))
        self.tagEdit10 = QtGui.QLineEdit(self.widget)
        self.tagEdit10.setGeometry(QtCore.QRect(54, 280, 200, 24))
        self.tagEdit10.setObjectName(_fromUtf8("tagEdit10"))
	self.tagLabel1 = QtGui.QLabel(self.widget)
        self.tagLabel1.setGeometry(QtCore.QRect(0, 10, 40, 24))
        self.tagLabel1.setObjectName(_fromUtf8("tagLabel1"))
	self.tagLabel2 = QtGui.QLabel(self.widget)
        self.tagLabel2.setGeometry(QtCore.QRect(0, 40, 40, 24))
        self.tagLabel2.setObjectName(_fromUtf8("tagLabel2"))
	self.tagLabel3 = QtGui.QLabel(self.widget)
        self.tagLabel3.setGeometry(QtCore.QRect(0, 70, 40, 24))
        self.tagLabel3.setObjectName(_fromUtf8("tagLabel3"))
	self.tagLabel4 = QtGui.QLabel(self.widget)
        self.tagLabel4.setGeometry(QtCore.QRect(0, 100, 40, 24))
        self.tagLabel4.setObjectName(_fromUtf8("tagLabel4"))
	self.tagLabel5 = QtGui.QLabel(self.widget)
        self.tagLabel5.setGeometry(QtCore.QRect(0, 130, 40, 24))
        self.tagLabel5.setObjectName(_fromUtf8("tagLabel5"))
	self.tagLabel6 = QtGui.QLabel(self.widget)
        self.tagLabel6.setGeometry(QtCore.QRect(0, 160, 40, 24))
        self.tagLabel6.setObjectName(_fromUtf8("tagLabel6"))
	self.tagLabel7 = QtGui.QLabel(self.widget)
        self.tagLabel7.setGeometry(QtCore.QRect(0, 190, 40, 24))
        self.tagLabel7.setObjectName(_fromUtf8("tagLabel7"))
	self.tagLabel8 = QtGui.QLabel(self.widget)
        self.tagLabel8.setGeometry(QtCore.QRect(0, 220, 40, 24))
        self.tagLabel8.setObjectName(_fromUtf8("tagLabel8"))
	self.tagLabel9 = QtGui.QLabel(self.widget)
        self.tagLabel9.setGeometry(QtCore.QRect(0, 250, 40, 24))
        self.tagLabel9.setObjectName(_fromUtf8("tagLabel9"))
        self.tagLabel10 = QtGui.QLabel(self.widget)
        self.tagLabel10.setGeometry(QtCore.QRect(0, 280, 48, 24))
        self.tagLabel10.setObjectName(_fromUtf8("tagLabel10"))
        self.buttonBox = QtGui.QDialogButtonBox(self.widget)
        self.buttonBox.setGeometry(QtCore.QRect(0, 330, 324, 27))
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Reset|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_2.addWidget(self.widget)

        self.retranslateUi(settingsView)
        QtCore.QMetaObject.connectSlotsByName(settingsView)
        settingsView.setTabOrder(self.tagEdit1, self.tagEdit2)
        settingsView.setTabOrder(self.tagEdit2, self.tagEdit3)
        settingsView.setTabOrder(self.tagEdit3, self.tagEdit4)
        settingsView.setTabOrder(self.tagEdit4, self.tagEdit5)
        settingsView.setTabOrder(self.tagEdit5, self.tagEdit6)
        settingsView.setTabOrder(self.tagEdit6, self.tagEdit7)
        settingsView.setTabOrder(self.tagEdit7, self.tagEdit8)
        settingsView.setTabOrder(self.tagEdit8, self.tagEdit9)
        settingsView.setTabOrder(self.tagEdit9, self.tagEdit10)
        settingsView.setTabOrder(self.tagEdit10, self.buttonBox)

    def retranslateUi(self, settingsView):
        settingsView.setWindowTitle(_translate("settingsView", "Frame", None))
        self.tagLabel6.setText(_translate("settingsView", "Tag 6 :", None))
        self.tagLabel10.setText(_translate("settingsView", "Tag 10 :", None))
        self.tagLabel3.setText(_translate("settingsView", "Tag 3 :", None))
        self.tagLabel8.setText(_translate("settingsView", "Tag 8 :", None))
        self.tagLabel5.setText(_translate("settingsView", "Tag 5 :", None))
        self.tagLabel1.setText(_translate("settingsView", "Tag 1 :", None))
        self.tagLabel7.setText(_translate("settingsView", "Tag 7 :", None))
        self.tagLabel4.setText(_translate("settingsView", "Tag 4 :", None))
        self.tagLabel2.setText(_translate("settingsView", "Tag 2 :", None))
        self.tagLabel9.setText(_translate("settingsView", "Tag 9 :", None))

