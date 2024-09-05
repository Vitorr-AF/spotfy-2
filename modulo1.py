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

def menu_inicial():
    print(
    """
1. Conferir músicas.
2. Selecionar pasta de músicas.
3. Informações
4. Fechar programa.
    """
    )
    opcao = input()
    if opcao == '1':
        conferir_musicas()
    elif opcao == '2':
        selecionar_pasta()
    elif opcao == '3':
        mostrar_info()
    elif opcao == '4':
        return
    else:
        print("Selecione uma opção válida")
        menu_inicial()


def conferir_musicas():
    os.system('cls')
    dados = json_texto()
    max_len = max(len(dados["baixadas"]), len(dados["não baixadas"]))
    
    baixadas_list = list(dados["baixadas"].items())
    nao_baixadas_list = list(dados["não baixadas"].items())


    print("Baixadas|Não baixadas")
    for i in range(max_len):
        # Para as músicas baixadas
        baixadas_nome, baixadas_link = baixadas_list[i] if i < len(baixadas_list) else ("", "")
        
        # Para as músicas não baixadas
        if i < len(nao_baixadas_list):
            nao_baixadas_nome, nao_baixadas_info = nao_baixadas_list[i]
            nao_baixadas_link = nao_baixadas_info[0]
            nao_baixadas_artista = nao_baixadas_info[1]
        else:
            nao_baixadas_nome, nao_baixadas_link, nao_baixadas_artista = "", "", ""

        print(f"{baixadas_nome}: '{baixadas_link}'   |   {nao_baixadas_nome}: '{nao_baixadas_link}' ({nao_baixadas_artista})")

    print(
"""
1. Adicionar música
2. Remover música
3. Baixar músicas
4. Voltar
"""
    )
    opcao = input()
    if opcao == '1':
        adicionar_musica()
    elif opcao == '2':
        remover_musica()
    elif opcao == '3':
        baixar_musicas()
    elif opcao == '4':
        menu_inicial()
    else:
        print("Insira uma opção válida")


def baixar_musicas():
    print('Nada aqui por enquanto')
def selecionar_pasta():
    os.system('cls')


def mostrar_info():
    os.system('cls')


def json_texto():
    with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)
    return dados


def adicionar_musica():
    print("Nome da música: ")
    nome = input("")
    if nome == "":
        conferir_musicas()
    print("Link da música: ")
    link = input("")
    print("Nome de artista: ")
    artista = input("")
    with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)
    dados['não baixadas'][nome] = link, artista
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo)
    conferir_musicas()


def remover_musica():
    print("Nome da música: ")
    nome = input("")
    if nome == "":
        conferir_musicas()
    

    with open('dados.json', 'r') as arquivo:
        dados = json.load(arquivo)
    dados['não baixadas'].pop(nome)
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo)
    conferir_musicas()
