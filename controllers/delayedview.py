#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from views.delayedview import Ui_delayedView

class delayedView(QtGui.QFrame, Ui_delayedView):
    def __init__(self):
        super (delayedView, self).__init__()
        self.setupUi(self)
