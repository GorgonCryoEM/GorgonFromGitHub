# Copyright (C) 2005-2008 Washington University in St Louis, Baylor College of Medicine.  All rights reserved
# Author:        Sasakthi S. Abeysinghe (sasakthi@gmail.com)
# Description:   A base class for dock widgets

# CVS Meta Information: 
#   $Source: /project/mm/cvs/graphics/ssa1/source/Gorgon/src_py/base_dock_widget.py,v $
#   $Revision: 1.4 $
#   $Date: 2009/12/24 21:53:49 $
#   $Author: ssa1 $
#   $State: Exp $
#
# History Log: 
#   $Log: base_dock_widget.py,v $
#   Revision 1.4  2009/12/24 21:53:49  ssa1
#   Giving back color control to the SSE Visualization options form when SSE Correspondence engine is not running (Bug ID: 58)
#
#   Revision 1.3  2009/12/24 19:37:36  ssa1
#   Refactoring child window behavior.. Using base classes to encapsulate common behavior
#
#   Revision 1.2  2009/12/24 07:25:07  ssa1
#   Refactoring child window behavior.. Using base classes to encapsulate common behavior
#
#   Revision 1.1  2009/12/24 05:09:30  ssa1
#   Refactoring child window behavior.. Using base classes to encapsulate common behavior
#

from PyQt4 import QtCore, QtGui
from base_dock import BaseDock

class BaseDockWidget(QtGui.QWidget):
    def __init__(self, main, title, hint, actionName, menuName, parentMenuName, allowedAreas, defaultArea, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.app = main
        self.defaultArea = defaultArea        
        self.createDisplayAction(title, hint, actionName)
        self.createDisplayMenu(menuName, parentMenuName)
        self.createDock(title, allowedAreas)        

    def createDock(self, title, allowedAreas):
        self.dock = BaseDock(self.tr(title), self.displayAct, self.app)
        self.dock.setAllowedAreas(allowedAreas)
        self.dock.setWidget(self)
        self.dock.close()  
        self.connect(self.dock, QtCore.SIGNAL("visibilityChanged (bool)"), self.dockVisibilityChanged)
   
    def createDisplayAction(self, title, hint, actionName):               
        self.displayAct = QtGui.QAction(self.tr(title + "..."), self)
        self.displayAct.setStatusTip(self.tr(hint))
        self.displayAct.setCheckable(True)
        self.displayAct.setChecked(False)
        self.connect(self.displayAct, QtCore.SIGNAL("triggered()"), self.loadWidget)
        self.app.actions.addAction(actionName,  self.displayAct)
  
    def createDisplayMenu(self, menuName, parentMenuName):
        self.app.menus.addAction(menuName, self.displayAct, parentMenuName)                                   
                
    def loadWidget(self):
        if(self.displayAct.isChecked()) :
            self.showWidget(True)
        else:
            self.showWidget(False)

    def showWidget(self, show):
        if(show):
            self.displayAct.setChecked(True)
            self.app.addDockWidget(self.defaultArea, self.dock)
            self.dock.show()
            self.bringToFront()
            
        else:
            self.displayAct.setChecked(False)
            self.app.removeDockWidget(self.dock)  
    
    def dockVisibilityChanged(self, visible):
        pass
        
    def bringToFront(self):
        self.dock.raise_()
    
    def closeEvent(self, event):
        QtGui.QWidget.closeEvent(self, event)
        self.displayAct.setChecked(False)
        
    def show(self):
        QtGui.QWidget.show(self)
        self.displayAct.setChecked(True)
        
    
    
    
    
