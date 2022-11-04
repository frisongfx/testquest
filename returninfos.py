# Classe que lê e retorna o resultado das informações pessoais do candidato
class ReturnInfos():
    # Inicio das variáveis da classe
    # Recebe o comparador da IA
    def __init__(self, Comparator):
        self.COMP = Comparator

        # Coordenadas para o corte da região das informações (MANUAL)
        self.Y1 = 1739
        self.Y2 = 1975
        self.X1 = 85
        self.X2 = 1133

    # Função que corta a região das informações baseado nas coordenadas da classe
    # Recebe a imagem da prova
    # Retorna a imagem da região cortada
    def cutInfos(self, prova):
        alt, larg, c = prova.shape
        cutted_infos = []
        for y in range(alt):
            for x in range(larg):
                if prova[y][x][0] < 100 and prova[y][x][2] > 200:
                    cutted_infos = prova[y + self.Y1:y + self.Y2, x + self.X1:x + self.X2]
                    break
            if prova[y][x][0] < 100 and prova[y][x][2] > 200:
                break

        return cutted_infos

    # Função que divide as informações e suas respectivas respostas assinaladas
    # Recebe a imagem da região cortada
    # Retorna uma matriz com cada tipo de informação e suas respectivas respostas
    def sliceInfos(self, cutted_infos):
        alt = 97
        label = 260
        height = 59
        sliced_infos = []
        genero = []
        etnia = []
        pcd = []

        genero.append(cutted_infos[0:height, 0:alt])
        genero.append(cutted_infos[0:height, alt + label:(alt * 2) + label])
        genero.append(cutted_infos[0:height, (alt * 2) + (label * 2):(alt * 3) + (label * 2)])

        sliced_infos.append(genero)

        etnia.append(cutted_infos[height:height * 2, 0:alt])
        etnia.append(cutted_infos[height:height * 2, alt + label:(alt * 2) + label])
        etnia.append(cutted_infos[height:height * 2, (alt * 2) + (label * 2):(alt * 3) + (label * 2)])
        etnia.append(cutted_infos[height * 2:height * 3, 0:alt])
        etnia.append(cutted_infos[height * 2:height * 3, alt + label:(alt * 2) + label])
        etnia.append(cutted_infos[height * 2:height * 3, (alt * 2) + (label * 2):(alt * 3) + (label * 2)])

        sliced_infos.append(etnia)

        pcd.append(cutted_infos[height * 3:height * 4, alt + label:(alt * 2) + label])
        pcd.append(cutted_infos[height * 3:height * 4, (alt * 2) + (label * 2):(alt * 3) + (label * 2)])

        sliced_infos.append(pcd)

        return sliced_infos

    # Função que compara e retorna o resultado das respostas das informações pessoais
    # Recebe a imagem da prova (e envia para a função 'cutInfos')
    # Retorna com um array de 3 números inteiros com os resultados de cada uma das informações
    def returnInfos(self, prova):
        sliced_infos = self.sliceInfos(self.cutInfos(prova))
        import cv2
        answers = []
        opt = []
        for option in sliced_infos:
            for answer in option:
                # cv2.imshow('title', answer)
                # cv2.waitKey(0)
                A = self.COMP.compare_info(answer)
                if A <= 2.5:
                    opt.append(1)
                else:
                    opt.append(0)

            answers.append(opt)
            opt = []

        results = []

        if answers[0] == [1, 0, 0]:
            results.append(1)
        elif answers[0] == [0, 1, 0]:
            results.append(2)
        else:
            results.append(3)

        if answers[1] == [1, 0, 0, 0, 0, 0]:
            results.append(1)
        elif answers[1] == [0, 1, 0, 0, 0, 0]:
            results.append(2)
        elif answers[1] == [0, 0, 1, 0, 0, 0]:
            results.append(3)
        elif answers[1] == [0, 0, 0, 1, 0, 0]:
            results.append(4)
        elif answers[1] == [0, 0, 0, 0, 1, 0]:
            results.append(5)
        else:
            results.append(6)

        if answers[2] == [1, 0]:
            results.append(1)
        else:
            results.append(2)

        return results