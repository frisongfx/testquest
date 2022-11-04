# Importa a classe de leitura e manipulação de imagens
import cv2

# Importa o numpy para manipulação de arrays
import numpy as np

# Importa a biblioteca de comparação de similaridade via IA
from sklearn.metrics.pairwise import cosine_similarity

# Classe que compara alternativas recebidas
class Comparator():
    def __init__(self):
        # Inicia as imagens de comparação para as provas
        self.fillPath = r'.\treino1.jpg'
        self.emptyPath = r'.\treino2.jpg'
        self.trainFill = np.array(
            cv2.cvtColor(cv2.imread(self.fillPath, cv2.IMREAD_COLOR), cv2.COLOR_BGR2GRAY)).flatten() / 255
        self.trainEmpty = np.array(
            cv2.cvtColor(cv2.imread(self.emptyPath, cv2.IMREAD_COLOR), cv2.COLOR_BGR2GRAY)).flatten() / 255

        # Inicia as imagens de comparação para as informações pessoais
        self.infoPath1 = r'.\treino3.jpg'
        self.infoPath2 = r'.\treino4.jpg'
        self.trainInfo1 = np.array(
            cv2.cvtColor(cv2.imread(self.infoPath1, cv2.IMREAD_COLOR), cv2.COLOR_BGR2GRAY)).flatten() / 255
        self.trainInfo2 = np.array(
            cv2.cvtColor(cv2.imread(self.infoPath2, cv2.IMREAD_COLOR), cv2.COLOR_BGR2GRAY)).flatten() / 255

    # Função que compara uma alternativa de uma prova
    # Recebe a imagem da alternativa
    # Retorna a diferença entre a comparação preenchida e vazia arredondado em 3 casas decimais
    def compare(self, alternative):
        alt = np.array(cv2.cvtColor(alternative, cv2.COLOR_BGR2GRAY)).flatten() / 255
        sim = cosine_similarity([alt], [self.trainFill])[0][0]
        nao = cosine_similarity([alt], [self.trainEmpty])[0][0]

        return round((nao * 100) - (sim * 100), 3)

    # Função que compara uma resposta de informação pessoal
    # Recebe a imagem de uma resposta
    # Retorna a diferença entre a comparação preenchida e vazia arredondado em 3 casas decimais
    def compare_info(self, alternative):
        alt = np.array(cv2.cvtColor(alternative, cv2.COLOR_BGR2GRAY)).flatten() / 255
        sim = cosine_similarity([alt], [self.trainInfo1])[0][0]
        nao = cosine_similarity([alt], [self.trainInfo2])[0][0]

        return round((nao * 100) - (sim * 100), 3)