#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom import minidom

class CorpusManager:
    def createCorpus(self):
        corpus = minidom.Document()
        root = corpus.createElement('tags')
    
        corpus.appendChild(root)
    
        return corpus
    
    def getCorpus(self, xmlFile):
        corpus = minidom.parse(xmlFile)
    
        return corpus

