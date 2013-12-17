#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ntpath

from PyQt4 import QtCore, QtGui
from peewee import *

from views.mainwindow import Ui_MainWindow

project = {}

class mainWindow(QtGui.QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super (mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
        
    def connectActions(self):
        self.actionNewProject.triggered.connect(self.newProject)
        self.actionOpenProject.triggered.connect(self.openProject)
        self.actionDirect.triggered.connect(self.directViewUi)
        self.actionDelayed.triggered.connect(self.delayedViewUi)
        self.actionSettings.triggered.connect(self.settingsViewUi)
        self.actionVisualization.triggered.connect(self.visualizationViewUi)
        self.actionAddVideo.triggered.connect(self.addVideo)
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(QtGui.qApp.quit)
    
    def newProject(self):
        exec 'from controllers.newprojectwizard import newProjectWizard'
        
        self.w = newProjectWizard(self)
        self.w.show()
    
    def openProject(self):
        projectDatabaseFile = QtGui.QFileDialog.getOpenFileName(self, "Ouvrir un projet", QtCore.QDir.homePath(), "Fichiers de projet Flying Squirrel (*.db);; Tous les fichiers (*.*)")
        
        if (projectDatabaseFile):
            project['database'] = unicode(projectDatabaseFile)
            
            project['folder'] = ntpath.dirname(project['database'])
        
            try:
                exec 'from models.models import *'
                
                project['name'] = Meta.get(Meta.id == 1).projectName
                
                self.directViewUi()
                self.setWindowTitle('Flying Squirrel - ' + project['name'])
                self.activateMenuLinks()
                self.updateVideoList()
            
            except IOError,  databaseError:
               print databaseError
    
    def addVideo(self):
        videoPath = QtGui.QFileDialog.getOpenFileName(self, u"Ajouter une vidéo", QtCore.QDir.homePath(), u"Fichiers vidéo (*.ogv *.avi *.mp4);; Tous les fichiers (*.*)")

        if(videoPath):
            exec 'from models.models import *'
                
            videoPath = unicode(videoPath)
            videoFile = ntpath.basename(videoPath)
                
            try:
                Video.create(path=videoPath, title=videoFile)
                
            except:
                print u"Erreur lors de l'ajout de la vidéo au projet.\nCe fichier fait peut-être déjà partie du projet ou une autre vidéo porte le même nom."
                
            self.updateVideoList()

        
    def about(self):
        exec 'from controllers.aboutdialog import aboutDialog'
        
        self.w = aboutDialog(self)
        self.w.show()

    def directViewUi(self):
        exec 'from controllers.directview import directView'
        exec 'from controllers.VLCplayer import VLCPlayer'
        
        self.directView = directView(self)
        self.setCentralWidget(self.directView)
        self.VLCPlayer = VLCPlayer()
        self.directView.horizontalLayout.insertWidget(0, self.VLCPlayer)
        
        self.directView.verticalLayout1.setAlignment(QtCore.Qt.AlignTop)
        self.directView.verticalLayout2.setAlignment(QtCore.Qt.AlignTop)

    def delayedViewUi(self):
        exec 'from controllers.delayedview import delayedView'
        
        if hasattr(self,  'VLCPlayer') and self.VLCPlayer.mediaplayer.is_playing():
            self.VLCPlayer.mediaplayer.stop()
        
        self.delayedView = delayedView()
        self.setCentralWidget(self.delayedView)

    def settingsViewUi(self):
        exec 'from controllers.settingsview import settingsView'
        
        if hasattr(self,  'VLCPlayer') and self.VLCPlayer.mediaplayer.is_playing():
            self.VLCPlayer.mediaplayer.stop()
            
        self.settingsView = settingsView(self)
        self.setCentralWidget(self.settingsView)

    def visualizationViewUi(self):
        exec 'from controllers.visualizationview import visualizationView'
        
        if hasattr(self,  'VLCPlayer') and self.VLCPlayer.mediaplayer.is_playing():
            self.VLCPlayer.mediaplayer.stop()
            
        self.visualizationView = visualizationView()
        self.setCentralWidget(self.visualizationView)
    
    def activateMenuLinks(self):
        self.actionSave.setEnabled(True)
        self.actionDirect.setEnabled(True)
        self.actionDelayed.setEnabled(True)
        self.actionSettings.setEnabled(True)
        self.actionVisualization.setEnabled(True)
        self.actionAddVideo.setEnabled(True)

    def updateVideoList(self):
        exec 'from models.models import *'
        
        i = 0
        videoLinks = {}
        
        for video in Video.select():
            videoLinks[i] = QtGui.QAction(self)
            videoLinks[i].setText(video.title)
            self.menuVideos.addAction(videoLinks[i])
        
        if(videoLinks):
            actionManageVideos = QtGui.QAction(self)
            actionManageVideos.setText(u'Gérer les vidéos')
            self.menuVideos.addAction(actionManageVideos)
