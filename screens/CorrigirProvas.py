from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 475)
        MainWindow.setMinimumSize(QtCore.QSize(551, 475))
        MainWindow.setMaximumSize(QtCore.QSize(551, 475))
        MainWindow.setSizeIncrement(QtCore.QSize(551, 475))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_corrigirprova = QtWidgets.QFrame(self.centralwidget)
        self.frame_corrigirprova.setGeometry(QtCore.QRect(0, 0, 551, 91))
        self.frame_corrigirprova.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_corrigirprova.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_corrigirprova.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_corrigirprova.setObjectName("frame_corrigirprova")
        self.label_barrabosch = QtWidgets.QLabel(self.frame_corrigirprova)
        self.label_barrabosch.setGeometry(QtCore.QRect(0, 0, 551, 16))
        self.label_barrabosch.setText("")
        self.label_barrabosch.setPixmap(QtGui.QPixmap("Bosch-Supergraphic.svg"))
        self.label_barrabosch.setScaledContents(True)
        self.label_barrabosch.setObjectName("label_barrabosch")
        self.label_logobosch = QtWidgets.QLabel(self.frame_corrigirprova)
        self.label_logobosch.setGeometry(QtCore.QRect(0, 20, 171, 71))
        self.label_logobosch.setText("")
        self.label_logobosch.setPixmap(QtGui.QPixmap("Bosch_symbol_logo_black_red.png"))
        self.label_logobosch.setScaledContents(True)
        self.label_logobosch.setObjectName("label_logobosch")
        self.label_escritacorrecao = QtWidgets.QLabel(self.frame_corrigirprova)
        self.label_escritacorrecao.setGeometry(QtCore.QRect(63, 70, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(10)
        self.label_escritacorrecao.setFont(font)
        self.label_escritacorrecao.setObjectName("label_escritacorrecao")
        self.frame_corrigirprova_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_corrigirprova_2.setGeometry(QtCore.QRect(0, 90, 551, 391))
        self.frame_corrigirprova_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_corrigirprova_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_corrigirprova_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_corrigirprova_2.setObjectName("frame_corrigirprova_2")
        self.label_logotestquest = QtWidgets.QLabel(self.frame_corrigirprova_2)
        self.label_logotestquest.setGeometry(QtCore.QRect(110, 26, 321, 81))
        self.label_logotestquest.setText("")
        self.label_logotestquest.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_logotestquest.setScaledContents(True)
        self.label_logotestquest.setObjectName("label_logotestquest")
        self.comboBox_Corrigirprova = QtWidgets.QComboBox(self.frame_corrigirprova_2)
        self.comboBox_Corrigirprova.setGeometry(QtCore.QRect(180, 126, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_Corrigirprova.setFont(font)
        self.comboBox_Corrigirprova.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.comboBox_Corrigirprova.setObjectName("comboBox_Corrigirprova")
        self.comboBox_Corrigirprova.addItem("")
        self.lineEdit_CaminhoGabarito = QtWidgets.QLineEdit(self.frame_corrigirprova_2)
        self.lineEdit_CaminhoGabarito.setGeometry(QtCore.QRect(180, 193, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        self.lineEdit_CaminhoGabarito.setFont(font)
        self.lineEdit_CaminhoGabarito.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.lineEdit_CaminhoGabarito.setObjectName("lineEdit_CaminhoGabarito")
        self.label_caminhoGabarito = QtWidgets.QLabel(self.frame_corrigirprova_2)
        self.label_caminhoGabarito.setGeometry(QtCore.QRect(212, 176, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_caminhoGabarito.setFont(font)
        self.label_caminhoGabarito.setObjectName("label_caminhoGabarito")
        self.label_caminhoPastasProvas = QtWidgets.QLabel(self.frame_corrigirprova_2)
        self.label_caminhoPastasProvas.setGeometry(QtCore.QRect(195, 231, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_caminhoPastasProvas.setFont(font)
        self.label_caminhoPastasProvas.setObjectName("label_caminhoPastasProvas")
        self.lineEdit_CaminhoPastas_Provas = QtWidgets.QLineEdit(self.frame_corrigirprova_2)
        self.lineEdit_CaminhoPastas_Provas.setGeometry(QtCore.QRect(180, 249, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        self.lineEdit_CaminhoPastas_Provas.setFont(font)
        self.lineEdit_CaminhoPastas_Provas.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.lineEdit_CaminhoPastas_Provas.setObjectName("lineEdit_CaminhoPastas_Provas")
        self.botaoGerarCorrigirprovas = QtWidgets.QPushButton(self.frame_corrigirprova_2)
        self.botaoGerarCorrigirprovas.setGeometry(QtCore.QRect(220, 293, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.botaoGerarCorrigirprovas.setFont(font)
        self.botaoGerarCorrigirprovas.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid Grey;\n"
"border-radius: 3px;")
        self.botaoGerarCorrigirprovas.setObjectName("botaoGerarCorrigirprovas")
        self.label = QtWidgets.QLabel(self.frame_corrigirprova_2)
        self.label.setGeometry(QtCore.QRect(0, 367, 551, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Bosch-Supergraphic.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.botaoGerarCorrigirprovas.clicked.connect(self.corrigir)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_escritacorrecao.setText(_translate("MainWindow", "Corrigir Provas"))
        self.comboBox_Corrigirprova.setItemText(0, _translate("MainWindow", "Selecionar Processo Seletivo"))

        # Inicia a combobox com informações diretas da API ------------------------------------------------------
        API = 'http://127.0.0.1:8000/processos/'
        processos = requests.get(API).json()
        v = 1
        for p in processos:
            self.comboBox_Corrigirprova.addItem("")
            self.comboBox_Corrigirprova.setItemText(v, _translate("MainWindow", p['titulo']))
            v += 1
        # -------------------------------------------------------------------------------------------------------

        self.label_caminhoGabarito.setText(_translate("MainWindow", "Caminho Gabarito:"))
        self.label_caminhoPastasProvas.setText(_translate("MainWindow", "Caminho Pastas Provas:"))
        self.botaoGerarCorrigirprovas.setText(_translate("MainWindow", "Gerar"))

    def corrigir(self):
        from testquest import TestQuest

        TQ = TestQuest(path=self.lineEdit_CaminhoGabarito.text())
        TQ.constructResults(self.lineEdit_CaminhoPastas_Provas.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
