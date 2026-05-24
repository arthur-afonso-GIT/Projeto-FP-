import csv

def criar_dados_animais():
    with open("dados_animais.csv", "w", newline="", encoding="utf-8") as dados:
        dados=csv.writer(dados)
        dados.writerow('id', 'nome', 'espécie', 'raça', 'idade', 'saúde', 'chegada', 'comportamento')

def criar_dados_atividades():
    with open("dados_atividades.csv", "w", newline="", encoding="utf-8") as dados:
        dados=csv.writer(dados)
        dados.writerow('id', 'id da atividade', 'nome da atividade', 'data', 'responsável')

def salvar_dados(dados_animais):
    #"dados_animais.csv" é o nome do arquivo /// "a" significa q vai adicionar no final e/ou criar o arquivo /// newline="" garante que a linha acabe de maneira correta /// encoding="utf-8" permite o uso de caracteres especiais
    with open("dados_animais.csv", "a", newline="", encoding="utf-8") as dados:
        dados=csv.writer(dados)
        dados.writerow(dados_animais)
        #json.dump(dados_animais, dados, indent=4)

def salvar_atividades(dados_atividades):
    with open("dados_atividades.csv", "a", newline="", encoding="utf-8") as dados:
        dados=csv.writer(dados)
        dados.writerow(dados_atividades)
        #json.dump(dados_atividades, dados, indent=4)

def carregar_dados():
    global dados_animais

    try:
        with open("dados_animais.csv", "r", encoding="utf-8") as dados:
            dados_animais = csv.reader(dados)

            dados_animais = {
                int(linha[0]): linha[1] for linha in dados if linha
            }

    except FileNotFoundError:
        dados_animais = {}

def carregar_dados_atv():
    global dados_atividades

    try:
        with open("dados_atividades.csv", "r", encoding="utf-8") as dados:
            dados_atividades = csv.reader(dados)

            dados_atividades = {
                int(linha[0]): linha[1] for linha in dados if linha
            }

    except FileNotFoundError:
        dados_atividades = {}

# item 1
def cadastro_i(id,nome, especie, raca, idade, saude, chegada, comportamento):
    if id in dados_animais:
        print("ID ja cadastrado")
        return
    dados_animais=[id,nome, especie, raca, idade, saude, chegada, comportamento]
    
    print("Cadastrado com sucesso!  ")
    salvar_dados(dados_animais)
    
    return dados_animais    

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
    if not dados_animais:
        print("Lista vazia. ")
        return
    
    for i in dados_animais.items():
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
    for i in dados_atividades.items():
        print(f" id da atividade: {i[0]}")
        print(f" id do i: {i[1]}")
        print(f" Nome da atividade:{i[2]}")
        print(f" Data da atividade:{i[3]}")
        print(f" Nome do responsável:{i[4]}")

# item 5
def busca_especifica_nome(nome):
    encontrados = []

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
    i = dados_animais.get(id)    
    
    if i:
        print(f"Animal encontrado: {id}")
        print(f" espécie: {i['especie']}")
        print(f" raça: {i['raca']}")
        print(f" Estado de saúde: {i['saude']}")
        print(f" comportamento: {i['comportamento']}")
        return True
    else:
        print(f"O i de id {id} não foi localizado")
        return False

# item 6
def busca_atv_id_i(id):
    for i in dados_atividades:
        if id in i:
            print(f" ID da atividade: {i}")
            print(f" Nome da atividade:{i['nome_atv']}")
            print(f" Data da atividade:{i['data']}")
            print(f" Nome do responsável:{i['responsavel']}")
            ciclos+=1
    if ciclos==0:
        print("id não existe\n")

# item 6
def busca_atv_id_atividade(id_atv):
    for i in dados_atividades:
        if id_atv in i:
            print(f" ID do i: {i[0]}")
            print(f" Nome da atividade:{i[1]}")
            print(f" Data da atividade:{i[2]}")
            print(f" Nome do responsável:{i[3]}")
            ciclos=1
    if ciclos==0:
        print("id não existe\n")
    
