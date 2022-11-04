# Importa a classe de leitura e manipulação de imagens
import cv2

# Importa o numpy para manipulação de arrays
import numpy as np

# Importa a função de corte e identificação das provas
from preparetest import PrepareTest


# Classe que recebe o gabarito e compara com uma pasta de provas e retorna os resultados para API
# Recebe o caminho para a imagem do gabarito
class TestQuest():
    # Início das variáveis da classe
    def __init__(self, path='./gabarito.jpg'):
        # Instância da função de corte e identificação das provas
        self.pt = PrepareTest()

        # Leitura do gabarito a partir do caminho recbido
        self.gabPath = path
        self.gabarito = np.array(cv2.imread(self.gabPath, cv2.IMREAD_COLOR))

        # Atributo que recebe o corte já identificado do gabarito
        self.result_gab = self.pt.identifyAlternative(
            self.pt.cutAlternative(
                self.pt.cutQuest(
                    self.pt.cutTest(self.gabarito)
                )
            )
        )

        # Números para a barra de progresso (NÃO FUNCIONAL AINDA)
        self.total = 0
        self.progress = 0

    # Função que compara a prova com o gabarito
    # Recebe a prova cortada e identificada
    # Retorna uma string com os resultados em 0 e 1 para cada questão
    def compareGab(self, result_quests):
        correct = ""

        qst = 0
        for quest in self.result_gab:
            if result_quests[qst] == quest:
                correct = correct + "1,"
            else:
                correct = correct + "0,"

            qst += 1

        correct = correct.strip(',')
        return correct

    # Função que lê o QR code da prova
    # Recebe o caminho da prova
    # Retorna o número referente ao QR code da prova
    def readQR(self, prova_path):
        from PIL import Image
        from pyzbar.pyzbar import decode
        import glob

        qr = glob.glob(prova_path)

        for i in range(len(qr)):
            data = decode(Image.open(qr[i]))
            data_qr = str(data[0].data)
            data_qr = data_qr[2:-1]

        return data_qr

    # Função que constroi os resultados no formato correto para envio à API
    # Recebe o caminho da prova
    # Retorna um dicionário com os resultados prontos para serem exportados
    def constructResults(self, prova_path):
        id = self.readQR(prova_path)
        test = np.array(cv2.imread(prova_path, cv2.IMREAD_COLOR))

        answers = self.compareGab(
            self.pt.identifyAlternative(
                self.pt.cutAlternative(
                    self.pt.cutQuest(
                        self.pt.cutTest(test)
                    )
                )
            )
        )

        infos = self.pt.INFOS.returnInfos(test)

        final_result = {
            'respostas': answers,
            'generoFK': infos[0],
            'etniaFK': infos[1],
            'pcdFK': infos[2],
            'idQrcode': id
        }

        return final_result

    # Função que lê a pasta de provas e exporta todos os resultados para a API
    # Recebe o caminho da pasta onde estão todas as provas (e somente as provas)
    def exportResults(self, path='./gabs'):
        # Importa a função de exportação para API
        from export import export_results
        # Importa a biblioteca de interação com o sistema operacional
        import os

        body = []
        folder_path = path
        paths = os.listdir(folder_path)

        for p in paths:
            self.total += 1

        v = 0
        for p in paths:
            body.append(self.constructResults(str(folder_path + '\\' + p)))
            self.progress += 1

            # Impressão visual em console -----------------
            print(self.progress, '/', self.total)
            print(p)
            print(body[v])
            # ---------------------------------------------

            v += 1

        # Retornar resultados
        #export_results(body)