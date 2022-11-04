from PyQt5 import QtCore, QtGui, QtWidgets
import requests, time
import pandas as pd

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(551, 475)
        self.MainWindow.setMinimumSize(QtCore.QSize(551, 475))
        self.MainWindow.setMaximumSize(QtCore.QSize(551, 475))
        self.MainWindow.setSizeIncrement(QtCore.QSize(551, 475))
        self.MainWindow.setBaseSize(QtCore.QSize(551, 475))
        self.MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_Criarprocesso_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_Criarprocesso_2.setGeometry(QtCore.QRect(0, 0, 551, 91))
        self.frame_Criarprocesso_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_Criarprocesso_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Criarprocesso_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Criarprocesso_2.setObjectName("frame_Criarprocesso_2")
        self.label_barrabosch = QtWidgets.QLabel(self.frame_Criarprocesso_2)
        self.label_barrabosch.setGeometry(QtCore.QRect(0, 0, 551, 16))
        self.label_barrabosch.setText("")
        self.label_barrabosch.setPixmap(QtGui.QPixmap("Bosch-Supergraphic.svg"))
        self.label_barrabosch.setScaledContents(True)
        self.label_barrabosch.setObjectName("label_barrabosch")
        self.label_logobosch = QtWidgets.QLabel(self.frame_Criarprocesso_2)
        self.label_logobosch.setGeometry(QtCore.QRect(0, 19, 171, 71))
        self.label_logobosch.setText("")
        self.label_logobosch.setPixmap(QtGui.QPixmap("Bosch_symbol_logo_black_red.png"))
        self.label_logobosch.setScaledContents(True)
        self.label_logobosch.setObjectName("label_logobosch")
        self.label_escritacorrecao = QtWidgets.QLabel(self.frame_Criarprocesso_2)
        self.label_escritacorrecao.setGeometry(QtCore.QRect(62, 70, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(10)
        self.label_escritacorrecao.setFont(font)
        self.label_escritacorrecao.setObjectName("label_escritacorrecao")
        self.frame_Criarprocesso = QtWidgets.QFrame(self.centralwidget)
        self.frame_Criarprocesso.setGeometry(QtCore.QRect(0, 90, 551, 391))
        self.frame_Criarprocesso.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_Criarprocesso.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Criarprocesso.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Criarprocesso.setObjectName("frame_Criarprocesso")
        self.label_logotestquest = QtWidgets.QLabel(self.frame_Criarprocesso)
        self.label_logotestquest.setGeometry(QtCore.QRect(111, 28, 321, 81))
        self.label_logotestquest.setText("")
        self.label_logotestquest.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_logotestquest.setScaledContents(True)
        self.label_logotestquest.setObjectName("label_logotestquest")
        self.label_nomedoProcesso = QtWidgets.QLabel(self.frame_Criarprocesso)
        self.label_nomedoProcesso.setGeometry(QtCore.QRect(187, 129, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_nomedoProcesso.setFont(font)
        self.label_nomedoProcesso.setObjectName("label_nomedoProcesso")
        self.lineEdit_nomedoProcesso = QtWidgets.QLineEdit(self.frame_Criarprocesso)
        self.lineEdit_nomedoProcesso.setGeometry(QtCore.QRect(154, 147, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        self.lineEdit_nomedoProcesso.setFont(font)
        self.lineEdit_nomedoProcesso.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.lineEdit_nomedoProcesso.setObjectName("lineEdit_nomedoProcesso")
        self.label_caminhoparaExcel = QtWidgets.QLabel(self.frame_Criarprocesso)
        self.label_caminhoparaExcel.setGeometry(QtCore.QRect(180, 185, 241, 20))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_caminhoparaExcel.setFont(font)
        self.label_caminhoparaExcel.setObjectName("label_caminhoparaExcel")
        self.lineEdit_caminhoparaExcel = QtWidgets.QLineEdit(self.frame_Criarprocesso)
        self.lineEdit_caminhoparaExcel.setGeometry(QtCore.QRect(154, 206, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        self.lineEdit_caminhoparaExcel.setFont(font)
        self.lineEdit_caminhoparaExcel.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.lineEdit_caminhoparaExcel.setObjectName("lineEdit_caminhoparaExcel")
        self.label_descricao = QtWidgets.QLabel(self.frame_Criarprocesso)
        self.label_descricao.setGeometry(QtCore.QRect(241, 240, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_descricao.setFont(font)
        self.label_descricao.setObjectName("label_descricao")
        self.lineEdit_descricao = QtWidgets.QLineEdit(self.frame_Criarprocesso)
        self.lineEdit_descricao.setGeometry(QtCore.QRect(155, 260, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        self.lineEdit_descricao.setFont(font)
        self.lineEdit_descricao.setStyleSheet("border: 1px solid black;\n"
"border-radius: 5px;")
        self.lineEdit_descricao.setObjectName("lineEdit_descricao")
        self.botaoGerarCriarProcessoSeletivo = QtWidgets.QPushButton(self.frame_Criarprocesso)
        self.botaoGerarCriarProcessoSeletivo.setGeometry(QtCore.QRect(222, 301, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.botaoGerarCriarProcessoSeletivo.setFont(font)
        self.botaoGerarCriarProcessoSeletivo.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid Grey;\n"
"border-radius: 5px;")
        self.botaoGerarCriarProcessoSeletivo.setObjectName("botaoGerarCriarProcessoSeletivo")
        self.botaoGerarCriarProcessoSeletivo.clicked.connect(self.sendProcess)
        self.label = QtWidgets.QLabel(self.frame_Criarprocesso)
        self.label.setGeometry(QtCore.QRect(0, 368, 551, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Bosch-Supergraphic.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        self.msgBox = QtWidgets.QMessageBox()
        self.msgBox.setIcon(QtWidgets.QMessageBox.Information)
        self.msgBox.setText("Processo cadastrado!")
        self.msgBox.setWindowTitle("Sucesso!")
        self.msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_escritacorrecao.setText(_translate("MainWindow", "Criar Processos Seletivos"))
        self.label_nomedoProcesso.setText(_translate("MainWindow", "Nome do Processo Seletivo:"))
        self.label_caminhoparaExcel.setText(_translate("MainWindow", "Caminho - Base de Candidatos:"))
        self.label_descricao.setText(_translate("MainWindow", "Descrição:"))
        self.botaoGerarCriarProcessoSeletivo.setText(_translate("MainWindow", "Gerar"))

    # Função que cria o processo seletivo e em seguida popula a api com a lista de nomes
    def sendProcess(self):
        API = 'http://127.0.0.1:8000/processos/'
        processo = [{
            'titulo': self.lineEdit_nomedoProcesso.text(),
            'descricao': self.lineEdit_descricao.text()
        }]

        requests.post(API, json=processo)

        while(True):
            p = requests.get(API + '?titulo=' + processo[0]['titulo']).json()
            if p == []:
                print('*')
                pass
            else:
                print(p)
                break

        if self.lineEdit_caminhoparaExcel.text() == '':
            self.msgBox.exec()
            self.MainWindow.close()
        else:
            file = pd.read_excel(self.lineEdit_caminhoparaExcel.text(), index_col=None,
                                 usecols=[0]).to_string(index=False).replace(" ", "").split("\n")
            var = ''
            nomes = []
            cont = 1
            for name in file:
                cont += 1
                nomes.append({"nome": name, "IdProcessoFK":p[0]['id']})

            API = "http://127.0.0.1:8000/pessoas/"
            requests.post(API, json=nomes)
            self.msgBox.exec()
            self.MainWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
