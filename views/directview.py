# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'directview.ui'
#
# Created: Thu Oct 24 14:56:56 2013
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

class Ui_directView(object):
    def setupUi(self, directView):
        directView.setObjectName(_fromUtf8("directView"))
        directView.resize(400, 300)
        directView.setFrameShape(QtGui.QFrame.StyledPanel)
        directView.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(directView)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout1 = QtGui.QVBoxLayout()
        self.verticalLayout1.setSpacing(10)
        self.verticalLayout1.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout1.setContentsMargins(-1, -1, 10, -1)
        self.verticalLayout1.setObjectName(_fromUtf8("verticalLayout1"))
        self.horizontalLayout.addLayout(self.verticalLayout1)
        self.verticalLayout2 = QtGui.QVBoxLayout()
        self.verticalLayout2.setSpacing(10)
        self.verticalLayout2.setObjectName(_fromUtf8("verticalLayout2"))
        self.horizontalLayout.addLayout(self.verticalLayout2)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(directView)
        QtCore.QMetaObject.connectSlotsByName(directView)

    def retranslateUi(self, directView):
        directView.setWindowTitle(_translate("directView", "Frame", None))

