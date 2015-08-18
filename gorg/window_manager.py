# Copyright (C) 2005-2008 Washington University in St Louis, Baylor College of Medicine.  All rights reserved
# Author:        Sasakthi S. Abeysinghe (sasakthi@gmail.com)
# Description:   A widget that manages all the windows of the main form. 


from PyQt4 import QtGui, QtCore
# from help_menus import HelpMenus
from camera import Camera
from volume_viewer import VolumeViewer
# from skeleton_viewer import SkeletonViewer
# from sse_viewer import SSEViewer
# from calpha_viewer import CAlphaViewer
# from calpha_reference_viewer import CAlphaReferenceViewer
import datetime
# from session_manager import SessionManager

class WindowManager(QtGui.QWidget):
    
    def __init__(self, main, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.app = main
        self.createUI()

    def createUI(self):
        self.createActions()
        self.createMenus()
        self.createChildWindows()        
        
    def createChildWindows(self):
#         self.helpMenus = HelpMenus(self.app)
        self.volumeViewer = VolumeViewer(self.app)
#         self.skeletonViewer = SkeletonViewer(self.app)
#         self.sseViewer = SSEViewer(self.app)
#         self.calphaViewer = CAlphaViewer(self.app)
#         self.calphaReference = CAlphaReferenceViewer(self.app)
#         self.mainCamera = Camera([self.calphaViewer, self.calphaReference, self.sseViewer, self.skeletonViewer, self.volumeViewer], self.app)
        self.mainCamera = Camera([self.volumeViewer], self.app)
        self.app.mainCamera = self.mainCamera   
        self.app.setCentralWidget(self.mainCamera)
        
    def createActions(self):
        self.saveSessionAct = QtGui.QAction(self.tr("Sessio&n..."), self)
        self.saveSessionAct.setStatusTip(self.tr("Save the current session"))
        self.connect(self.saveSessionAct, QtCore.SIGNAL("triggered()"), self.saveSession)
        self.app.actions.addAction("save_Session", self.saveSessionAct)  
        
        self.loadSessionAct = QtGui.QAction(self.tr("Sessio&n..."), self)
        self.loadSessionAct.setStatusTip(self.tr("Load a session from file"))
        self.connect(self.loadSessionAct, QtCore.SIGNAL("triggered()"), self.loadSession)
        self.app.actions.addAction("load_Session", self.loadSessionAct)          

        self.closeSessionAct = QtGui.QAction(self.tr("Sessio&n..."), self)
        self.closeSessionAct.setStatusTip(self.tr("Close session"))
        self.connect(self.closeSessionAct, QtCore.SIGNAL("triggered()"), self.closeSession)
        self.app.actions.addAction("close_Session", self.closeSessionAct)          
            
    def createMenus(self):
        self.app.menus.addAction("file-save-session", self.app.actions.getAction("save_Session"), "file-save")
        self.app.menus.getMenu("file-save").addSeparator()
        self.app.menus.addAction("file-open-session", self.app.actions.getAction("load_Session"), "file-open")
        self.app.menus.getMenu("file-open").addSeparator()
        self.app.menus.addAction("file-close-session", self.app.actions.getAction("close_Session"), "file-close")
        self.app.menus.getMenu("file-close").addSeparator()

        
    def closeSession(self):
        if (QtGui.QMessageBox.warning(self, self.tr("Are you sure?"), self.tr("You are about to close the session.  All unsaved data will be lost!"), QtGui.QMessageBox.Yes, QtGui.QMessageBox.Cancel) == QtGui.QMessageBox.Yes):
            if (self.volumeViewer.loaded) :
                self.volumeViewer.unloadData()
            if (self.skeletonViewer.loaded) :
                self.skeletonViewer.unloadData()
            if (self.sseViewer.loaded) :
                self.sseViewer.unloadData()
            if (self.calphaViewer.loaded) :
                self.calphaViewer.unloadData()
            if (self.calphaReference.loaded) :
                self.calphaReference.unloadData()
