from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from qrtools import QR
from PIL import ImageGrab
import os,sys
import time

__author__ = "BaconCondensate"
__email__ = "-"
__version__ = "0.1"

class potato:
    userID = ""
    userCID = 0
    userCN = 0
    userCA = 0
    userDone = ""
    resp = "https://0.0.0.0/"
    qrDecoded = ""


def resource_path(relative_path):
  if hasattr(sys, '_MEIPASS'):
      return os.path.join(sys._MEIPASS, relative_path)
  return os.path.join(os.path.abspath('.'), relative_path)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QtCore.QSize(640, 480))
        MainWindow.setMaximumSize(QtCore.QSize(640, 480))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 0)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.userID_i = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userID_i.setMaxLength(11)
        self.userID_i.setObjectName("userID_i")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.userID_i)
        self.userID_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userID_b.sizePolicy().hasHeightForWidth())
        self.userID_b.setSizePolicy(sizePolicy)
        self.userID_b.setObjectName("userID_b")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userID_b)
        self.userCN_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userCN_b.sizePolicy().hasHeightForWidth())
        self.userCN_b.setSizePolicy(sizePolicy)
        self.userCN_b.setObjectName("userCN_b")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.userCN_b)
        self.userCID_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userCID_b.sizePolicy().hasHeightForWidth())
        self.userCID_b.setSizePolicy(sizePolicy)
        self.userCID_b.setObjectName("userCID_b")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.userCID_b)
        self.userCN_i = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userCN_i.setMaxLength(4)
        self.userCN_i.setObjectName("userCN_i")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.userCN_i)
        self.userCID_i = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userCID_i.setMaxLength(6)
        self.userCID_i.setObjectName("userCID_i")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.userCID_i)
        self.userCA_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userCA_b.sizePolicy().hasHeightForWidth())
        self.userCA_b.setSizePolicy(sizePolicy)
        self.userCA_b.setObjectName("userCA_b")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.userCA_b)
        self.userCA_i = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.userCA_i.setMaxLength(4)
        self.userCA_i.setObjectName("userCA_i")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.userCA_i)
        self.verticalLayout.addLayout(self.formLayout)
        self.userALL = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.userALL.setObjectName("userALL")
        self.verticalLayout.addWidget(self.userALL)
        self.textBrowser = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        self.textBrowser.setAcceptDrops(False)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.submit = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.submit.setObjectName("submit")
        self.gridLayout.addWidget(self.submit, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.qr_get_b = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.qr_get_b.setObjectName("qr_get_b")
        self.horizontalLayout.addWidget(self.qr_get_b)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.imginput = QtWidgets.QLabel(self.gridLayoutWidget)
        self.imginput.setMaximumSize(QtCore.QSize(300, 300))
        self.imginput.setAcceptDrops(True)
        self.imginput.setFrameShape(QtWidgets.QFrame.Box)
        self.imginput.setFrameShadow(QtWidgets.QFrame.Plain)
        self.imginput.setText("")
        self.imginput.setPixmap(QtGui.QPixmap(resource_path("blank.png")))
        self.imginput.setScaledContents(False)
        self.imginput.setAlignment(QtCore.Qt.AlignCenter)
        self.imginput.setObjectName("imginput")
        self.verticalLayout_2.addWidget(self.imginput)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.link_get = QtWidgets.QTextBrowser(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.link_get.sizePolicy().hasHeightForWidth())
        self.link_get.setSizePolicy(sizePolicy)
        self.link_get.setMaximumSize(QtCore.QSize(16777215, 60))
        self.link_get.setObjectName("link_get")
        self.gridLayout.addWidget(self.link_get, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #USER
        self.userID_b.clicked
        self.userID_b.clicked.connect(self.set_userID)  
        self.userID_b.clicked.connect(self.refresh)

        self.userCID_b.clicked.connect(self.set_userCID)  
        self.userCID_b.clicked.connect(self.refresh)      

        self.userCN_b.clicked.connect(self.set_userCN)  
        self.userCN_b.clicked.connect(self.refresh)

        self.userCA_b.clicked.connect(self.set_userCA)  
        self.userCA_b.clicked.connect(self.refresh) 

        self.userALL.clicked.connect(self.set_ALL)
        self.userALL.clicked.connect(self.refresh)

        self.submit.clicked.connect(self.submit_att)

        self.qr_get_b.clicked.connect(self.qrgrab)
        self.qr_get_b.clicked.connect(self.refresh)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Condensed Bacon Attendance Tool (Not for redistribution)"))
        self.userID_b.setText(_translate("MainWindow", "Set UserID"))
        self.userCN_b.setText(_translate("MainWindow", "Set Class #"))
        self.userCID_b.setText(_translate("MainWindow", "Set Class ID"))
        self.userCA_b.setText(_translate("MainWindow", "Set Class Att"))
        self.userALL.setText(_translate("MainWindow", "Set All"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.qr_get_b.setText(_translate("MainWindow", "Get QR"))




#USER
    def refresh(self):
        potato.userDone = (f"https://myatma.atmajaya.ac.id/PSIGW/RESTListeningConnector/PSFT_CS/A_SCH_QR_ABS.v1/CRSE_ID/{potato.userCID}/CLASS_NBR/{potato.userCN}/ATTEND_TMPLT_NBR/{potato.userCA}/OPRID/{potato.userID}")
        self.textBrowser.setText(potato.userDone)

    def set_userID(self):
        potato.userID = self.userID_i.text()
    def set_userCID(self):
        potato.userCID = self.userCID_i.text()
    def set_userCN(self):
        potato.userCN = self.userCN_i.text()
    def set_userCA(self):
        potato.userCA = self.userCA_i.text()
    def set_ALL(self):
        potato.userID = self.userID_i.text()
        potato.userCID = self.userCID_i.text()
        potato.userCN = self.userCN_i.text()
        potato.userCA = self.userCA_i.text()
    def submit_att(self):
        response = requests.get(potato.userDone,verify=False, timeout=8)
        print(response.text)
        potato.resp = response.text
        self.link_get.setText(potato.resp)
    def qrgrab(self):
        _translate = QtCore.QCoreApplication.translate
        
        im = ImageGrab.grab()
        im.save('tmp.png')
        my_QR = QR(filename='tmp.png')
        my_QR.decode()
        potato.qrDecoded = my_QR.data

        self.userCID_i.setText(_translate("MainWindow",potato.qrDecoded[91:97]))
        potato.userCID = self.userCID_i.text()

        self.userCN_i.setText(_translate("MainWindow",potato.qrDecoded[108:112]))
        potato.userCN = self.userCN_i.text()

        self.userCA_i.setText(_translate("MainWindow",potato.qrDecoded[130:134]))
        potato.userCA = self.userCA_i.text()
        #self.imginput.setPixmap(QtGui.QPixmap("tmp.png"))
        os.remove("tmp.png")

    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
