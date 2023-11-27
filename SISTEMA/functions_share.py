from datetime import datetime
import json


def obter_turno_atual(): #Para pegar o turno Atual
    hora_atual = datetime.now().time()
    turno_m_inicio = datetime.strptime("06:00", "%H:%M").time()
    turno_m_fim = datetime.strptime("19:00", "%H:%M").time()
    turno1_inicio = datetime.strptime("06:00", "%H:%M").time()
    turno2_inicio = datetime.strptime("14:36", "%H:%M").time()
    turno3_inicio = datetime.strptime("23:04", "%H:%M").time()

    if turno_m_inicio <= hora_atual < turno_m_fim:
        if turno1_inicio <= hora_atual < turno2_inicio:
            return "M1"
        else:
            return "M2"
    elif turno1_inicio <= hora_atual < turno2_inicio:
        return 1
    elif turno2_inicio <= hora_atual < turno3_inicio:
        return 2
    else:
        return 3

def carregar_usuarios(): # Carrega a matriz
    with open("bd/equipe/equipeDados.json", "r") as arquivo:
        usuarios = json.load(arquivo)
        return usuarios

def buscar_pessoa_registro(registro):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["Registro"] == registro:
            return usuario

def mostrar_usuarios(cod): #Mostra Usuario x Cargo x Turno
    if cod is None:
       return 0
    turno_selecionado = obter_turno_atual()
    list_permit={
        "0405": "Mecanico",
        "0406": "Eletricista",
        "0407": "Eletricista",
        "0408": "Eletricista",
        "0403": "TODOS",
        "0706": "TODOS",
        "0502": "Mecanico",
        "0504": "Eletricista",
        "0505": "Eletricista",
        "0506": "Eletricista",
        "0404": "Mecanico",
        "0418": "Mecanico",
    }
    usuarios = carregar_usuarios()
    usuarios_turno = []
    for usuario in usuarios:
        if isinstance(turno_selecionado, int) and usuario["Cargo"] != list_permit[cod]:
            if str(usuario["Turno"]) == str(turno_selecionado):
                usuarios_turno.append(usuario)
        elif isinstance(turno_selecionado, str):
            if turno_selecionado[0] == 'M' and (usuario["Turno"] == "M" or str(usuario["Turno"]) == turno_selecionado[1:]) and usuario["Cargo"] != list_permit[cod]:
                usuarios_turno.append(usuario)
    return usuarios_turno

def chaves_arquivo(): # Carrega as chaves do loto
    with open('bd/loto/chavesCadastradas.json', 'r',  encoding='utf-8') as arquivo_chaves:
        chaves_data = json.load(arquivo_chaves)
        return chaves_data
    
def  pesquisar_chave_arquivo(chave): # Buscar info da determinada Chave
    chaves = chaves_arquivo()
    for chave_info in chaves:
        if chave_info['chave'] == chave:
            return chave_info
        
        
def buscar_chave_no_temporario(chave): # Verificar se a chave esta em aberto
    with open('bd/loto/temporario.txt', 'r') as arquivo_temporario:
        linhas = arquivo_temporario.readlines()

    for linha in linhas:
        dados_registro = json.loads(linha)
        if dados_registro['chave'] == chave:
            return dados_registro