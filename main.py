import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import os 

# GUI FILE
from app_modules import *



class MainWindow(QMainWindow):
    inputfile = "ENTREE.txt";
    outputfile = "SORTIE.txt";
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        ## PRINT ==> SYSTEM
        # print('System: ' + platform.system())
        # print('Version: ' +platform.release())

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Tp Compil - Meghar - Tiouti')
        ## ==> END ##
        self.ui.lineEdit.setText(self.inputfile)
        self.ui.lineEdit_3.setText(self.outputfile)

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1000, 720)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "Accueil", "btn_acc", "url(:/16x16/icons/16x16/cil-lightbulb.png)", True)
        UIFunctions.addNewMenu(self, "Texte", "btn_home", "url(:/16x16/icons/16x16/cil-justify-left.png)", True)
        UIFunctions.addNewMenu(self, "Fichiers", "btn_new_user", "url(:/16x16/icons/16x16/cil-description.png)", True)
        # UIFunctions.addNewMenu(self, "Custom Widgets", "btn_widgets", "url(:/16x16/icons/16x16/cil-equalizer.png)", False)
        ## ==> END ##

        # START MENU => SELECTION
        # UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        # self.ui.stackedWidget.setCurrentWidget(self.ui.page_text)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        # UIFunctions.userIcon(self, "WM", "", True)
        ## ==> END ##


        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        # self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    @pyqtSlot()
    def decompresserFile(self):
        os.system("flex Reverse.l")
        os.system("gcc lex.yy.c")
        os.system("a {} {}".format(self.inputfile,self.outputfile))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Fichier decompressé avec succès")
        msg.setWindowTitle("Succès")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
    @pyqtSlot()
    def compresserFile(self):
        os.system("flex tp.l")
        os.system("gcc lex.yy.c")
        os.system("a {} {}".format(self.inputfile,self.outputfile))
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Fichier compressé avec succès")
        msg.setWindowTitle("Succès")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()
    @pyqtSlot()
    def compresserText(self):
        os.system("flex tptext.l")
        os.system("gcc lex.yy.c")
        self.ui.lineEdit_6.setText(os.popen("a {}".format(self.ui.lineEdit_7.text())).read())
    @pyqtSlot()
    def decompresserText(self):
        os.system("flex Reversetxt.l")
        os.system("gcc lex.yy.c")
        self.ui.lineEdit_6.setText(os.popen("a {}".format(self.ui.lineEdit_7.text())).read())
    @pyqtSlot()
    def getfile(self,type):
        fname = QFileDialog.getOpenFileName(None, 'Open file', 'c:\\',"Text files (*.txt)")
        if (type == "input") : 
            self.inputfile = fname[0] ;
            self.ui.lineEdit.setText(fname[0])
        elif(type=="output") : 
            self.outputfile = fname[0] ;
            self.ui.lineEdit_3.setText(fname[0])
        
        return fname
    
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        self.ui.pushButton.clicked.connect(lambda : self.getfile("input"))
        self.ui.pushButton_5.clicked.connect(lambda : self.getfile("output"))

        self.ui.pushButton_4.clicked.connect(lambda :self.compresserFile())
        self.ui.pushButton_3.clicked.connect(lambda :self.decompresserFile())


        self.ui.pushButton_6.clicked.connect(lambda :self.compresserText())
        self.ui.pushButton_7.clicked.connect(lambda :self.decompresserText())

        # PAGE Text
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_text)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Texte")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE FILE
        if btnWidget.objectName() == "btn_new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_file)
            UIFunctions.resetStyle(self, "btn_new_user")
            UIFunctions.labelPage(self, "Fichiers")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE acc
        if btnWidget.objectName() == "btn_acc":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_acc")
            UIFunctions.labelPage(self, "Accueil")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    
        


    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
