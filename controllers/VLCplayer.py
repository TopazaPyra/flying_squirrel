#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui
from views.vlcplayer import Ui_VLCPlayer

class VLCPlayer(QtGui.QFrame, Ui_VLCPlayer):
    def __init__(self):
        super (VLCPlayer, self).__init__()
        self.createPlayer()
        self.setupUi(self)
        self.connectActions()
        self.isPaused = False
        
