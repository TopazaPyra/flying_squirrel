# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Oct 31 12:04:38 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(734, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../img/flying_squirrel.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        self.menuVues = QtGui.QMenu(self.menubar)
        self.menuVues.setObjectName(_fromUtf8("menuVues"))
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        self.menuAide = QtGui.QMenu(self.menubar)
        self.menuAide.setObjectName(_fromUtf8("menuAide"))
        self.menuVideos = QtGui.QMenu(self.menubar)
        self.menuVideos.setObjectName(_fromUtf8("menuVideos"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNewProject = QtGui.QAction(MainWindow)
        self.actionNewProject.setObjectName(_fromUtf8("actionNewProject"))
        self.actionOpenProject = QtGui.QAction(MainWindow)
        self.actionOpenProject.setObjectName(_fromUtf8("actionOpenProject"))
        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setEnabled(False)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionPreferences = QtGui.QAction(MainWindow)
        self.actionPreferences.setObjectName(_fromUtf8("actionPreferences"))
        self.actionDocumentation = QtGui.QAction(MainWindow)
        self.actionDocumentation.setObjectName(_fromUtf8("actionDocumentation"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionDirect = QtGui.QAction(MainWindow)
        self.actionDirect.setEnabled(False)
        self.actionDirect.setObjectName(_fromUtf8("actionDirect"))
        self.actionDelayed = QtGui.QAction(MainWindow)
        self.actionDelayed.setEnabled(False)
        self.actionDelayed.setObjectName(_fromUtf8("actionDelayed"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setEnabled(False)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionVisualization = QtGui.QAction(MainWindow)
        self.actionVisualization.setEnabled(False)
        self.actionVisualization.setObjectName(_fromUtf8("actionVisualization"))
        self.actionAddVideo = QtGui.QAction(MainWindow)
        self.actionAddVideo.setEnabled(False)
        self.actionAddVideo.setObjectName(_fromUtf8("actionAddVideo"))
        self.menuFichier.addAction(self.actionNewProject)
        self.menuFichier.addAction(self.actionOpenProject)
        self.menuFichier.addAction(self.actionSave)
        self.menuFichier.addAction(self.actionExit)
        self.menuVues.addAction(self.actionDirect)
        self.menuVues.addAction(self.actionDelayed)
        self.menuVues.addAction(self.actionSettings)
        self.menuVues.addAction(self.actionVisualization)
        self.menuOptions.addAction(self.actionPreferences)
        self.menuAide.addAction(self.actionDocumentation)
        self.menuAide.addAction(self.actionAbout)
        self.menuVideos.addAction(self.actionAddVideo)
        self.menuVideos.addSeparator()
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuVues.menuAction())
        self.menubar.addAction(self.menuVideos.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAide.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Flying Squirrel", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.menuVues.setTitle(_translate("MainWindow", "Vues", None))
        self.menuOptions.setTitle(_translate("MainWindow", "Options", None))
        self.menuAide.setTitle(_translate("MainWindow", "Aide", None))
        self.menuVideos.setTitle(_translate("MainWindow", "Vidéos", None))
        self.actionNewProject.setText(_translate("MainWindow", "Nouveau projet", None))
        self.actionOpenProject.setText(_translate("MainWindow", "Ouvrir un projet", None))
        self.actionSave.setText(_translate("MainWindow", "Enregistrer", None))
        self.actionExit.setText(_translate("MainWindow", "Quitter", None))
        self.actionPreferences.setText(_translate("MainWindow", "Préférences", None))
        self.actionDocumentation.setText(_translate("MainWindow", "Documentation", None))
        self.actionAbout.setText(_translate("MainWindow", "À propos de Flying Squirrel", None))
        self.actionDirect.setText(_translate("MainWindow", "Direct", None))
        self.actionDelayed.setText(_translate("MainWindow", "Différé", None))
        self.actionSettings.setText(_translate("MainWindow", "Paramétrage", None))
        self.actionVisualization.setText(_translate("MainWindow", "Visualisation", None))
        self.actionAddVideo.setText(_translate("MainWindow", "Ajouter une vidéo", None))

