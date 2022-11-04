from PyQt5 import QtCore, QtGui, QtWidgets
import CriarProcessoSeletivo, GerarProvas, CorrigirProvas

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(551, 475)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(551, 475))
        MainWindow.setMaximumSize(QtCore.QSize(551, 475))
        MainWindow.setSizeIncrement(QtCore.QSize(551, 454))
        MainWindow.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_menu = QtWidgets.QFrame(self.centralwidget)
        self.frame_menu.setGeometry(QtCore.QRect(0, 91, 551, 391))
        self.frame_menu.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.label_logotestquest = QtWidgets.QLabel(self.frame_menu)
        self.label_logotestquest.setGeometry(QtCore.QRect(116, 34, 321, 81))
        self.label_logotestquest.setText("")
        self.label_logotestquest.setPixmap(QtGui.QPixmap("logo.png"))
        self.label_logotestquest.setScaledContents(True)
        self.label_logotestquest.setObjectName("label_logotestquest")
        self.botao_criar_processos = QtWidgets.QPushButton(self.frame_menu)
        self.botao_criar_processos.setGeometry(QtCore.QRect(186, 147, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_criar_processos.setFont(font)
        self.botao_criar_processos.setStyleSheet("\n"
"background-color: rgb(165, 165, 165);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid Grey;\n"
"border-radius: 5px;")
        self.botao_criar_processos.setObjectName("botao_criar_processos")
        self.botao_gerarprovas = QtWidgets.QPushButton(self.frame_menu)
        self.botao_gerarprovas.setGeometry(QtCore.QRect(186, 208, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_gerarprovas.setFont(font)
        self.botao_gerarprovas.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid Grey;\n"
"border-radius: 5px;")
        self.botao_gerarprovas.setObjectName("botao_gerarprovas")
        self.botao_CorrigirProvas = QtWidgets.QPushButton(self.frame_menu)
        self.botao_CorrigirProvas.setGeometry(QtCore.QRect(186, 270, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.botao_CorrigirProvas.setFont(font)
        self.botao_CorrigirProvas.setStyleSheet("background-color: rgb(165, 165, 165);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid Grey;\n"
"border-radius: 5px;")
        self.botao_CorrigirProvas.setObjectName("botao_CorrigirProvas")
        self.label = QtWidgets.QLabel(self.frame_menu)
        self.label.setGeometry(QtCore.QRect(0, 367, 551, 20))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Bosch-Supergraphic.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame_menu_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_menu_2.setGeometry(QtCore.QRect(0, 0, 551, 91))
        self.frame_menu_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_menu_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu_2.setObjectName("frame_menu_2")
        self.label_barrabosch = QtWidgets.QLabel(self.frame_menu_2)
        self.label_barrabosch.setGeometry(QtCore.QRect(0, 0, 821, 16))
        self.label_barrabosch.setText("")
        self.label_barrabosch.setPixmap(QtGui.QPixmap("Bosch-Supergraphic.svg"))
        self.label_barrabosch.setScaledContents(True)
        self.label_barrabosch.setObjectName("label_barrabosch")
        self.label_logobosch = QtWidgets.QLabel(self.frame_menu_2)
        self.label_logobosch.setGeometry(QtCore.QRect(0, 20, 171, 71))
        self.label_logobosch.setText("")
        self.label_logobosch.setPixmap(QtGui.QPixmap("Bosch_symbol_logo_black_red.png"))
        self.label_logobosch.setScaledContents(True)
        self.label_logobosch.setObjectName("label_logobosch")
        self.label_escritacorrecao = QtWidgets.QLabel(self.frame_menu_2)
        self.label_escritacorrecao.setGeometry(QtCore.QRect(62, 70, 121, 20))
        font = QtGui.QFont()
        font.setFamily("Bosch Sans")
        font.setPointSize(10)
        self.label_escritacorrecao.setFont(font)
        self.label_escritacorrecao.setObjectName("label_escritacorrecao")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.botao_criar_processos.clicked.connect(self.mostrarCriarprocessosSeletivos)
        self.botao_gerarprovas.clicked.connect(self.mostrarGerarProvas)
        self.botao_CorrigirProvas.clicked.connect(self.mostrarCorrigirProvas)

    def mostrarCriarprocessosSeletivos(self):
        MainCriarProcessos.show()

    def mostrarGerarProvas(self):
        MainGerarProvas.show()

    def mostrarCorrigirProvas(self):
        MainCorrigirProvas.show()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.botao_criar_processos.setText(_translate("MainWindow", "Criar Processos Seletivos"))
        self.botao_gerarprovas.setText(_translate("MainWindow", "Gerar Provas"))
        self.botao_CorrigirProvas.setText(_translate("MainWindow", "Corrigir Provas"))
        self.label_escritacorrecao.setText(_translate("MainWindow", "Correção de Provas"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #CriarProcessos
    MainCriarProcessos = QtWidgets.QMainWindow()
    telaCriarProcessos = CriarProcessoSeletivo.Ui_MainWindow()
    telaCriarProcessos.setupUi(MainCriarProcessos)

    #GerarProvas
    MainGerarProvas = QtWidgets.QMainWindow()
    telaGerarProvas = GerarProvas.Ui_MainWindow()
    telaGerarProvas.setupUi(MainGerarProvas)

    #CorrigirProvas
    MainCorrigirProvas = QtWidgets.QMainWindow()
    telaCorrigirProvas = CorrigirProvas.Ui_MainWindow()
    telaCorrigirProvas.setupUi(MainCorrigirProvas)


    sys.exit(app.exec_())
