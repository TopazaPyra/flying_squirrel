#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from views.about import Ui_aboutDialog

class aboutDialog(QtGui.QDialog, Ui_aboutDialog):
    def __init__(self, parent=None):
        super (aboutDialog, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
		
    def connectActions(self):
        self.okButton.clicked.connect(QtGui.QDialog.close)
