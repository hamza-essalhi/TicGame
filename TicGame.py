 #################################################
#     Copyrights hamza essalhi                  #
################################################


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.WinPoss=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
        self.Player1_score=0
        self.Player2_score=0
        self.Playerturn=2
        self.GetBtn=[]
        self.Player1Btn=[]
        self.Player2Btn=[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 634)
        MainWindow.setMinimumSize(QtCore.QSize(0, 634))
        MainWindow.setMaximumSize(QtCore.QSize(660, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/tic-tac-toe.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{\n"
        "background-color:#56BBF1\n"
        "}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget{\n"
        "background-color:#56BBF1\n"
        "}\n"
        "\n"
        "QPushButton,QLabel{\n"
        "background-color:#5EE6EB;\n"
        "border:none;\n"
        "border-radius: 8px;\n"
        "}\n"
        "#TiCFram{\n"
        "border:2px solid #4D77FF;\n"
        "border-radius: 8px;\n"
        "}\n"
        "\n"
        "#MessageLabel,#Player1,#Player2{\n"
        "padding-left:3px\n"
        "}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.TiCFram = QtWidgets.QFrame(self.centralwidget)
        self.TiCFram.setMinimumSize(QtCore.QSize(400, 350))
        self.TiCFram.setMaximumSize(QtCore.QSize(400, 350))
        self.TiCFram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.TiCFram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.TiCFram.setObjectName("TiCFram")
        self.gridLayout = QtWidgets.QGridLayout(self.TiCFram)
        self.gridLayout.setObjectName("gridLayout")
        self.Btn8 = QtWidgets.QPushButton(self.TiCFram,clicked=lambda:self.XOfunc(self.Btn8))
        self.Btn8.setMinimumSize(QtCore.QSize(100, 100))
        self.Btn8.setObjectName("Btn8")
        self.gridLayout.addWidget(self.Btn8, 2, 1, 1, 1)
        self.Btn7 = QtWidgets.QPushButton(self.TiCFram,clicked=lambda:self.XOfunc(self.Btn7))
        self.Btn7.setMinimumSize(QtCore.QSize(100, 100))
        self.Btn7.setObjectName("Btn7")
        self.gridLayout.addWidget(self.Btn7, 2, 0, 1, 1)
        self.Btn3 = QtWidgets.QPushButton(self.TiCFram,clicked=lambda:self.XOfunc(self.Btn3))
        self.Btn3.setMinimumSize(QtCore.QSize(100, 100))
        self.Btn3.setObjectName("Btn3")
        self.gridLayout.addWidget(self.Btn3, 0, 2, 1, 1)
        self.Btn1 = QtWidgets.QPushButton(self.TiCFram,clicked=lambda:self.XOfunc(self.Btn1))
        self.Btn1.setMinimumSize(QtCore.QSize(100, 100))
        self.Btn1.setObjectName("Btn1")
        self.gridLayout.addWidget(self.Btn1, 0, 0, 1, 1)
        self.Btn6 = QtWidgets.QPushButton(self.TiCFram,clicked=lambda:self.XOfunc(self.Btn6))
        self.Btn6.setMinimumSize(QtCore.QSize(100, 100))
        self.Btn6.setObjectName("Btn6")
        self.gridLayout.addWidget(self.Btn6, 1, 2, 1, 1)
        self.Btn4 = QtWidgets.QPushButton(self.TiCFram,clicked=lambda:self.XOfunc(self.Btn4))
        self.Btn4.setMinimumSize(QtCore.QSize(100, 100))
        self.Btn4.setObjectName("Btn4")
        self.gridLayout.addWidget(self.Btn4, 1, 0, 1, 1)
        self.Btn9 = QtWidgets.QPushButton(self.TiCFram,clicked=lambda:self.XOfunc(self.Btn9))
        self.Btn9.setMinimumSize(QtCore.QSize(100, 100))
        self.Btn9.setObjectName("Btn9")
        self.gridLayout.addWidget(self.Btn9, 2, 2, 1, 1)
        self.Btn5 = QtWidgets.QPushButton(self.TiCFram,clicked=lambda:self.XOfunc(self.Btn5))
        self.Btn5.setMinimumSize(QtCore.QSize(100, 100))
        self.Btn5.setObjectName("Btn5")
        self.gridLayout.addWidget(self.Btn5, 1, 1, 1, 1)
        self.Btn2 = QtWidgets.QPushButton(self.TiCFram,clicked=lambda:self.XOfunc(self.Btn2))
        self.Btn2.setMinimumSize(QtCore.QSize(100, 100))
        self.Btn2.setObjectName("Btn2")
        self.gridLayout.addWidget(self.Btn2, 0, 1, 1, 1)
        self.gridLayout_2.addWidget(self.TiCFram, 1, 0, 1, 1)
        self.MessageLabel = QtWidgets.QLabel(self.centralwidget)
        self.MessageLabel.setMinimumSize(QtCore.QSize(0, 45))
        self.MessageLabel.setMaximumSize(QtCore.QSize(16777215, 50))
        self.MessageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.MessageLabel.setObjectName("MessageLabel")
        self.gridLayout_2.addWidget(self.MessageLabel, 2, 0, 1, 1)
        self.Player2 = QtWidgets.QLabel(self.centralwidget)
        self.Player2.setMinimumSize(QtCore.QSize(0, 45))
        self.Player2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Player2.setObjectName("Player2")
        self.gridLayout_2.addWidget(self.Player2, 4, 0, 1, 1)
        self.Player1 = QtWidgets.QLabel(self.centralwidget)
        self.Player1.setMinimumSize(QtCore.QSize(0, 45))
        self.Player1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.Player1.setObjectName("Player1")
        self.gridLayout_2.addWidget(self.Player1, 3, 0, 1, 1)
        self.GameTitle = QtWidgets.QLabel(self.centralwidget)
        self.GameTitle.setMinimumSize(QtCore.QSize(0, 60))
        self.GameTitle.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.GameTitle.setFont(font)
        self.GameTitle.setTextFormat(QtCore.Qt.MarkdownText)
        self.GameTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.GameTitle.setObjectName("GameTitle")
        self.gridLayout_2.addWidget(self.GameTitle, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.MessageLabel.setText("Let's play")
        #init of score p1,p2
        self.Player1.setText(self.Player1.text()+str(self.Player1_score))
        self.Player2.setText(self.Player2.text()+str(self.Player2_score))
    #game funcation  
    def XOfunc(self,btn):
        #buttons for algo switch
        btns=[self.Btn1,self.Btn2,self.Btn3,
            self.Btn4,self.Btn5,self.Btn6,
            self.Btn7,self.Btn8,self.Btn9
            ]
        #counter
        self.Playerturn+=1

        #algo to add to vrf the clicked buttons
        if btn not in self.GetBtn:
            # if the buttons not clicked,adding to  get buttons list
            self.GetBtn.append(btn)
            # conditon to switch the player 1 for player 1, 0 for player 2 
            if self.Playerturn%2==1:
                #change button srt and color green lock at ColorBg function if you went to change colors !!
                btn.setText('X')
                self.BgColor(btn,setIt='p1')
                #switch message to player 2
                self.MessageLabel.setText('Player 2 turn')
                #geting index from btns list and adding the int index plus 1 to vrf winning possibilities
                self.Player1Btn.append(int(btns.index(btn)+1))
                #condution to vrf if player 1 list = 3 notes that win can be if len = 3
                if len(self.Player1Btn)==3:
                    #geting winnig possb 
                    for i in self.WinPoss:
                        # vrf if there is a poss in player 1 list 
                        if sorted(self.Player1Btn)==(i):
                            #change scr value
                            self.Player1_score+=1
                            #disp value 
                            self.Player1.setText('Player 1 :'+str(self.Player1_score))
                            #massge that player 1 win
                            self.MessageLabel.setText('Player 1 win ')
                            #resatarting game 
                            for i in self.GetBtn:
                                self.BgColor(i,setIt='clear')
                            self.restart()
                            
            elif self.Playerturn%2==0:
                #change button srt and color green lock at ColorBg function if you went to change colors !!
                btn.setText('O')
                self.BgColor(btn,setIt='p2')
                #switch message to player 1
                self.MessageLabel.setText('Player 1 turn')
                #geting index from btns list and adding the int index plus 1 to vrf winning possibilities
                self.Player2Btn.append(int(btns.index(btn)+1))
                #condution to vrf if player 2 list = 3 notes that win can be if len = 3
                if len(self.Player2Btn)==3:
                    #geting winnig possb 
                    for i in self.WinPoss:
                        # vrf if there is a poss in player 1 list 
                        if sorted(self.Player2Btn)==(i):
                            #change scr value
                            self.Player2_score+=1
                            #disp value 
                            self.Player2.setText('Player 2 :'+str(self.Player2_score))
                            #massge that player 1 win
                            self.MessageLabel.setText('Player 2 win ')
                            #resatarting game 
                            for i in self.GetBtn:
                                self.BgColor(i,setIt='clear')
                            self.restart()
                           
            #if there is no winer notes len = 9
            if len(self.GetBtn)==9:
                self.MessageLabel.setText('Draw')
                for i in self.GetBtn:
                    self.BgColor(i,setIt='clear')
                self.restart()
            
    # bg and color change function you cane setup your bg color if u wt
    def BgColor(self,btn,setIt):
        if setIt=='p1':
            btn.setStyleSheet("background-color:#00C897;font-size:40px\n")
        elif setIt=='clear':
            btn.setStyleSheet("background-color:#5EE6EB\n")
            btn.setText('')
        else:
             btn.setStyleSheet("background-color:#FFD32D;font-size:40px\n")
    #restart function
    def restart(self):
        self.Playerturn=2
        self.GetBtn=[]
        self.Player1Btn=[]
        self.Player2Btn=[]



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "tic tac toe"))
        #Buttons titles
        self.Btn1.setText(_translate("MainWindow", ""))
        self.Btn2.setText(_translate("MainWindow", ""))
        self.Btn3.setText(_translate("MainWindow", ""))
        self.Btn4.setText(_translate("MainWindow", ""))
        self.Btn5.setText(_translate("MainWindow", ""))
        self.Btn6.setText(_translate("MainWindow", ""))
        self.Btn7.setText(_translate("MainWindow", ""))
        self.Btn8.setText(_translate("MainWindow", ""))
        self.Btn9.setText(_translate("MainWindow", ""))
        self.MessageLabel.setText(_translate("MainWindow", "Message label "))
        self.Player2.setText(_translate("MainWindow", "Player 2 :"))
        self.Player1.setText(_translate("MainWindow", "Player 1 : "))
        self.GameTitle.setText(_translate("MainWindow", "tic tac toe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
