#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, codecs, shutil, string, unicodedata

from PyQt4 import QtCore, QtGui
from peewee import *

from views.newproject import Ui_newProjectWizard

from models.corpus import *

from controllers.mainwindow import project

class newProjectWizard(QtGui.QWizard, Ui_newProjectWizard):
    
    def __init__(self,  parent=None):
        super (newProjectWizard, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        
    def connectActions(self):
        self.projectPathButton.clicked.connect(self.openProjectPath)
        self.corpusFilePathButton.clicked.connect(self.openCorpusFilePath)
        self.button(newProjectWizard.FinishButton).clicked.connect(self.createProject)
        self.wizardPage2.nextId = self.corpusSettingNextId
        
    def openProjectPath(self):
        directoryName = QtGui.QFileDialog.getExistingDirectory(self, u"Répertoire", QtCore.QDir.homePath())
        
        if directoryName:
            self.folderPath.setText(directoryName)
    
    def openCorpusFilePath(self):
        corpusFile = QtGui.QFileDialog.getOpenFileName(self,  u"Corpus",  QtCore.QDir.homePath(),  "Corpus (*.xml)")
        
        if corpusFile:
            self.corpusFilePath.setText(corpusFile)
  
    def corpusSettingNextId(self):
        self.projectNameValue.setText(self.projectNameEdit.text())
        self.projectFolderValue.setText(self.folderPath.text())
        
        if self.newCorpusButton.isChecked():
            self.corpusValue.setText(u'nouveau corpus')
            return 3
        else:
            self.corpusValue.setText(u'chargé à partir d\'un fichier existant')
            return 2
            
    def sanitize(self, filename):

            validFilenameChars = "-_.%s%s" % (string.ascii_letters, string.digits)
            cleanedFilename = unicodedata.normalize('NFKD',  filename)
            cleanedFilename = cleanedFilename.replace(' ', '_')

            return ''.join(c for c in cleanedFilename if c in validFilenameChars) 
        
    def createProject(self):
        directoryName = self.folderPath.text()
        project['name'] = unicode(self.projectNameEdit.text())
		
        if directoryName and project['name']:
            project['folder'] = unicode(directoryName) + "/" + self.sanitize(project['name'])
            if not os.path.exists(project['folder']):
                os.mkdir(project['folder'])
                
                if self.newCorpusButton.isChecked():
                    corpusManager = CorpusManager()
                    corpus = corpusManager.createCorpus()
                    
                    corpusFile = codecs.open(project['folder'] + "/" + self.sanitize(project['name']) + ".xml",  'w',  'utf-8')
                    corpusFile.write(corpus.toprettyxml())
                    
                elif self.existingCorpusButton.isChecked():
                    existingCorpus = unicode(self.corpusFilePath.text())
                    shutil.copyfile(existingCorpus,  project['folder'] + "/" + self.sanitize(project['name']) + ".xml")
                
                project['database'] = project['folder'] + "/" + self.sanitize(project['name']) + ".db"
                
                exec 'from models.models import *'
                
                Meta.create_table()
                Video.create_table()
                Sequence.create_table()
                Tag.create_table()
                
                Meta.create(projectName=project['name'])
                
                if self.newCorpusButton.isChecked():
                    self.parent().settingsViewUi()
                else :
                    self.parent().directViewUi()
                
                self.parent().setWindowTitle('Flying Squirrel - ' + project['name'])
                self.parent().activateMenuLinks()
                
            else:
                reply = QtGui.QMessageBox()
                reply.setText(u"Ce répertoire existe déjà. Supprimez-le ou changez de nom de projet.")
                reply.exec_()
