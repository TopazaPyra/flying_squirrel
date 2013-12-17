#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.dom import minidom

class TagsManager:
    def __init__(self, corpus):
        self.corpus = corpus
    
    def addTag(self, tag):
        root = self.corpus.documentElement
    
        tagNode = self.corpus.createElement('tag')
        tagValue = self.corpus.createTextNode(tag)
        tagNode.appendChild(tagValue)
        root.appendChild(tagNode)
    
    def removeTag(self, tag):
        root = self.corpus.documentElement
    
        removedTag = root.removeChild(tag)
        removedTag.unlink
    
    def getTags(self):
        root = self.corpus.documentElement
    
        return root.getElementsByTagName('tag')
