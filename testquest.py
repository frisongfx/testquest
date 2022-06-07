import cv2
import numpy as np

class TestQuest():
    def __init__(self):
        self.total_quests = 10
        self.total_alternatives = 5
        self.prova1_path = './gabs2/gab.png'
        self.gabarito = np.array(cv2.imread('./gabs2/gab.png', cv2.IMREAD_COLOR))
        self.prova1 = np.array(cv2.imread(self.prova1_path, cv2.IMREAD_COLOR))

    def cutTest(self, prova):
        alt, larg, c = prova.shape
        for y in range(alt):
            for x in range(larg):
                if prova[y][x][0] < 100 and prova[y][x][2] > 200:
                    cut = prova[y:y + 1350, x+4:x + 690]
                    break

        return cut

    def cutQuest(self, prova):
        alt, larg, c = prova.shape
        quests = []
        tam = alt//self.total_quests
        sec = 0
        for sect in range(0, alt, tam):
            quest = prova[sect:sect + tam, 0:larg]
            quests.append(quest)
            sec +=1
            if sec == self.total_quests:
                break

        return quests

    def cutAlternative(self, quests):
        splited_quests = []

        for quest in quests:
            alt, larg, c = quest.shape
            this_quest = []
            tam = larg//(self.total_alternatives)
            sec = 0
            for sect in range(0, larg, tam):
                alternative = quest[0:alt, sect:sect + tam]
                this_quest.append(alternative)
                sec += 1
                if sec == self.total_alternatives:
                    break

            splited_quests.append(this_quest)

        return splited_quests

    def identifyAlternative(self, splited_quests):
        result_quests = []

        for quest in splited_quests:
            quest_result = []
            for alternative in quest:
                alternative = cv2.cvtColor(alternative, cv2.COLOR_BGR2GRAY)
                alt, larg = alternative.shape

                blackPx = 0
                for pxAlt in range(alt):
                    for pxLarg in range(larg):
                        if alternative[pxAlt, pxLarg] < 100:
                            blackPx += 1

                if blackPx < 4600:
                    quest_result.append(0)
                elif blackPx < 8750:
                    quest_result.append(2)
                elif blackPx < 13000:
                    quest_result.append(1)
                else:
                    quest_result.append(2)

            result_quests.append(quest_result)

        return result_quests

    def compareGab(self, result_quests):
        result_gab = self.identifyAlternative(self.cutAlternative(self.cutQuest(self.cutTest(self.gabarito))))
        correct = []

        qst = 0
        for quest in result_gab:
            if result_quests[qst] == quest:
                correct.append(True)
            else:
                correct.append(False)

            qst += 1

        return correct

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

    def constructResults(self, prova_path):
        id = self.readQR(prova_path)
        result = self.compareGab(self.identifyAlternative(self.cutAlternative(self.cutQuest(self.cutTest(np.array(cv2.imread(prova_path, cv2.IMREAD_COLOR)))))))

        gerais = 0
        tecnicas = 0
        pos = 0
        acertos = 0
        erros = 0
        for quest in result:
            if quest:
                acertos += 1
                if pos < 5:
                    gerais += 1
                else:
                    tecnicas += 1
            else:
                erros += 1

            pos += 1

        total = [acertos, erros]
        gerais_tecnicas = [gerais, tecnicas]

        final_result = [
            id,
            total,
            gerais_tecnicas,
            result
        ]

        return final_result

    def excel(self, final_result):
        from excel_export import excel
        excel.export_results(final_result, self.total_quests)


tq = TestQuest()
tq.excel(tq.constructResults(tq.prova1_path))