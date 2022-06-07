import pandas as pd
import qrcode
import cv2
import numpy as np

nome_alunos = ()

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=30,
    border=2
)

'''nome_alunos = [
    "Ryan",
    "João",
    "Maria",
    "Jorge",
    "Cleusa",
    "Paulo",
    "Francisco"
]'''

nome_alunos = pd.read_excel(r"S:\PM\ter\ets\Inter_Setor\COMPARTILHADO\PROJETOS\Smart Automation 2ª Turma\Projetos Especiais\Correção Automática de Prova\2ª EDIÇÃO HACKATHON\testquest\excel_export\Banco_Geral.xlsx")

for i in range(nome_alunos.ID.size):
    nome = (nome_alunos["ID"][i])
    imagem_qrcode = qrcode.make(nome)
    imagem_qrcode.save(f"qcode_{nome}.png")

'''
for i in range(nome_alunos.ID.size):
    print(nome_alunos.NOME.values[i])


for i in nome_alunos:
    nome = (nome_alunos["NOME"] [i])
    imagem_qrcode = qrcode.make(nome)
    imagem_qrcode.save(f"qcode_{nome}.png")
'''

