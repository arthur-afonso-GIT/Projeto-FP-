import csv
import os
from datetime import datetime


# mapeamento dos indices pra melhorar legibilidade

ID = 0
NOME = 1
ESPECIE = 2
RACA = 3
IDADE = 4
SAUDE = 5
CHEGADA = 6
COMPORTAMENTO = 7

ATV_ID_ANIMAL = 0
ATV_ID_ATIVIDADE = 1
ATV_NOME = 2
ATV_DATA = 3
ATV_RESPONSAVEL = 4


def gerar_id():
    agora = datetime.now()
    return int(agora.strftime("%d%m%H%M%S"))


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
    #"dados_animais.csv" é o nome do arquivo /// "a" significa q vai adicionar no final e/ou criar o arquivo /// newline="" garante que a linha acabe de maneira correta /// encoding="utf-8" permite o uso de caracteres especiais
    with open("dados_animais.csv", "a", newline="", encoding="utf-8") as dados:
        escritor = csv.writer(dados)
        escritor.writerow(dados_animal)


def salvar_atividades(dados_atividades):
    with open("dados_atividades.csv", "a", newline="", encoding="utf-8") as dados:
        escritor = csv.writer(dados)
        escritor.writerow(dados_atividades)


def carregar_dados():
    with open("dados_animais.csv", "r", encoding="utf-8") as dados:
        leitor = csv.reader(dados)
        return list(leitor)


def carregar_dados_atv():
    with open("dados_atividades.csv", "r", encoding="utf-8") as dados:
        leitor = csv.reader(dados)
        return list(leitor)

# item 1
def cadastro_animal(id,nome, especie, raca, idade, saude, chegada, comportamento):
    dados_animais=carregar_dados()
    id_string=str(id)
    existe=0
    for i in dados_animais:
        if id_string in i:
            print("ID ja cadastrado")
            existe=1
    if existe==0:
        dados_animal=[id, nome, especie, raca, idade, saude, chegada, comportamento]
        salvar_dados(dados_animal)
        print("Cadastrado com sucesso!  ")

def listar_animais():   
    dados_animais=carregar_dados()

    if len(dados_animais) <=1:
        print("A lista de animais está vazia.")
        return
    
    for i in dados_animais[1:]:
            print(f" id: {i[ID]}")
            print(f" Nome: {i[NOME]}")
            print(f" Idade: {i[IDADE]}")
            print(f" espécie: {i[ESPECIE]}")
            print(f" raça: {i[RACA]}")
            print(f" Estado de saúde: {i[SAUDE]}")
            print(f" comportamento: {i[COMPORTAMENTO]}")
            print(f" Data de chegada: {i[SAUDE]}")
            print("-" * 30)

#item 4
def listar_atividades():
    dados_atividades=carregar_dados_atv()
    existe=0
    for i in dados_atividades:
            print(f" id da atividade: {i[0]}")
            print(f" id do i: {i[1]}")
            print(f" Nome da atividade:{i[2]}")
            print(f" Data da atividade:{i[3]}")
            print(f" Nome do responsável:{i[4]}")
            existe+=1

def busca_especifica_nome(nome):
    encontrados = []
    dados_animais=carregar_dados()
    for i in dados_animais:
        if i[1].lower() == nome.lower():
            encontrados.append(i)
    
    if len(encontrados)!=0:
        print(f"\nResultados para {nome}: {len(encontrados)} encontrado(s)")
        for i in encontrados:
            print(f"\nID: {i[ID]}")
            print(f"Nome: {i[NOME]}")
            print(f"Espécie: {i[ESPECIE]}")
            print(f"Raça: {i[RACA]}")
            print(f"Saúde: {i[SAUDE]}")
    else:
        print(f"\nNenhum animal chamado '{nome}' foi localizado.")


def busca_especifica_id(id):
    id_string=str(id)
    dados_animais=carregar_dados()

    for i in dados_animais[1:]:
        if id_string==i[ID]:
            print(f"\nID: {i[ID]}")
            print(f"Nome: {i[NOME]}")
            print(f"Espécie: {i[ESPECIE]}")
            print(f"Raça: {i[RACA]}")
            print(f"Saúde: {i[SAUDE]}")
            return True
    print(f"O animal com o id {id} não foi encontrado.")
    return False

# item 6
def busca_atv_id_i(id):
    dados_atividades=carregar_dados_atv()
    ciclos = 0
    for i in dados_atividades:
        if id in i:
            print(f" ID da atividade: {i[0]}")
            print(f" Nome da atividade:{i[1]}")
            print(f" Data da atividade:{i[2]}")
            print(f" Nome do responsável:{i[3]}")
            ciclos+=1
    if ciclos==0:
        print("id não existe\n")

