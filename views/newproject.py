# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newproject.ui'
#
# Created: Thu Oct 10 13:19:40 2013
#      by: PyQt4 UI code generator 4.10.2
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

class Ui_newProjectWizard(object):
    def setupUi(self, newProjectWizard):
        newProjectWizard.setObjectName(_fromUtf8("newProjectWizard"))
        newProjectWizard.resize(409, 300)
        self.wizardPage1 = QtGui.QWizardPage()
        self.wizardPage1.setObjectName(_fromUtf8("wizardPage1"))
        self.folderLabel = QtGui.QLabel(self.wizardPage1)
        self.folderLabel.setGeometry(QtCore.QRect(0, 135, 81, 16))
        self.folderLabel.setObjectName(_fromUtf8("folderLabel"))
        self.projectPathButton = QtGui.QToolButton(self.wizardPage1)
        self.projectPathButton.setGeometry(QtCore.QRect(360, 130, 26, 23))
        self.projectPathButton.setObjectName(_fromUtf8("projectPathButton"))
        self.projectNameEdit = QtGui.QLineEdit(self.wizardPage1)
        self.projectNameEdit.setGeometry(QtCore.QRect(110, 80, 271, 25))
        self.projectNameEdit.setObjectName(_fromUtf8("projectNameEdit"))
        self.newProjectLabel = QtGui.QLabel(self.wizardPage1)
        self.newProjectLabel.setGeometry(QtCore.QRect(0, 85, 101, 16))
        self.newProjectLabel.setObjectName(_fromUtf8("newProjectLabel"))
        self.folderPath = QtGui.QLineEdit(self.wizardPage1)
        self.folderPath.setGeometry(QtCore.QRect(110, 130, 251, 25))
        self.folderPath.setText(_fromUtf8(""))
        self.folderPath.setObjectName(_fromUtf8("folderPath"))
        self.page1Title = QtGui.QLabel(self.wizardPage1)
        self.page1Title.setGeometry(QtCore.QRect(0, 30, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.page1Title.setFont(font)
        self.page1Title.setObjectName(_fromUtf8("page1Title"))
        newProjectWizard.addPage(self.wizardPage1)
        self.wizardPage2 = QtGui.QWizardPage()
        self.wizardPage2.setObjectName(_fromUtf8("wizardPage2"))
        self.newCorpusButton = QtGui.QRadioButton(self.wizardPage2)
        self.newCorpusButton.setGeometry(QtCore.QRect(110, 120, 201, 21))
        self.newCorpusButton.setChecked(True)
        self.newCorpusButton.setObjectName(_fromUtf8("newCorpusButton"))
        self.existingCorpusButton = QtGui.QRadioButton(self.wizardPage2)
        self.existingCorpusButton.setGeometry(QtCore.QRect(110, 150, 191, 21))
        self.existingCorpusButton.setObjectName(_fromUtf8("existingCorpusButton"))
        self.tagsCorpusLabel = QtGui.QLabel(self.wizardPage2)
        self.tagsCorpusLabel.setGeometry(QtCore.QRect(0, 85, 191, 16))
        self.tagsCorpusLabel.setObjectName(_fromUtf8("tagsCorpusLabel"))
        self.page2Title = QtGui.QLabel(self.wizardPage2)
        self.page2Title.setGeometry(QtCore.QRect(0, 30, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.page2Title.setFont(font)
        self.page2Title.setObjectName(_fromUtf8("page2Title"))
        newProjectWizard.addPage(self.wizardPage2)
        self.wizardPage3 = QtGui.QWizardPage()
        self.wizardPage3.setObjectName(_fromUtf8("wizardPage3"))
        self.corpusFilePathButton = QtGui.QToolButton(self.wizardPage3)
        self.corpusFilePathButton.setGeometry(QtCore.QRect(360, 80, 26, 23))
        self.corpusFilePathButton.setObjectName(_fromUtf8("corpusFilePathButton"))
        self.corpusFilePath = QtGui.QLineEdit(self.wizardPage3)
        self.corpusFilePath.setGeometry(QtCore.QRect(130, 80, 231, 25))
        self.corpusFilePath.setText(_fromUtf8(""))
        self.corpusFilePath.setObjectName(_fromUtf8("corpusFilePath"))
        self.corpusFileLabel = QtGui.QLabel(self.wizardPage3)
        self.corpusFileLabel.setGeometry(QtCore.QRect(0, 85, 111, 16))
        self.corpusFileLabel.setObjectName(_fromUtf8("corpusFileLabel"))
        self.page3Title = QtGui.QLabel(self.wizardPage3)
        self.page3Title.setGeometry(QtCore.QRect(0, 30, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.page3Title.setFont(font)
        self.page3Title.setObjectName(_fromUtf8("page3Title"))
        newProjectWizard.addPage(self.wizardPage3)
        self.wizardPage4 = QtGui.QWizardPage()
        self.wizardPage4.setObjectName(_fromUtf8("wizardPage4"))
        self.page4Title = QtGui.QLabel(self.wizardPage4)
        self.page4Title.setGeometry(QtCore.QRect(0, 30, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.page4Title.setFont(font)
        self.page4Title.setObjectName(_fromUtf8("page4Title"))
        self.congratulationLabel = QtGui.QLabel(self.wizardPage4)
        self.congratulationLabel.setGeometry(QtCore.QRect(0, 85, 381, 16))
        self.congratulationLabel.setObjectName(_fromUtf8("congratulationLabel"))
        self.projectNameLabel = QtGui.QLabel(self.wizardPage4)
        self.projectNameLabel.setGeometry(QtCore.QRect(0, 120, 121, 16))
        self.projectNameLabel.setObjectName(_fromUtf8("projectNameLabel"))
        self.projectNameValue = QtGui.QLabel(self.wizardPage4)
        self.projectNameValue.setGeometry(QtCore.QRect(140, 120, 251, 16))
        self.projectNameValue.setObjectName(_fromUtf8("projectNameValue"))
        self.projectFolderLabel = QtGui.QLabel(self.wizardPage4)
        self.projectFolderLabel.setGeometry(QtCore.QRect(0, 150, 121, 16))
        self.projectFolderLabel.setObjectName(_fromUtf8("projectFolderLabel"))
        self.projectFolderValue = QtGui.QLabel(self.wizardPage4)
        self.projectFolderValue.setGeometry(QtCore.QRect(140, 150, 251, 16))
        self.projectFolderValue.setObjectName(_fromUtf8("projectFolderValue"))
        self.corpusLabel = QtGui.QLabel(self.wizardPage4)
        self.corpusLabel.setGeometry(QtCore.QRect(0, 180, 57, 14))
        self.corpusLabel.setObjectName(_fromUtf8("corpusLabel"))
        self.corpusValue = QtGui.QLabel(self.wizardPage4)
        self.corpusValue.setGeometry(QtCore.QRect(140, 180, 251, 16))
        self.corpusValue.setObjectName(_fromUtf8("corpusValue"))
        newProjectWizard.addPage(self.wizardPage4)

        self.retranslateUi(newProjectWizard)
        QtCore.QMetaObject.connectSlotsByName(newProjectWizard)

    def retranslateUi(self, newProjectWizard):
        newProjectWizard.setWindowTitle(_translate("newProjectWizard", "Nouveau projet", None))
        self.folderLabel.setText(_translate("newProjectWizard", "Répertoire :", None))
        self.projectPathButton.setText(_translate("newProjectWizard", "...", None))
        self.newProjectLabel.setText(_translate("newProjectWizard", "Nom du projet :", None))
        self.page1Title.setText(_translate("newProjectWizard", "Création du projet", None))
        self.newCorpusButton.setText(_translate("newProjectWizard", "Créer un nouveau corpus", None))
        self.existingCorpusButton.setText(_translate("newProjectWizard", "Utiliser un corpus existant", None))
        self.tagsCorpusLabel.setText(_translate("newProjectWizard", "Corpus de tags :", None))
        self.page2Title.setText(_translate("newProjectWizard", "Paramétrage du corpus", None))
        self.corpusFilePathButton.setText(_translate("newProjectWizard", "...", None))
        self.corpusFileLabel.setText(_translate("newProjectWizard", "Fichier de corpus :", None))
        self.page3Title.setText(_translate("newProjectWizard", "Sélection du corpus", None))
        self.page4Title.setText(_translate("newProjectWizard", "Validation", None))
        self.congratulationLabel.setText(_translate("newProjectWizard", "Félications, votre projet va maintenant être créé. ", None))
        self.projectNameLabel.setText(_translate("newProjectWizard", "Nom du projet :", None))
        self.projectNameValue.setText(_translate("newProjectWizard", "TextLabel", None))
        self.projectFolderLabel.setText(_translate("newProjectWizard", "Répertoire :", None))
        self.projectFolderValue.setText(_translate("newProjectWizard", "TextLabel", None))
        self.corpusLabel.setText(_translate("newProjectWizard", "Corpus :", None))
        self.corpusValue.setText(_translate("newProjectWizard", "TextLabel", None))

