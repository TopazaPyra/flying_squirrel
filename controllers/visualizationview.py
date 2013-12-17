#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from views.visualizationview import Ui_visualizationView

class visualizationView(QtGui.QFrame, Ui_visualizationView):
    def __init__(self):
        super (visualizationView, self).__init__()
        self.setupUi(self)
