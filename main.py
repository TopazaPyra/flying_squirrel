#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtGui

from controllers.mainwindow import mainWindow

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    
    window = mainWindow()
    window.show()
    if sys.argv[1:]:
        player.OpenFile(sys.argv[1])
    sys.exit(app.exec_())
