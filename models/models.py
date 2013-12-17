#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
from controllers.mainwindow import project

database = SqliteDatabase(project['database'])

class BaseModel(Model):
    class Meta:
        database = database

class Meta(BaseModel):
    projectName = CharField(255, unique=True)
    
class Video(BaseModel):
    title = CharField(255, unique=True)
    path = CharField(255, unique=True)
        
class Sequence(BaseModel):
    debut = DoubleField()
    fin = DoubleField()
    video = ForeignKeyField(Video, related_name='sequences')
        
class Tag(BaseModel):
    tag = CharField(50)
