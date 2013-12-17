#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs

from PyQt4 import QtCore, QtGui
from xml.dom import minidom

from views.settingsview import Ui_settingsView

from models.corpus import *
from models.tag import *

from controllers.mainwindow import project

class settingsView(QtGui.QFrame, Ui_settingsView):
    def __init__(self, parent=None):
        super (settingsView, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        
        corpusManager = CorpusManager()
        corpus = corpusManager.getCorpus(project['database'][:-3] + '.xml')

        tagsManager = TagsManager(corpus)
        tags = tagsManager.getTags()

        tagEditList = self.widget.findChildren(QtGui.QLineEdit)

        i = 0
        
        for tag in tags:
            tagEditList[i].setText(tag.childNodes[0].data)
            i = i + 1
        
    def connectActions(self):
        
        self.buttonBox.button(QtGui.QDialogButtonBox.Reset).clicked.connect(self.resetTags)
        #self.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(self.cancelSettings)
        self.buttonBox.button(QtGui.QDialogButtonBox.Save).clicked.connect(self.saveTags)
    
    def resetTags(self):
        tagEditList = self.widget.findChildren(QtGui.QLineEdit)
        
        for tagEdit in tagEditList:
            tagEdit.clear()

    #def cancelSettings(self):
    
    def saveTags(self):
        corpusManager = CorpusManager()
        corpus = corpusManager.createCorpus()
        tagsManager = TagsManager(corpus)
        
        for tag in self.widget.findChildren(QtGui.QLineEdit):
             if tag.text():
                 tagsManager.addTag(unicode(tag.text()))

        corpusFile = codecs.open(project['database'][:-3] + ".xml",  'w',  'utf-8')
        corpusFile.write(corpus.toxml())