# item 6
def busca_atv_nome_atividade(nome_atv):
    dados_atividades=carregar_dados_atv()
    ciclos = 0
    for i in dados_atividades:
        if nome_atv in i:
            print(f" ID do do animal: {i[0]}")
            print(f" Nome da atividade:{i[1]}")
            print(f" Data da atividade:{i[2]}")
            print(f" Nome do responsável:{i[3]}")
            ciclos=1
    if ciclos==0:
        print("id não existe\n")
    
# item 7
def editar_animal_1(id,nome, especie, raca, idade, saude, chegada, comportamento):
    dados_animais=carregar_dados()
    temp_dados_animais=[]
    string_id=str(id)
    for i in dados_animais:
        if i[0]==string_id:
            if nome!=0:
                i[1]=nome
            if especie!=0:
                i[2]=especie
            if raca!=0:
                i[3]=raca
            if idade!=0:
                i[4]=idade
            if saude!=0:
                i[5]=saude
            if chegada!=0:
                i[6]=chegada
            if comportamento!=0:
                i[7]=comportamento
        temp_dados_animais.append(i)
    with open('dados_animais', 'w', newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)
        escritor.writerows(temp_dados_animais)


def editar_animal_2(id):
    dados_animais = carregar_dados()
    string_id = str(id)
    temp_dados_animais = [dados_animais[0]]
    encontrado = False

    for animal in dados_animais[1:]:
        if animal[ID] == string_id:
            encontrado = True
            print(f"\nEditando o animal {animal[NOME]}. Deixe em branco para manter o atual.")
            
            novo_nome = input(f"Novo nome [{animal[NOME]}]: ") or animal[NOME]
            nova_especie = input(f"Nova espécie [{animal[ESPECIE]}]: ") or animal[ESPECIE]
            nova_raca = input(f"Nova raça [{animal[RACA]}]: ") or animal[RACA]
            nova_idade = input(f"Nova idade [{animal[IDADE]}]: ") or animal[IDADE]
            nova_saude = input(f"Nova saúde [{animal[SAUDE]}]: ") or animal[SAUDE]
            nova_chegada = input(f"Nova chegada [{animal[CHEGADA]}]: ") or animal[CHEGADA]
            novo_comportamento = input(f"Novo comportamento [{animal[COMPORTAMENTO]}]: ") or animal[COMPORTAMENTO]
            
            animal = [
                animal[ID], novo_nome, nova_especie, nova_raca,
                nova_idade, nova_saude, nova_chegada, novo_comportamento
            ]
        temp_dados_animais.append(animal)

    if encontrado:
        with open('dados_animais.csv', 'w', newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq)
            escritor.writerows(temp_dados_animais)
        print("Cadastro updated com sucesso!")
    else:
        print("Animal não encontrado para edição.")


def excluir_i(id):
    dados_animais = carregar_dados()
    string_id = str(id)
    temp_dados_animais = [dados_animais[0]]
    animal_alvo = None

    for animal in dados_animais[1:]:
        if animal[ID] == string_id:
            animal_alvo = animal
            continue
        temp_dados_animais.append(animal)

    if animal_alvo:
        confirmacao = input(f"Deseja excluir os dados do animal {animal_alvo[NOME]}? (sim/nao): ")
        if confirmacao.lower() in ['s', 'sim']:
            with open('dados_animais.csv', 'w', newline="", encoding="utf-8") as arq:
                escritor = csv.writer(arq)
                escritor.writerows(temp_dados_animais)
            print("Deletado com sucesso.")
        else:
            print('Operação cancelada.')
    else:
        print(f'O animal com ID {id} não foi encontrado.')


def excluir_atividade(id_atv):
    dados_atividades = carregar_dados_atv()
    string_id = str(id_atv)
    temp_dados_atividades = [dados_atividades[0]]
    atividade_alvo = None

    for atv in dados_atividades[1:]:
        if atv[ATV_ID_ATIVIDADE] == string_id:
            atividade_alvo = atv
            continue
        temp_dados_atividades.append(atv)

    if atividade_alvo:
        confirmacao = input(f"Deseja excluir a atividade {atividade_alvo[ATV_NOME]}? (sim/nao): ")
        if confirmacao.lower() in ['s', 'sim']:
            with open('dados_atividades.csv', 'w', newline="", encoding="utf-8") as arq:
                escritor = csv.writer(arq)
                escritor.writerows(temp_dados_atividades)
            print("Atividade deletada com sucesso.")
        else:
            print('Operação cancelada.')
    else:
        print(f'A atividade com ID {id_atv} não foi encontrada.')

def cadastro_atividade(id, id_atv, nome_atv, data, responsavel):
    dados_animais = carregar_dados()
    string_id = str(id)
    animal_existe = False
    
    for animal in dados_animais[1:]:
        if animal[ID] == string_id:
            animal_existe = True
            break

    if animal_existe:
        dados_atividades = [id, id_atv, nome_atv, data, responsavel]
        salvar_atividades(dados_atividades)
        print("Atividade cadastrada com sucesso!\n")
    else:
        print("ID do animal é inválido. Cadastro rejeitado.\n")


