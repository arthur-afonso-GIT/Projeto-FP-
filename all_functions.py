import csv
import os
from datetime import datetime

def criar_dados_animais():
    with open("dados_animais.csv", "w", newline="", encoding="utf-8") as dados:
        dado='id', 'nome', 'espécie', 'raça', 'idade', 'saúde', 'chegada', 'comportamento'
        dados=csv.writer(dados)
        dados.writerow(dado)

def criar_dados_atividades():
    with open("dados_atividades.csv", "w", newline="", encoding="utf-8") as dados:
        dado='id', 'id da atividade', 'nome da atividade', 'data', 'responsável'
        dados=csv.writer(dados)
        dados.writerow(dado)

def salvar_dados(dados_animal):
    #"dados_animais.csv" é o nome do arquivo /// "a" significa q vai adicionar no final e/ou criar o arquivo /// newline="" garante que a linha acabe de maneira correta /// encoding="utf-8" permite o uso de caracteres especiais
    with open("dados_animais.csv", "a", newline="", encoding="utf-8") as dados:
        dados=csv.writer(dados)
        dados.writerow(dados_animal)
        #json.dump(dados_animais, dados, indent=4)

def salvar_atividades(dados_atividades):
    with open("dados_atividades.csv", "a", newline="", encoding="utf-8") as dados:
        dados=csv.writer(dados)
        dados.writerow(dados_atividades)
        #json.dump(dados_atividades, dados, indent=4)

def carregar_dados():
    global dados_animais
    with open("dados_animais.csv", "r", encoding="utf-8") as dados:
        dados_animais = list(csv.reader(dados))
        return dados_animais

def carregar_dados_atv():
    global dados_atividades

    with open("dados_atividades.csv", "r", encoding="utf-8") as dados:
        dados_atividades = list(csv.reader(dados))

# item 1
def cadastro_animal(id,nome, especie, raca, idade, saude, chegada, comportamento):
    dados_animais=carregar_dados()
    id_string=str(id)
    if id_string in dados_animais:
        print("ID ja cadastrado")
        return
    dados_animal=[id, nome, especie, raca, idade, saude, chegada, comportamento]
    salvar_dados(dados_animal)
    print("Cadastrado com sucesso!  ")
      

#item 2
def cadastro_atividade(id,id_atv, nome_atv, data, responsavel):
    if id in dados_animais:
        dados_atividades=[id,id_atv, nome_atv, data, responsavel]
        print("Cadastrado com sucesso!\n")
        salvar_atividades(dados_atividades)
    else:
        print("id inválido\n")


# item 3
def listar_animais():   
    dados_animais=carregar_dados()
    if not dados_animais:
        print("Lista vazia. ")
        return
    
    for i in dados_animais:
            print(f" id: {i[0]}")
            print(f" espécie: {i[1]}")
            print(f" raça: {i[2]}")
            print(f" Estado de saúde: {i[3]}")
            print(f" comportamento: {i[4]}")
            print(f" Nome: {i[5]}")

#item 4
def listar_atividades():
    if not dados_atividades:
        print("Lista vazia. ")
        return
    
    for i in dados_atividades:
        print(f" id da atividade: {i[0]}")
        print(f" id do i: {i[1]}")
        print(f" Nome da atividade:{i[2]}")
        print(f" Data da atividade:{i[3]}")
        print(f" Nome do responsável:{i[4]}")

# item 5
def busca_especifica_nome(nome):
    encontrados = [[]]

    for dados in dados_animais.values():
        if dados['nome'].lower() == nome.lower():
            encontrados.append(dados)
    
    if encontrados:
        print(f"\nResultados para '{nome}': {len(encontrados)} encontrado(s)")
        for i in encontrados:
            print(f"ID: {i[0]}")
            print(f"Nome: {i[1]}")
            print(f"Espécie: {i[2]}")
            print(f"Raça: {i[3]}")
            print(f"Saúde: {i[4]}")
    else:
        print(f"\nNenhum animal chamado '{nome}' foi localizado.")

# item 5
def busca_especifica_id(id):
    for i in dados_animais:
        if id in i:
            print(f"Animal encontrado: {i[0]}")
            print(f" espécie: {i[1]}")
            print(f" raça: {i[2]}")
            print(f" Estado de saúde: {i[3]}")
            print(f" comportamento: {i[4]}")
            return True
    else:
        print(f"O animal de id {id} não foi localizado")
        return False

# item 6
def busca_atv_id_i(id):
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
def editar_animal(id,nome, especie, raca, idade, saude, chegada, comportamento):
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




# item 9
def excluir_i(id):
    i = dados_animais.get(id)
    if i:
        confirmacao = str(input(f"Deseja excluir os dados do i {i['nome']}?(sim ou não) "))
        if confirmacao.lower() == 's' or confirmacao.lower() == 'sim':
            del dados_animais[id]
            print("Deletado com sucesso")
        else:
            print('Operação cancelada.')
    else:
        print(f'O i com id {id} não foi encontrado')
        
    salvar_dados()
    
    
def menu_cadastro_animal():

    while True:
        try:
            id = int(input("Digite o id do animal: "))
            nome = str(input("Digite o nome do animal: "))
            especie = str(input("Digite a especie do animal: "))
            raca = str(input("Digite a raça do animal: "))
            idade = int(input("Digite a idade do animal: "))
            saude = str(input("Digite o estado de saude do animal: "))
            chegada = str(input("Digite a data de chegada do animal (formato dd/mm/aaaa): "))
            comportamento = str(input("Digite o comportamento do animal: "))

            cadastro_animal(
                id,
                nome,
                especie,
                raca,
                idade,
                saude,
                chegada,
                comportamento
            )

            break

        except ValueError:
            print("Algum dos dados inseridos foi invalido, tente novamente")


