import csv

def criar_dados_animais():
    with open("dados_animais.csv", "w", newline="", encoding="utf-8") as dados:
        escritor = csv.writer(dados)
        escritor.writerow([
            "id", "nome", "espécie", "raça", 
            "idade", "saúde", "chegada", "comportamento"
        ])

def criar_dados_atividades():
    with open("dados_atividades.csv", "w", newline="", encoding="utf-8") as dados:
        escritor = csv.writer(dados)
        escritor.writerow([
            "id_animal", "id_atividade", "nome_atividade", "data", "responsável"
        ])

def salvar_dados(dados_animal):
    with open("dados_animais.csv", "a", newline="", encoding="utf-8") as dados:
        escritor = csv.writer(dados)
        escritor.writerow(dados_animal)

def salvar_atividades(dados_atividades):
    with open("dados_atividades.csv", "a", newline="", encoding="utf-8") as dados:
        escritor = csv.writer(dados)
        escritor.writerow(dados_atividades)

def carregar_dados():
    try:
        with open("dados_animais.csv", "r", encoding="utf-8") as dados:
            return list(csv.reader(dados))
    except FileNotFoundError:
        return []

def carregar_dados_atv():
    try:
        with open("dados_atividades.csv", "r", encoding="utf-8") as dados:
            return list(csv.reader(dados))
    except FileNotFoundError:
        return []