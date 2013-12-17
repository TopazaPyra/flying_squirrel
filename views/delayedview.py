# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delayedview.ui'
#
# Created: Wed Sep 11 15:26:16 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_delayedView(object):
    def setupUi(self, delayedView):
        delayedView.setObjectName(_fromUtf8("delayedView"))
        delayedView.resize(400, 300)
        delayedView.setFrameShape(QtGui.QFrame.StyledPanel)
        delayedView.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(delayedView)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(delayedView)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)

        self.retranslateUi(delayedView)
        QtCore.QMetaObject.connectSlotsByName(delayedView)

    def retranslateUi(self, delayedView):
        delayedView.setWindowTitle(QtGui.QApplication.translate("delayedView", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("delayedView", "Vue différée", None, QtGui.QApplication.UnicodeUTF8))

