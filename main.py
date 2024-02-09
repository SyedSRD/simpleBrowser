# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:59:52 2019

@author: SYED
"""
from PyQt5 import QtCore, QtWidgets,QtGui
import home1,bookmark,history,database
import sys,csv,os,copy
import sqlite3 #DATABASE



class mainBRO(QtWidgets.QMainWindow,home1.Ui_MainWindow):
    def __init__(self,parent=None):
        try:
            super(mainBRO,self).__init__(parent)
            self.setupUi(self)
            self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
            
        
            self.form3=history()
            self.form4=bookmark()
            #self.form5=bookmarkDialog()
            
            

#==============================================================================
# signals
#==============================================================================
            self.btnGo.clicked.connect(self.webPageLoad)
            self.webView.urlChanged.connect(self.webPagedr)
            self.btnBMD.clicked.connect(self.webPageBM)
            self.btnBack.clicked.connect(self.webView.back)
            self.btnForward.clicked.connect(self.webView.forward)
            n=self.btn1.objectName()[3]
            self.btn1.clicked.connect(lambda :self.bmk(n))
            self.actionHistory.triggered.connect(self.loadHistory)
            self.actionBookMark.triggered.connect(self.loadBM)
            self.actionNew_Window.triggered.connect(self.newWin)
            self.actionQuit.triggered.connect(self.close)
            
            
        except Exception as e:
                print(e)
            
            
#==============================================================================
# slots
#==============================================================================
    
    def newWin(self):
        self.form8=mainBRO()
        self.form8.show()
        self.form8.setWindowTitle("NEW WINDOW")

    def webPageLoad(self):
        url =self.lineEdit.text()
        url1=copy.deepcopy(url)
        if url:
            self.webView.load(QtCore.QUrl(url))
            self.webView.show()
            database.menu('browserdb.db',str(url1),1)
            
        else:
            QtWidgets.QMessageBox.about(self, "ERROR", "The link field is empty plz specify a valid url")
            
    def webPagedr(self):
        url1=self.webView.url()
        url2=copy.deepcopy(url1.toString())
        self.lineEdit.setText(url1.toString())
        database.menu('browserdb.db',str(url2),1)
    
    def webPageBM(self):
        url3 =self.lineEdit.text()
        if url3=="":
            QtWidgets.QMessageBox.about(self, "ERROR", "The link field is empty plz specify a valid url")
        else:
            database.menu('browserdb.db',str(url3),2)
    def bmk(self,num):
        try:
            with sqlite3.connect('browserdb.db') as db:
                cursor = db.cursor()
                cursor.execute("SELECT bname FROM bookmark WHERE sno2=="+str(num)+";")
                urlb=cursor.fetchone()

                print(urlb)
            cursor.close()
            db.close()
            
            self.webView.load(QtCore.QUrl("http://www.google.com"))
            self.webView.show()
            self.webPagedr()
            
        except Exception as e:
            print(e)
        
    def loadHistory(self):
        try:
            with sqlite3.connect('browserdb.db') as db:
                cursor = db.cursor()
                cursor.execute("SELECT hname FROM history ;")
                tsklist=cursor.fetchall()
               # print(tsklist)
            cursor.close()
            db.close()
        
            self.form3.show()
            model = QtGui.QStandardItemModel()
            
           
            for task in tsklist:
                item = QtGui.QStandardItem(str(list(task)))
                
                model.appendRow(item)
            self.form3.listWHistory.setModel(model)    
        except Exception as e:
            print(e)
    def loadBM(self):
        try:
            with sqlite3.connect('browserdb.db') as db:
                cursor = db.cursor()
                cursor.execute("SELECT bname FROM bookmark ;")
                tsklist=cursor.fetchall()
               # print(tsklist)
            cursor.close()
            db.close()
        
            self.form4.show()
            model = QtGui.QStandardItemModel()
            
           
            for task in tsklist:
                item = QtGui.QStandardItem(str(list(task)))
                
                model.appendRow(item)
            self.form4.listWBM.setModel(model)    
        except Exception as e:
            print(e)
################################################################################
class bookmark(QtWidgets.QWidget,bookmark.Ui_Form):
    
    def __init__(self,parent=None):
        super(bookmark,self).__init__(parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.form7=mainBRO()
        self.listWBM.doubleClicked.connect(self.dirLink1)
        self.btnBClr.clicked.connect(self.clear)
        self.btnBClrAll.clicked.connect(self.clearAll)
        
    def clear(self):
        k=self.listWBM.currentIndex().data()[2:-2]
        try:
            with sqlite3.connect('browserdb.db') as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM bookmark WHERE bname = '"+k+"';")
                db.commit()
                cursor.execute("SELECT bname FROM bookmark ;")
                tsklist=cursor.fetchall()
            cursor.close()
            db.close()
            model = QtGui.QStandardItemModel()
            for task in tsklist:
                item = QtGui.QStandardItem(str(list(task)))
                model.appendRow(item)
            self.listWBM.setModel(model)
        except Exception as e:
                print(e) 
                
    def clearAll(self):
        
        try:
            with sqlite3.connect('browserdb.db') as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM bookmark ;")
                db.commit()
                cursor.execute("SELECT bname FROM bookmark ;")
                tsklist=cursor.fetchall()
            cursor.close()
            db.close()
            model = QtGui.QStandardItemModel()
            for task in tsklist:
                item = QtGui.QStandardItem(str(list(task)))
                model.appendRow(item)
            self.listWBM.setModel(model)
        except Exception as e:
                print(e)
                
    def dirLink1(self):
        try:
            data=self.listWBM.currentIndex().data()[2:-2]
            print(data)
            self.close()
            self.form7.lineEdit.setText(data)
            self.form7.webView.load(QtCore.QUrl(data))
            self.form7.webView.show()
            self.form7.webPagedr()
            self.form7.show()
        except Exception as e:
                print(e) 
                
                
##########################################################################################
##########################################################################################


class history(QtWidgets.QWidget,history.Ui_Form):
    
    def __init__(self,parent=None):
        super(history,self).__init__(parent)
        
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.setupUi(self)
        self.listWHistory.doubleClicked.connect(self.dirLink)
        
        self.btnClr.clicked.connect(self.clear)
        self.btnClrAll.clicked.connect(self.clearAll)
        
    def dirLink(self):
        try:
            self.form1=mainBRO()
            data=self.listWHistory.currentIndex().data()[2:-2]
            print(data)
            self.close()
            self.form1.lineEdit.setText(data)
            self.form1.webView.load(QtCore.QUrl(data))
            self.form1.webView.show()
            self.form1.webPagedr()
            self.form1.show()
        except Exception as e:
                print(e) 
        
    def clear(self):
        k=self.listWHistory.currentIndex().data()[2:-2]
        try:
            with sqlite3.connect('browserdb.db') as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM history WHERE hname = '"+k+"';")
                db.commit()
                cursor.execute("SELECT hname FROM history ;")
                tsklist=cursor.fetchall()
            cursor.close()
            db.close()
            model = QtGui.QStandardItemModel()
            for task in tsklist:
                item = QtGui.QStandardItem(str(list(task)))
                model.appendRow(item)
            self.listWHistory.setModel(model)
        except Exception as e:
                print(e) 
        
    def clearAll(self):
        
        try:
            with sqlite3.connect('browserdb.db') as db:
                cursor = db.cursor()
                cursor.execute("DELETE FROM history ;")
                db.commit()
                cursor.execute("SELECT hname FROM history ;")
                tsklist=cursor.fetchall()
            cursor.close()
            db.close()
            model = QtGui.QStandardItemModel()
            for task in tsklist:
                item = QtGui.QStandardItem(str(list(task)))
                model.appendRow(item)
            self.listWHistory.setModel(model)
        except Exception as e:
                print(e)
        
        
#################################################################################
################################################################################

            
app=QtCore.QCoreApplication.instance()
if app is None:
   app = QtWidgets.QApplication(sys.argv)
app.setStyle(QtWidgets.QStyleFactory.create('Fusion'))
form=mainBRO()
#form=mainD6('s')

form.show()

app.exec_()      