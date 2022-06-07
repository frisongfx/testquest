import pandas as pd

def export_results(prova, qtdQuest):
    arquivo_geral = pd.read_excel(r'C:\Users\ct67ca\Desktop\testquest\excel_export\Banco_Geral.xlsx')
    arquivo_lista = pd.read_excel(r'C:\Users\ct67ca\Desktop\testquest\excel_export\Banco_Lista.xlsx')
    arquivo_por_quest = pd.read_excel(r'C:\Users\ct67ca\Desktop\testquest\excel_export\Banco_TF.xlsx')

    i = 0
    for id in arquivo_lista['ID']:
            arquivo_geral.loc[i, 'ID'] = id
            arquivo_por_quest.loc[i, 'ID'] = id
            i = i + 1
    j = 0
    for nome in arquivo_lista['NOME']:
        for i in arquivo_geral['ID']:
            if i == id:
                arquivo_geral.loc[j, 'NOME'] = nome
                j = j + 1
    n = 0
    for data in arquivo_lista['DATA']:
        for m in arquivo_geral['ID']:
            if m == id:
                arquivo_geral.loc[n, 'DATA'] = data
                n = n + 1

    arquivo_geral.to_excel('C:\\Users\\ct67ca\\Desktop\\testquest\\excel_export\\Banco_Geral.xlsx', index=False)
    arquivo_por_quest.to_excel('C:\\Users\\ct67ca\\Desktop\\testquest\\excel_export\\Banco_TF.xlsx', index=False)

    arquivo_geral = pd.read_excel(r'C:\Users\ct67ca\Desktop\testquest\excel_export\Banco_Geral.xlsx')
    arquivo_por_quest = pd.read_excel(r'C:\Users\ct67ca\Desktop\testquest\excel_export\Banco_TF.xlsx')

    valor = prova[0]
    linha = 0

    for dado in arquivo_geral["ID"]:
        if str(dado) == valor:
            arquivo_geral.loc[linha, 'ACERTOS'] = prova[1][0]
            arquivo_geral.loc[linha, 'TOTAL DE ERROS'] = prova[1][1]
            arquivo_geral.loc[linha, 'ACERTOS TÉC.'] = prova[2][0]
            arquivo_geral.loc[linha, 'ACERTOS GERAIS'] = prova[2][1]
        else:
            linha = linha + 1

    linha = 0
    value = 0
    for dado in arquivo_por_quest["ID"]:
        if str(dado) == valor:
            for j in range(qtdQuest):
                quest = 'QUESTÃO {}'.format(j+1)
                if prova[3][j] == False:
                    value = 0
                elif prova[3][j] == True:
                    value = 1
                arquivo_por_quest.loc[linha, quest] = value
        else:
            linha = linha + 1

    arquivo_geral.to_excel('C:\\Users\\ct67ca\\Desktop\\testquest\\excel_export\\Banco_Geral.xlsx', index=False)
    arquivo_por_quest.to_excel('C:\\Users\\ct67ca\\Desktop\\testquest\\excel_export\\Banco_TF.xlsx', index=False)
