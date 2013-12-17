#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

from views.directview import Ui_directView

from models.corpus import *
from models.tag import *

from controllers.mainwindow import project

class directView(QtGui.QFrame, Ui_directView):
    def __init__(self,  parent=None):
        super (directView, self).__init__(parent)
        self.setupUi(self)
        
        corpusManager = CorpusManager()
        corpus = corpusManager.getCorpus(project['database'][:-3] + '.xml')
        tagsManager = TagsManager(corpus)
        tags = tagsManager.getTags()
         
        i = 0
        buttons = {}
        
        for tag in tags:
            buttons[i] =  QtGui.QPushButton(self)
            buttons[i].setMinimumSize(QtCore.QSize(0, 40))
            buttons[i].setCheckable(True)
            
            buttons[i].setText(tag.childNodes[0].data)
            
            if i % 2 == 0:
                self.verticalLayout1.addWidget(buttons[i]) 
            else:
                self.verticalLayout2.addWidget(buttons[i])

            i = i + 1
