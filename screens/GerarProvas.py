from PyQt5 import QtCore, QtGui, QtWidgets
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 475)
        MainWindow.setMinimumSize(QtCore.QSize(551, 475))
        MainWindow.setMaximumSize(QtCore.QSize(551, 475))
        MainWindow.setSizeIncrement(QtCore.QSize(551, 475))
        MainWindow.setBaseSize(QtCore.QSize(551, 475))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_CorrigirProvas = QtWidgets.QFrame(self.centralwidget)
        self.frame_CorrigirProvas.setGeometry(QtCore.QRect(0, 0, 551, 91))
        self.frame_CorrigirProvas.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_CorrigirProvas.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CorrigirProvas.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CorrigirProvas.setObjectName("frame_CorrigirProvas")
        self.label_barrabosch = QtWidgets.QLabel(self.frame_CorrigirProvas)
        self.label_barrabosch.setGeometry(QtCore.QRect(0, 0, 551, 16))
        self.label_barrabosch.setText("")
        self.label_barrabosch.setPixmap(QtGui.QPixmap("Bosch-Supergraphic.svg"))
        self.label_barrabosch.setScaledContents(True)
        self.label_barrabosch.setObjectName("label_barrabosch")
        self.label_logobosch = QtWidgets.QLabel(self.frame_CorrigirProvas)
        self.label_logobosch.setGeometry(QtCore.QRect(0, 20, 171, 71))
        self.label_logobosch.setText("")
        self.label_logobosch.setPixmap(QtGui.QPixmap("Bosch_symbol_logo_black_red.png"))
        self.label_logobosch.setScaledContents(True)
        self.label_logobosch.setObjectName("label_logobosch")
        self.label_escritacorrecao = QtWidgets.QLabel(self.frame_CorrigirProvas)
        self.label_escritacorrecao.setGeometry(QtCore.QRect(64, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(10)
        self.label_escritacorrecao.setFont(font)
        self.label_escritacorrecao.setObjectName("label_escritacorrecao")
        self.frame_CorrigirProvas_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_CorrigirProvas_2.setGeometry(QtCore.QRect(0, 90, 551, 391))
        self.frame_CorrigirProvas_2.setMaximumSize(QtCore.QSize(551, 475))
        self.frame_CorrigirProvas_2.setBaseSize(QtCore.QSize(551, 475))
        self.frame_CorrigirProvas_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_CorrigirProvas_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_CorrigirProvas_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_CorrigirProvas_2.setObjectName("frame_CorrigirProvas_2")
        self.label_logotestquest = QtWidgets.QLabel(self.frame_CorrigirProvas_2)
        self.label_logotestquest.setGeometry(QtCore.QRect(110, 27, 321, 81))
        self.label_logotestquest.setText("")
        self.label_logotestquest.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_logotestquest.setScaledContents(True)
        self.label_logotestquest.setObjectName("label_logotestquest")
        self.comboBox_SelecionarProcessoSeletivo = QtWidgets.QComboBox(self.frame_CorrigirProvas_2)
        self.comboBox_SelecionarProcessoSeletivo.setGeometry(QtCore.QRect(182, 128, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        self.comboBox_SelecionarProcessoSeletivo.setFont(font)
        self.comboBox_SelecionarProcessoSeletivo.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.comboBox_SelecionarProcessoSeletivo.setObjectName("comboBox_SelecionarProcessoSeletivo")
        self.comboBox_SelecionarProcessoSeletivo.addItem("")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_CorrigirProvas_2)
        self.dateEdit.setGeometry(QtCore.QRect(219, 197, 110, 22))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.dateEdit.setObjectName("dateEdit")
        self.label_datadaprova = QtWidgets.QLabel(self.frame_CorrigirProvas_2)
        self.label_datadaprova.setGeometry(QtCore.QRect(228, 178, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_datadaprova.setFont(font)
        self.label_datadaprova.setObjectName("label_datadaprova")
        self.label_numero = QtWidgets.QLabel(self.frame_CorrigirProvas_2)
        self.label_numero.setGeometry(QtCore.QRect(199, 228, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_numero.setFont(font)
        self.label_numero.setObjectName("label_numero")
        self.label_participantes = QtWidgets.QLabel(self.frame_CorrigirProvas_2)
        self.label_participantes.setGeometry(QtCore.QRect(192, 251, 81, 20))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_participantes.setFont(font)
        self.label_participantes.setObjectName("label_participantes")
        self.spinBox_nParticipantes = QtWidgets.QSpinBox(self.frame_CorrigirProvas_2)
        self.spinBox_nParticipantes.setGeometry(QtCore.QRect(281, 236, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox_nParticipantes.setFont(font)
        self.spinBox_nParticipantes.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.spinBox_nParticipantes.setMaximum(99999)
        self.spinBox_nParticipantes.setObjectName("spinBox_nParticipantes")
        self.botaoGerar_GerarProvas = QtWidgets.QPushButton(self.frame_CorrigirProvas_2)
        self.botaoGerar_GerarProvas.setGeometry(QtCore.QRect(223, 296, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.botaoGerar_GerarProvas.setFont(font)
        self.botaoGerar_GerarProvas.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid Grey;\n"
"border-radius: 5px;")
        self.botaoGerar_GerarProvas.setObjectName("botaoGerar_GerarProvas")
        self.label = QtWidgets.QLabel(self.frame_CorrigirProvas_2)
        self.label.setGeometry(QtCore.QRect(0, 368, 551, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Bosch-Supergraphic.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.botaoGerar_GerarProvas.clicked.connect(self.generate)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_escritacorrecao.setText(_translate("MainWindow", "Gerar Provas"))
        self.comboBox_SelecionarProcessoSeletivo.setItemText(0, _translate("MainWindow", "Selecionar Processo Seletivo"))

        # Inicia a combobox com informações diretas da API ------------------------------------------------------
        API = 'http://127.0.0.1:8000/processos/'
        processos = requests.get(API).json()
        v = 1
        for p in processos:
            self.comboBox_SelecionarProcessoSeletivo.addItem("")
            self.comboBox_SelecionarProcessoSeletivo.setItemText(v, _translate("MainWindow", p["titulo"]))
            v += 1
        # -------------------------------------------------------------------------------------------------------

        self.label_datadaprova.setText(_translate("MainWindow", "Data da Prova:"))
        self.label_numero.setText(_translate("MainWindow", "Número de"))
        self.label_participantes.setText(_translate("MainWindow", "Participantes"))
        self.botaoGerar_GerarProvas.setText(_translate("MainWindow", "Gerar"))

    # Função que chama o link para geração das provas pela API
    def generate(self):
        API = 'http://127.0.0.1:8000/processos/'
        p = requests.get(API + '?titulo=' + self.comboBox_SelecionarProcessoSeletivo.currentText()).json()

        API = 'http://127.0.0.1:8000/gabaritos?processo='
        requests.get(API+str(p[0]['id']))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