# item 7
def editar_i(id):
    i = dados_animais.get(id)
    if i:
        print(f"Editando dados do i: {i['nome']} (ID: {id})")
        print("Pressione Enter para manter o valor atual.")
        
        novo_nome = input(f"Novo nome [{i['nome']}]: ") or i['nome']
        nova_especie = input(f"Nova espécie [{i['especie']}]: ") or i['especie']
        nova_raca = input(f"Nova raça [{i['raca']}]: ") or i['raca']
        nova_idade = input(f"Nova idade [{i['idade']}]: ") or i['idade']
        nova_saude = input(f"Novo estado de saúde [{i['saude']}]: ") or i['saude']
        novo_comportamento = input(f"Novo comportamento [{i['comportamento']}]: ") or i['comportamento']

        dados_animais[id] = {
            'nome': novo_nome,
            'especie': nova_especie,
            'raca': nova_raca,
            'idade': nova_idade,
            'saude': nova_saude,
            'chegada': i['chegada'],
            'comportamento': novo_comportamento,
            'id': id
        }
        
        print(f"\nSucesso: O cadastro do i {id} foi atualizado!")
    else:
        print(f"Erro: O i de ID {id} não foi encontrado para edição.")
    salvar_dados()
    return dados_animais

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
    
    
def menu():

    while True:
        # usei aspas triplas pra ficar mais legivel, dps podem trocar por \n se quiser
        opcao = input("""
O que você deseja fazer?

1 - Cadastrar i
2 - Cadastrar atividades
3 - Listar animais
4 - Listar atividades
5 - Buscar i por ID
6 - Buscar atividade por i
7 - Editar cadastro
8 - Editar atividade
9 - Excluir cadastro
10 - Excluir atividade
11 - Sair
    
Escolha uma opção: \n """)

        if opcao == '1' or 'cadastrar' in opcao.lower():

            # id, nome, especie, raca, idade, saude, chegada, comportamento
            while True:
                try:
                    id = int(input("Digite o id do i: "))
                    nome = str(input("Digite o nome do i: "))
                    especie = str(input("Digite a especie do i: "))
                    raca = str(input("Digite a raça do i: "))
                    idade = int(input("Digite a idade do i: "))
                    saude = str(input("Digite o estado de saude do i: "))
                    chegada = str(input("Digite a data de chegada do i (formato dd/mm/aaaa): "))
                    comportamento = str(input("Digite o comportamento do i: "))

                    cadastro_i(
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
                    continue

        elif opcao=='2' or 'cadastrar atividades' in opcao.lower():
            while True:
                try:
                    id = int(input("Digite o id do i: "))
                    id_atv = int(input("Digite o id da atividade: "))
                    nome_atv = str(input("Digite o nome da atividade: "))
                    data = str(input("Digite a data de realização do serviço (formato dd/mm/aaaa):"))
                    responsavel = str(input("Digite o nome do responsável:"))
                    cadastro_atividade(id, id_atv, nome_atv, data, responsavel)

                    break
                except ValueError:
                    print("Algum dos dados inseridos foi invalido, tente novamente")
                    continue

        elif opcao == '3' or 'lista animais' in opcao.lower():
            listar_animais()
        elif opcao == '4' or 'lista atividades' in opcao.lower():
            listar_atividades()
        elif opcao == '5' or 'buscar i' in opcao.lower() or 'id i' in opcao.lower():
            while True:
                escolha=input("tipo de busca:\n1-nome\n2-ID")
                if escolha == 1 or escolha.lower() == "nome":
                    escolha=0
                    break
                elif escolha == 2 or escolha.lower() == "id":
                    escolha=1
                    break
                else:
                    print("valor inválido")

            while escolha==0:
                try:
                    id = int(input("Digite o ID: "))
                    break

                except ValueError:
                    print("Entrada invalida")
                    continue

            busca_especifica_id(id)

            while escolha == 1:

                try:
                    nome_buscado = str(input("Digite o nome a ser buscado: "))
                    busca_especifica_nome(nome_buscado)
                    break
                except ValueError:
                    print("i não registrado")
                    continue


        elif opcao == '6' or 'buscar atividade' in opcao.lower() or 'id atividade' in opcao.lower():
            while True:
                escolha=input("Deseja buscar por qual ID?\n1-i\n2-atividade")
                if escolha == 1 or escolha.lower() == "i":
                    escolha=0
                    break
                elif escolha == 2 or escolha.lower() == "id":
                    escolha=1
                    break
                else:
                    print("valor inválido")

            while escolha==0:
                try:
                    id = int(input("Digite o ID: "))
                    break

                except ValueError:
                    print("Entrada invalida")
                    continue

            busca_atv_id_i(id)

            while escolha == 1:

                try:
                    id_atv = str(input("Digite o ID a ser buscado: "))
                    busca_atv_id_atividade(id_atv)
                    break
                except ValueError:
                    print("ID não registrado")
                    continue

        elif opcao == '7' or 'editar' in opcao.lower():
            id = int(input("Digite o id do cadastro a ser alterado: "))
            editar_i(id)

        elif opcao == '9' or 'exclui' in opcao.lower():
            id = int(input('Digite o id do i a ser excluido: '))
            excluir_i(id)

        elif opcao == '11' or 'sair' in opcao.lower():
            print("Encerrando sistema")
            break

        else:
            print('A opção selecionada não foi encontrada')