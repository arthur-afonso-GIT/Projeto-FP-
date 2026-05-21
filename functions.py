import json
def salvar_dados():
    with open("dados_animais.json", "w") as dados:
        json.dump(dados_animais, dados, indent=4)

def salvar_atividades():
    with open("dados_atividades.json", "w") as dados:
        json.dump(dados_animais, dados, indent=4)

def carregar_dados():
    global dados_animais

    try:
        with open("dados_animais.json", "r") as dados:
            dados_animais = json.load(dados)

            dados_animais = {
                int(k): v for k, v in dados_animais.items()
            }

    except FileNotFoundError:
        dados_animais = {}

def carregar_dados():
    global dados_atividades

    try:
        with open("dados_animais.json", "r") as dados:
            dados_atividades = json.load(dados)

            dados_atividades = {
                int(k): v for k, v in dados_atividades.items()
            }

    except FileNotFoundError:
        dados_atividades = {}

# item 1
def cadastro_animal(id,nome, especie, raca, idade, saude, chegada, comportamento):
    if id in dados_animais:
        print("ID ja cadastrado")
        return
    dados_animais[id] = {
        "nome": nome,
        "especie": especie,
        "raca": raca,
        "idade": idade,
        "saude": saude,
        "chegada": chegada,
        "comportamento": comportamento,
        "id": id
    }
    
    print("Cadastrado com sucesso!  ")
    salvar_dados(   )
    
    return dados_animais    

#item 2
def cadastro_atividade(id,id_atv, nome_atv, data, responsavel):
    if id in dados_animais:
        dados_atividades[id_atv]={
            "id": id,
            "nome_atv": nome_atv,
            "data": data,
            "responsavel": responsavel
        }
        print("Cadastrado com sucesso!\n")
        salvar_dados(   )
    else:
        print("id inválido\n")


# item 3
def listar_animais():   
    if not dados_animais:
        print("Lista vazia. ")
        return
    
    for i, j in dados_animais.items():
        print(f" id:\t{i}")
        print(f" espécie:\t{j['especie']}")
        print(f" raça:\t{j['raca']}")
        print(f" Estado de saúde:\t{j['saude']}")
        print(f" comportamento:\t{j['comportamento']}")
        print(f" Nome:\t{j['nome']}")

#item 4
def listar_atividades():
    if not dados_atividades:
        print("Lista vazia. ")
        return
    for i, j in dados_atividades.items():
        print(f" id da atividade:\t{i}")
        print(f" id do animal:\t{j['id']}")
        print(f" Nome da atividade:\t{j['nome_atv']}")
        print(f" Data da atividade:\t{j['data']}")
        print(f" Nome do responsável:\t{j['responsavel']}")

def busca_especifica_nome(nome):
    encontrados = []

    for dados in dados_animais.values():
        if dados['nome'].lower() == nome.lower():
            encontrados.append(dados)
    
    if encontrados:
        print(f"\nResultados para '{nome}': {len(encontrados)} encontrado(s)")
        for animal in encontrados:
            print(f"ID: {animal['id']}")
            print(f"Nome: {animal['nome']}")
            print(f"Espécie: {animal['especie']}")
            print(f"Raça: {animal['raca']}")
            print(f"Saúde: {animal['saude']}")
    else:
        print(f"\nNenhum animal chamado '{nome}' foi localizado.")

# item 5
def busca_especifica_id(id):
    animal = dados_animais.get(id)    
    
    if animal:
        print(f"Animal encontrado: {id}")
        print(f" espécie: {animal['especie']}")
        print(f" raça: {animal['raca']}")
        print(f" Estado de saúde: {animal['saude']}")
        print(f" comportamento: {animal['comportamento']}")
        return True
    else:
        print(f"O animal de id {id} não foi localizado")
        return False
    
# item 7
def editar_animal(id):
    animal = dados_animais.get(id)
    if animal:
        print(f"Editando dados do animal: {animal['nome']} (ID: {id})")
        print("Pressione Enter para manter o valor atual.")
        
        novo_nome = input(f"Novo nome [{animal['nome']}]: ") or animal['nome']
        nova_especie = input(f"Nova espécie [{animal['especie']}]: ") or animal['especie']
        nova_raca = input(f"Nova raça [{animal['raca']}]: ") or animal['raca']
        nova_idade = input(f"Nova idade [{animal['idade']}]: ") or animal['idade']
        nova_saude = input(f"Novo estado de saúde [{animal['saude']}]: ") or animal['saude']
        novo_comportamento = input(f"Novo comportamento [{animal['comportamento']}]: ") or animal['comportamento']

        dados_animais[id] = {
            'nome': novo_nome,
            'especie': nova_especie,
            'raca': nova_raca,
            'idade': nova_idade,
            'saude': nova_saude,
            'chegada': animal['chegada'],
            'comportamento': novo_comportamento,
            'id': id
        }
        
        print(f"\nSucesso: O cadastro do animal {id} foi atualizado!")
    else:
        print(f"Erro: O animal de ID {id} não foi encontrado para edição.")
    salvar_dados()
    return dados_animais

# item 9
def excluir_animal(id):
    animal = dados_animais.get(id)
    if animal:
        confirmacao = str(input(f"Deseja excluir os dados do animal {animal['nome']}?(sim ou não) "))
        if confirmacao.lower() == 's' or confirmacao.lower() == 'sim':
            del dados_animais[id]
            print("Deletado com sucesso")
        else:
            print('Operação cancelada.')
    else:
        print(f'O animal com id {id} não foi encontrado')
        
    salvar_dados()