def listar_atividades():
    dados_atividades = carregar_dados_atv()
    if len(dados_atividades) <= 1:
        print("Lista de atividades vazia.")
        return
    
    for atv in dados_atividades[1:]:
        print(f"\nID do Animal: {atv[ATV_ID_ANIMAL]}")
        print(f"ID da Atividade: {atv[ATV_ID_ATIVIDADE]}")
        print(f"Nome da Atividade: {atv[ATV_NOME]}")
        print(f"Data da Atividade: {atv[ATV_DATA]}")
        print(f"Nome do Responsável: {atv[ATV_RESPONSAVEL]}")

def editar_atividade(id_atv):
    dados_atividade = carregar_dados_atv()
    string_id = str(id_atv)
    temp_dados_atv = [dados_atividade[0]]
    encontrado = False

    for atv in dados_atividade[1:]:
        if atv[ATV_ID_ATIVIDADE] == string_id:
            encontrado = True
            
            nome_novo = input(f"Novo nome [{atv[ATV_NOME]}]: " or atv[ATV_NOME])
            data_nova = input(f"Nova data [{atv[ATV_DATA]}]: " or atv[ATV_DATA])
            responsavel_novo = input(f"Novo responsável [{atv[ATV_RESPONSAVEL]}]: " or atv[ATV_RESPONSAVEL])

        atv = [
            atv[ATV_ID_ANIMAL],
            atv[ATV_ID_ATIVIDADE],
            nome_novo,
            data_nova,
            responsavel_novo
        ]
        temp_dados_atv.append(atv)
        if encontrado:
            with open("dados_atividades.csv", "w", newline="", encoding = "utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(temp_dados_atv)
def busca_atv_id_i(id):
    dados_atividades = carregar_dados_atv()
    string_id = str(id)
    encontrado = False

    for atv in dados_atividades[1:]:
        if atv[ATV_ID_ANIMAL] == string_id:
            print("\nAtividade Encontrada:")
            print(f"ID da Atividade: {atv[ATV_ID_ATIVIDADE]}")
            print(f"Nome da Atividade: {atv[ATV_NOME]}")
            print(f"Data da Atividade: {atv[ATV_DATA]}")
            print(f"Nome do Responsável: {atv[ATV_RESPONSAVEL]}")
            encontrado = True
            
    if not encontrado:
        print("Nenhuma atividade encontrada para este ID de animal.\n")


def busca_atv_nome_atividade(nome_atv):
    dados_atividades = carregar_dados_atv()
    encontrado = False

    for atv in dados_atividades[1:]:
        if nome_atv.lower() in atv[ATV_NOME].lower():
            print("\nAtividade Encontrada:")
            print(f"ID do Animal: {atv[ATV_ID_ANIMAL]}")
            print(f"ID da Atividade: {atv[ATV_ID_ATIVIDADE]}")
            print(f"Nome da Atividade: {atv[ATV_NOME]}")
            print(f"Data da Atividade: {atv[ATV_DATA]}")
            print(f"Nome do Responsável: {atv[ATV_RESPONSAVEL]}")
            encontrado = True
            
    if not encontrado:
        print("Nenhuma atividade encontrada com esse nome.\n")


def contagem_regressiva_alertas(id):
    dados_atividades = carregar_dados_atv()
    string_id = str(id)
    animais_encontrados = []
    
    for i in dados_atividades[1:]:
        if i[ATV_ID_ANIMAL] == string_id:
            animais_encontrados.append(i)
            
    if not animais_encontrados:
        print("Nenhuma atividade pendente foi encontrada para este respectivo animal.")
        return
        
    print(f"\nAlertas para o animal com ID {id}:")
    dia_hoje = datetime.today()
    
    for i in animais_encontrados:
        try:
            nome_atv = i[ATV_NOME]
            data_atv = datetime.strptime(i[ATV_DATA], "%d/%m/%Y")
            responsavel_animal = i[ATV_RESPONSAVEL]
            diferenca_dias = (data_atv - dia_hoje).days + 1
            
            if diferenca_dias < 0:
                print(f"ATRASADA -> {nome_atv} | Responsável: {responsavel_animal} | Há: {abs(diferenca_dias)} dia(s)")
            elif diferenca_dias == 0:
                print(f"É HOJE A CONSULTA -> {nome_atv} | Responsável: {responsavel_animal}")
            elif diferenca_dias <= 7:
                print(f"FALTA POUCO TEMPO -> {nome_atv} | Responsável: {responsavel_animal} | Em {diferenca_dias} dia(s)")
            else:
                print(f"AINDA HÁ TEMPO -> {nome_atv} | Responsável: {responsavel_animal} | Em {diferenca_dias} dia(s)")
        except ValueError:
            print(f"Data inválida na atividade '{i[ATV_NOME]}', pulando registro.")
            continue


def menu_cadastro_animal():
    while True:
        try:
            id = int(input("Digite o id do animal: "))
            nome = str(input("Digite o nome do animal: "))
            especie = str(input("Digite a especie do animal: "))
            raca = str(input("Digite a raça do animal: "))
            idade = int(input("Digite a idade do animal: "))
            saude = str(input("Digite o estado de saude do animal: "))
            chegada = str(input("Digite a data de chegada do animal (dd/mm/aaaa): "))
            comportamento = str(input("Digite o comportamento do animal: "))

            cadastro_animal(id, nome, especie, raca, idade, saude, chegada, comportamento)
            break
        except ValueError:
            print("Algum dos dados inseridos foi inválido, tente novamente.")


def menu_cadastro_atividade():
    while True:
        try:
            id = int(input("Digite o id do animal: "))
            id_atv = int(input("Digite o id da atividade: "))
            nome_atv = str(input("Digite o nome da atividade: "))
            data = str(input("Digite a data de realização (dd/mm/aaaa): "))
            responsavel = str(input("Digite o nome do responsável: "))

            cadastro_atividade(id, id_atv, nome_atv, data, responsavel)
            break
        except ValueError:
            print("Algum dos dados inseridos foi inválido, tente novamente.")


def menu_busca_animal():
    while True:
        escolha = input("Tipo de busca:\n1 - Nome\n2 - ID\nEscolha: ")
        if escolha == '1' or escolha.lower() == "nome":
            nome_buscado = input("Digite o nome a ser buscado: ")
            busca_especifica_nome(nome_buscado)
            break
        elif escolha == '2' or escolha.lower() == "id":
            try:
                id = int(input("Digite o ID: "))
                if busca_especifica_id(id):
                    contagem_regressiva_alertas(id)
                break
            except ValueError:
                print("Entrada inválida.")
        else:
            print("Valor inválido.")


def menu_busca_atividade():
    while True:
        escolha = input("Forma de busca:\n1 - ID do animal\n2 - Nome da atividade\nEscolha: ")
        if escolha == '1' or escolha.lower() == "id":
            try:
                id = int(input("Digite o ID do animal: "))
                busca_atv_id_i(id)
                break
            except ValueError:
                print("Entrada inválida.")
        elif escolha == '2' or escolha.lower() == "nome":
            nome_atv = input("Digite o nome da atividade a ser buscado: ")
            busca_atv_nome_atividade(nome_atv)
            break
        else:
            print("Valor inválido.")


def menu():
    while True:
        opcao = input("""
O que você deseja fazer?

1 - Cadastrar animal
2 - Cadastrar atividades
3 - Listar animais
4 - Listar atividades
5 - Buscar animal por ID
6 - Buscar atividade
7 - Editar cadastro de animal
8 - Editar atividade
9 - Excluir cadastro de animal
11 - Sair
    
Escolha uma opção: """)

        if opcao == '1' or 'cadastro' in opcao.lower() and 'atv' not in opcao.lower():
            menu_cadastro_animal()
        elif opcao == '2' or 'atividade' in opcao.lower() and 'cadastrar' in opcao.lower():
            menu_cadastro_atividade()
        elif opcao == '3' or 'lista animais' in opcao.lower():
            listar_animais()
        elif opcao == '4' or 'lista atividades' in opcao.lower():
            listar_atividades()
        elif opcao == '5' or 'buscar animal' in opcao.lower():
            menu_busca_animal()
        elif opcao == '6' or 'buscar atividade' in opcao.lower():
            menu_busca_atividade()
        elif opcao == '7' or 'editar' in opcao.lower():
            try:
                id = int(input("Digite o id do cadastro a ser alterado: "))
                editar_animal_2(id)
            except ValueError:
                print("ID inválido.")
        elif opcao == '8' or 'editar atividade' in opcao.lower():
            try:
                id_atv = int(input("Digite o id da atividade que você deseja editar: "))
                editar_atividade(id_atv)
            except ValueError:
                print("O id digitado está inválido ou não existe, tente novamente.")
        elif opcao == '9' or 'excluir animal' in opcao.lower():
            try:
                id = int(input('Digite o id do animal a ser excluído: '))
                excluir_i(id)
            except ValueError:
                print("ID inválido.")
        elif opcao == '10' or 'excluir atividade' in opcao.lower():
            try:
                id_atv=input("id da atividade: ")
                excluir_atividade(id_atv)
            except ValueError:
                print("ID inválido.")
        elif opcao == '11' or 'sair' in opcao.lower():
            print("Encerrando sistema.")
            break
        else:
            print('A opção selecionada não foi encontrada.')