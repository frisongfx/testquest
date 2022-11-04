import requests

def export_results(body):

    API = 'http://127.0.0.1:8000/pessoas/'

    # body = [{
    #     "nome": "",
    #     "respostas": "0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1",
    #     "genero": "Masculino",
    #     "etnia": "Branco",
    #     "pcd": True,
    #     "idQrcode": 176
    # }]

    for pessoa in body:
        requests.put(API + str(pessoa.get("idQrcode")) + "/", json=pessoa)
