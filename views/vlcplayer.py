#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
import user
#import vlc
from libs import vlc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VLCPlayer(object):
    def createPlayer(self):
        self.instance = vlc.Instance()
        self.mediaplayer = self.instance.media_player_new()

    def setupUi(self, VLCPlayer):
        VLCPlayer.setObjectName(_fromUtf8("VLCPlayer"))
        self.positionslider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.positionslider.setToolTip("Position")
        self.positionslider.setMaximum(1000)
        
        self.hbuttonbox = QtGui.QHBoxLayout()
        self.playbutton = QtGui.QPushButton(VLCPlayer)
        self.playbutton.setObjectName(_fromUtf8("Play"))
        self.hbuttonbox.addWidget(self.playbutton)
        
        self.stopbutton = QtGui.QPushButton(VLCPlayer)
        self.stopbutton.setObjectName(_fromUtf8("Stop"))
        self.hbuttonbox.addWidget(self.stopbutton)
        
        self.hbuttonbox.addStretch(1)
        self.volumeslider = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        self.volumeslider.setMaximum(100)
        self.volumeslider.setToolTip("Volume")
        self.hbuttonbox.addWidget(self.volumeslider)
        
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(200)
        
        self.videoframe = QtGui.QFrame()
        self.vboxlayout = QtGui.QVBoxLayout(VLCPlayer)
        self.vboxlayout.addWidget(self.videoframe)
        self.vboxlayout.addWidget(self.positionslider)
        self.vboxlayout.addLayout(self.hbuttonbox)
        
        self.retranslateUi(VLCPlayer)
        QtCore.QMetaObject.connectSlotsByName(VLCPlayer)
        
    def retranslateUi(self, VLCPlayer):
        self.playbutton.setText(QtGui.QApplication.translate("VLCPlayer", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.stopbutton.setText(QtGui.QApplication.translate("VLCPlayer", "Stop", None, QtGui.QApplication.UnicodeUTF8))
    
    def connectActions(self):
        self.connect(self.positionslider, QtCore.SIGNAL("sliderMoved(int)"), self.setPosition)

        self.playbutton.clicked.connect(self.PlayPause)
        self.stopbutton.clicked.connect(self.Stop)

        self.volumeslider.setValue(self.mediaplayer.audio_get_volume())
        
        self.connect(self.volumeslider, QtCore.SIGNAL("valueChanged(int)"), self.setVolume)
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.updateUI)

    def PlayPause(self):
        """Toggle play/pause status
        """
        if self.mediaplayer.is_playing():
            self.mediaplayer.pause()
            self.playbutton.setText("Play")
            self.isPaused = True
        else:
            if self.mediaplayer.play() == -1:
                self.OpenFile()
                return
            self.mediaplayer.play()
            self.playbutton.setText("Pause")
            self.timer.start()
            self.isPaused = False

    def Stop(self):
        """Stop player
        """
        self.mediaplayer.stop()
        self.playbutton.setText("Play")

    def OpenFile(self, filename=None):
        """Open a media file in a MediaPlayer
        """
        if filename is None:
            filename = QtGui.QFileDialog.getOpenFileName(self, "Open File", user.home)
        if not filename:
            return

        # create the media
        self.media = self.instance.media_new(unicode(filename))
        # put the media in the media player
        self.mediaplayer.set_media(self.media)

        # parse the metadata of the file
        self.media.parse()

        # the media player has to be 'connected' to the QFrame
        # (otherwise a video would be displayed in it's own window)
        # this is platform specific!
        # you have to give the id of the QFrame (or similar object) to
        # vlc, different platforms have different functions for this
        if sys.platform == "linux2": # for Linux using the X Server
            self.mediaplayer.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32": # for Windows
            self.mediaplayer.set_hwnd(self.videoframe.winId())
        elif sys.platform == "darwin": # for MacOS
            self.mediaplayer.set_agl(self.videoframe.windId())
        self.PlayPause()

    def setVolume(self, Volume):
        """Set the volume"""
        self.mediaplayer.audio_set_volume(Volume)

    def setPosition(self, position):
        """Set the position"""
        # setting the position to where the slider was dragged
        self.mediaplayer.set_position(position / 1000.0)
        # the vlc MediaPlayer needs a float value between 0 and 1, Qt
        # uses integer variables, so you need a factor; the higher the
        # factor, the more precise are the results
        # (1000 should be enough)

    def updateUI(self):
        """updates the user interface"""
        # setting the slider to the desired position
        self.positionslider.setValue(self.mediaplayer.get_position() * 1000)

        if not self.mediaplayer.is_playing():
            # no need to call this function if nothing is played
            self.timer.stop()
            if not self.isPaused:
                # after the video finished, the play button stills shows
                # "Pause", not the desired behavior of a media player
                # this will fix it
                self.Stop()
