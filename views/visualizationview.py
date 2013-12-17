# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visualizationview.ui'
#
# Created: Wed Sep 11 15:26:42 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_visualizationView(object):
    def setupUi(self, visualizationView):
        visualizationView.setObjectName(_fromUtf8("visualizationView"))
        visualizationView.resize(400, 300)
        visualizationView.setFrameShape(QtGui.QFrame.StyledPanel)
        visualizationView.setFrameShadow(QtGui.QFrame.Raised)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(visualizationView)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(visualizationView)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)

        self.retranslateUi(visualizationView)
        QtCore.QMetaObject.connectSlotsByName(visualizationView)

    def retranslateUi(self, visualizationView):
        visualizationView.setWindowTitle(QtGui.QApplication.translate("visualizationView", "Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("visualizationView", "Vue visualisation", None, QtGui.QApplication.UnicodeUTF8))