def menu_cadastro_atividade():

    while True:
        try:
            id = int(input("Digite o id do animal: "))
            id_atv = int(input("Digite o id da atividade: "))
            nome_atv = str(input("Digite o nome da atividade: "))
            data = str(input("Digite a data de realização do serviço (formato dd/mm/aaaa): "))
            responsavel = str(input("Digite o nome do responsável: "))

            cadastro_atividade(
                id,
                id_atv,
                nome_atv,
                data,
                responsavel
            )

            break

        except ValueError:
            print("Algum dos dados inseridos foi invalido, tente novamente")


def menu_busca_animal():

    while True:

        escolha = input(
            "tipo de busca:\n"
            "1-nome\n"
            "2-ID\n"
        )

        if escolha == '1' or escolha.lower() == "nome":

            nome_buscado = str(input("Digite o nome a ser buscado: "))

            busca_especifica_nome(nome_buscado)

            break

        elif escolha == '2' or escolha.lower() == "id":

            while True:
                try:
                    id = int(input("Digite o ID: "))

                    busca_especifica_id(id)
                    contagem_regressiva_alertas(id)

                    break

                except ValueError:
                    print("Entrada invalida")

            break

        else:
            print("valor inválido")


def menu_busca_atividade():

    while True:

        escolha = input(
            "forma de busca:\n"
            "1-ID do animal\n"
            "2-Nome da atividade\n"
        )

        if escolha == '1' or escolha.lower() == "id":

            while True:
                try:
                    id = int(input("Digite o ID: "))

                    busca_atv_id_i(id)

                    break

                except ValueError:
                    print("Entrada invalida")

            break

        elif escolha == '2' or escolha.lower() == "nome":

            nome_atv = str(input("Digite o nome a ser buscado: "))

            busca_atv_nome_atividade(nome_atv)

            break

        else:
            print("valor inválido")


def contagem_regressiva_alertas(id):
    carregar_dados_atv()
    string_id = str(id)
    animais_encontrados = []
    for i in dados_atividades[1:]:
        if i[0] == string_id:
            animais_encontrados.append(i)
    if not animais_encontrados:
        print(f"Nenhuma atividade pendente foi encontrada para este respectivo animal")
        return
    print(f"\n---- ALERTAS PARA O ANIMAL COM ID {id} ---\n")
    dia_hoje = datetime.today()
    for i in animais_encontrados:
        try:
            nome_atv = i[2]
            data_atv = datetime.strptime(i[3], "%d/%m/%Y")
            responsavel_animal = i[4]
            diferenca_dias = (data_atv - dia_hoje).days 
            if diferenca_dias < 0:
                print(f"ATRASADA --> {nome_atv} | Responsável pelo animal: {responsavel_animal} | Consulta prevista há: {abs(diferenca_dias)} dia(s)")
            elif diferenca_dias == 0:
                print(f"É HOJE A CONSULTA --> {nome_atv} | Responsável pelo animal: {responsavel_animal} | Consulta prevista para hoje.")
            elif diferenca_dias <=7:
                print(f"FALTA POUCO TEMPO --> {nome_atv} | Responsável pelo animal: {responsavel_animal} | Consulta prevista para {diferenca_dias} dia(s)")
            else:
                print(f"AINDA HÁ TEMPO --> {nome_atv} | Responsável pelo animal: {responsavel_animal} | Consulta prevista para {diferenca_dias} dia(s)")
        except ValueError:
            print(f"Data inválida na atividade '{i[2]}', vamos pular isso.")
            continue     
def menu():

     while True:

        # usei aspas triplas pra ficar mais legivel, dps podem trocar por \n se quiser
        opcao = input("""
O que você deseja fazer?

1 - Cadastrar animal
2 - Cadastrar atividades
3 - Listar animais
4 - Listar atividades
5 - Buscar animal por ID
6 - Buscar atividade por animal
7 - Editar cadastro
8 - Editar atividade
9 - Excluir cadastro
10 - Excluir atividade
11 - Sair
    
Escolha uma opção: \n """)

        if opcao == '1' or 'cadastrar' in opcao.lower():

            menu_cadastro_animal()

        elif opcao == '2' or 'cadastrar atividades' in opcao.lower():

            menu_cadastro_atividade()

        elif opcao == '3' or 'lista animais' in opcao.lower():

            listar_animais()

        elif opcao == '4' or 'lista atividades' in opcao.lower():

            listar_atividades()

        elif opcao == '5' or 'buscar animal' in opcao.lower() or 'id animal' in opcao.lower():

            menu_busca_animal()

        elif opcao == '6' or 'buscar atividade' in opcao.lower() or 'id atividade' in opcao.lower():

            menu_busca_atividade()

        elif opcao == '7' or 'editar animal' in opcao.lower():

            id = int(input("Digite o id do cadastro a ser alterado: "))

            editar_animal(id)

        elif opcao == '9' or 'exclui' in opcao.lower():

            id = int(input('Digite o id do animal a ser excluido: '))

            excluir_i(id)

        elif opcao == '11' or 'sair' in opcao.lower():

            print("Encerrando sistema")

            break

        else:

            print('A opção selecionada não foi encontrada')


            

