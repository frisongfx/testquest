# Importa a classe do comparador com a IA
from comparator import Comparator

# Importa a classe de extração de informações do participante
from returninfos import ReturnInfos

# Importa a classe de leitura e manipulação de imagens
import cv2


# Classe que prepara o corte da prova e identifica as questões
class PrepareTest():
    # Início das variáveis da classe
    def __init__(self):
        # Instância do comparador
        self.COMP = Comparator()
        # Instancia da classe de extração de informações que leva o comparador como parâmetro
        self.INFOS = ReturnInfos(self.COMP)

        # Variáveis do formato da prova
        self.total_blocks = 2
        self.total_quests_per_block = 15
        self.total_alternatives = 5

        # Instância das variáveis de controle de pixels
        self.px_block_total = 0
        self.px_block_diff = 0

        self.px_V_total = 0
        self.px_Vt_offset = 0
        self.px_Vb_offset = 0

        self.px_H_total = 0
        self.px_Hl_offset = 0
        self.px_Hr_offset = 0


    # Função que enquadra a prova dinamicamente a partir do quadrado vermelho e corta os blocos de questões
    # Recebe a imagem escaneada da prova
    # Retorna um array com as imagens de cada bloco
    def cutTest(self, prova):
        alt, larg, c = prova.shape

        cut = []
        for w in range(alt):
            for z in range(larg):
                if prova[w][z][0] < 100 and prova[w][z][2] > 150 and z < (larg/2):
                    for j in range(alt):
                        for k in range(larg):
                            if prova[j][k][0] < 100 and prova[j][k][2] > 245 and k > (larg/2):

                                self.px_H_total = k-z
                                self.px_Hl_offset = self.px_H_total // 30
                                self.px_Hr_offset = self.px_H_total // 50

                                self.px_V_total = j-w
                                self.px_Vt_offset = self.px_V_total // 22
                                self.px_Vb_offset = self.px_V_total // 28

                                self.px_block_total = (self.px_H_total
                                                       - self.px_Hr_offset
                                                       - self.px_Hl_offset) // 3
                                self.px_block_total = self.px_block_total + (self.px_block_total // 13)

                                self.px_block_diff = (self.px_H_total
                                                       - self.px_Hr_offset
                                                       - self.px_Hl_offset) // 4
                                self.px_block_diff = self.px_block_diff + (self.px_block_diff // 7)

                                full = prova[w + self.px_Vt_offset: j - self.px_Vb_offset,
                                            z + self.px_Hl_offset: k - self.px_Hr_offset]

                                for i in range(self.total_blocks):
                                    if i == 0:
                                        cut.append(full[:, :self.px_block_total])
                                    else:
                                        cut.append(full[:, (self.px_block_total * i) + (self.px_block_diff * i):])
                                break
                        if prova[j][k][0] < 100 and prova[j][k][2] > 150 and k > (larg / 2):
                            break
                    break
            if prova[w][z][0] < 100 and prova[w][z][2] > 150 and z < (larg / 2):
                break


        return cut

    # Função que divide os blocos em suas respectivas questões
    # Recebe um array com as imagens de cada bloco
    # Retorna um array com as imagens de cada questão
    def cutQuest(self, cut):
        quests = []
        for i, block in enumerate(cut):
            alt, larg, c = block.shape
            tam = alt // self.total_quests_per_block
            sec = 0
            for sect in range(0, alt, tam):
                quest = block[sect:sect + tam, 0:larg]
                quests.append(quest)
                sec += 1
                if sec == self.total_quests_per_block:
                    break

        quests = quests[:-5]
        return quests

    # Função que divide cada questão em suas respectivas alternativas
    # Recebe um array com as imagens de cada questão
    # Retorna uma matriz com um array de alternativas pra cada questão
    def cutAlternative(self, quests):
        splited_quests = []

        for quest in quests:
            alt, larg, c = quest.shape
            this_quest = []
            tam = larg // (self.total_alternatives)
            sec = 0
            for sect in range(0, larg, tam):
                alternative = quest[0:alt, sect:sect + tam]
                this_quest.append(alternative)
                sec += 1
                if sec == self.total_alternatives:
                    break

            splited_quests.append(this_quest)

        return splited_quests

    # Função que identifica cada alternativa de cada questão através da IA
    # Recebe uma matriz com um array de alternativas pra cada questão
    # Retorna uma matriz com um array de alternativas de 0 = Branco e 1 = Preenchido para cada questão
    def identifyAlternative(self, splited_quests):
        result_quests = []

        for quest in splited_quests:
            quest_result = []
            for alternative in quest:
                similarity = self.COMP.compare(alternative)
                if similarity <= 2.5:
                    quest_result.append(1)
                else:
                    quest_result.append(0)

            result_quests.append(quest_result)

        return result_quests