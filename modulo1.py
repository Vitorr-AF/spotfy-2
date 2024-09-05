import json
import os


def verificar_json():
    """
    Verifica se o arquivo de dados json já existe, se não for o caso cria um arquivo vazio
    """
    if os.path.isfile('./dados.json'):
        with open('dados.json', 'r') as dados:
            dicionario = json.load(dados)
            if 'baixadas' not in dicionario:
                dicionario['baixadas'] = {}
            if 'não baixadas' not in dicionario:
                dicionario['não baixadas'] = {}
            if 'pasta' not in dicionario:
                dicionario['pasta'] = {}
        with open('dados.json', 'w') as dados:
            json.dump(dicionario, dados)
        
    else:
        dics = {}
        dics['baixadas'] = {}
        dics['não baixadas'] = {}
        dics['pasta'] = ''

        with open('dados.json', 'w') as dados:
            json.dump(dics, dados)

