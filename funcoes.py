import csv
import random
from datetime import datetime
from constantes import *
from persistencia import (
    carregar_dados, carregar_dados_atv, salvar_dados, salvar_atividades
)

def gerar_id_aleatorio(tipo='animal'):
    if tipo == 'animal':
        return str(random.randint(1000, 9999))
    else:
        return str(random.randint(10000, 99999))

def cadastro_animal(id, nome, especie, raca, idade, saude, chegada, comportamento):
    dados_animais = carregar_dados()
    id_string = str(id)
    
    for i in dados_animais:
        if id_string in i:
            print("ID já cadastrado!")
            return
            
    dados_animal = [id, nome, especie, raca, idade, saude, chegada, comportamento]
    salvar_dados(dados_animal)
    print("Cadastrado com sucesso!")

def listar_animais():   
    dados_animais = carregar_dados()
    if len(dados_animais) <= 1:
        print("A lista de animais está vazia.")
        return
    
    for i in dados_animais[1:]:
        print(f" ID: {i[ID]}")
        print(f" Nome: {i[NOME]}")
        print(f" Idade: {i[IDADE]}")
        print(f" Espécie: {i[ESPECIE]}")
        print(f" Raça: {i[RACA]}")
        print(f" Estado de saúde: {i[SAUDE]}")
        print(f" Comportamento: {i[COMPORTAMENTO]}")
        print(f" Data de chegada: {i[CHEGADA]}")
        print("-" * 30)

def listar_atividades():
    dados_atividades = carregar_dados_atv()
    if len(dados_atividades) <= 1:
        print("A lista de atividades está vazia.")
        return
        
    for i in dados_atividades[1:]:
        print(f" ID do Animal: {i[ATV_ID_ANIMAL]}")
        print(f" ID da Atividade: {i[ATV_ID_ATIVIDADE]}")
        print(f" Nome da Atividade: {i[ATV_NOME]}")
        print(f" Data da Atividade: {i[ATV_DATA]}")
        print(f" Nome do Responsável: {i[ATV_RESPONSAVEL]}")
        print("-" * 30)

def busca_especifica_nome(nome):
    encontrados = []
    dados_animais = carregar_dados()
    for i in dados_animais[1:]:
        if i[NOME].lower() == nome.lower():
            encontrados.append(i)
    
    if encontrados:
        print(f"\nResultados para {nome}: {len(encontrados)} encontrado(s)")
        for i in encontrados:
            print(f"\nID: {i[ID]}")
            print(f"Nome: {i[NOME]}")
            print(f"Espécie: {i[ESPECIE]}")
            print(f"Raça: {i[RACA]}")
            print(f"Saúde: {i[SAUDE]}")
    else:
        print(f"\nNenhum animal chamado '{nome}' foi localizado.")
        
    return encontrados

def busca_especifica_id(id):
    id_string = str(id)
    dados_animais = carregar_dados()
    for i in dados_animais[1:]:
        if id_string == i[ID]:
            print(f"\nID: {i[ID]}")
            print(f"Nome: {i[NOME]}")
            print(f"Espécie: {i[ESPECIE]}")
            print(f"Raça: {i[RACA]}")
            print(f"Saúde: {i[SAUDE]}")
            return True
    print(f"O animal com o id {id} não foi encontrado.")
    return False

def busca_atv_id_i(id):
    dados_atividades = carregar_dados_atv()
    string_id = str(id)
    ciclos = 0
    for i in dados_atividades[1:]:
        if string_id == i[ATV_ID_ANIMAL]:
            print(f" ID da atividade: {i[ATV_ID_ATIVIDADE]}")
            print(f" Nome da atividade: {i[ATV_NOME]}")
            print(f" Data da atividade: {i[ATV_DATA]}")
            print(f" Nome do responsável: {i[ATV_RESPONSAVEL]}")
            print("-" * 30)
            ciclos += 1
    if ciclos == 0:
        print("Nenhuma atividade encontrada para este ID.\n")

def busca_atv_nome_atividade(nome_atv):
    dados_atividades = carregar_dados_atv()
    ciclos = 0
    for i in dados_atividades[1:]:
        if nome_atv in i[ATV_NOME]:
            print(f" ID do Animal: {i[ATV_ID_ANIMAL]}")
            print(f" ID da Atividade: {i[ATV_ID_ATIVIDADE]}")
            print(f" Nome da Atividade: {i[ATV_NOME]}")
            print(f" Data da Atividade: {i[ATV_DATA]}")
            print(f" Nome do responsável: {i[ATV_RESPONSAVEL]}")
            print("-" * 30)
            ciclos = 1
    if ciclos == 0:
        print("Nenhuma atividade com esse nome foi encontrada.\n")

def editar_animal(id):
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
            csv.writer(arq).writerows(temp_dados_animais)
        print("Cadastro atualizado com sucesso!")
    else:
        print("Animal não encontrado para edição.")

def editar_atividade(id_atv):
    dados_atividade = carregar_dados_atv()
    string_id = str(id_atv)
    temp_dados_atv = [dados_atividade[0]]
    encontrado = False

    for atv in dados_atividade[1:]:
        if atv[ATV_ID_ATIVIDADE] == string_id:
            encontrado = True
            print(f"\nEditando atividade {atv[ATV_NOME]}. Deixe em branco para manter.")
            
            nome_novo = input(f"Novo nome [{atv[ATV_NOME]}]: ") or atv[ATV_NOME]
            data_nova = input(f"Nova data [{atv[ATV_DATA]}]: ") or atv[ATV_DATA]
            responsavel_novo = input(f"Novo responsável [{atv[ATV_RESPONSAVEL]}]: ") or atv[ATV_RESPONSAVEL]

            atv = [
                atv[ATV_ID_ANIMAL],
                atv[ATV_ID_ATIVIDADE],
                nome_novo,
                data_nova,
                responsavel_novo
            ]
        temp_dados_atv.append(atv)

    if encontrado:
        with open("dados_atividades.csv", "w", newline="", encoding="utf-8") as arquivo:
            csv.writer(arquivo).writerows(temp_dados_atv)
        print("Atividade atualizada com sucesso!")
    else:
        print("Atividade não encontrada.")

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
                csv.writer(arq).writerows(temp_dados_animais)
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
                csv.writer(arq).writerows(temp_dados_atividades)
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

def  sugestao_personalizada(especie, idade, comportamento):
    especie = especie.lower()
    comportamento = comportamento.lower()
    adotantes = []
    cuidados = []
    compatibilidade = []
    atividades = []

    if comportamento == "bravo" or comportamento == "agressivo":
        adotantes.append("Tutores experientes, sem crianças ou outros animais em casa.")
    elif comportamento == "agitado" or comportamento == "brincalhão":
        adotantes.append("Famílias agitadas, casa com quintal e dispostas a passear todos os dias.")
    elif comportamento == "tímido" or comportamento == "assustado":
        adotantes.append("Famílias calmas, rotina tranquila e tutores pacientes.")
    else:
        adotantes.append("Qualquer perfil de tutor responsável.")
    
    if idade <= 1:
        cuidados.append("Necessita de vacinação em dia e acompanhamento do crescimento.")
        atividades.append("Brincadeiras educativas e adestramento.")
    elif idade >= 8:
        cuidados.append("Realizar check-ups veterinários periódicos.")
        atividades.append("Exercícios leves e caminhadas diárias.")
    else:
        cuidados.append("Manter vacinas anuais e alimentação balanceada.")
        atividades.append("Passeios diários.")

    if especie == "cachorro":
        compatibilidade.append("Rotina de alimentação equilibrada e passeios diários.")
    elif especie == "gato":
        compatibilidade.append("Telagem nas janelas e enriquecimento ambiental vertical.")
    else:
        compatibilidade.append("Pesquisar necessidades específicas da espécie.")

    print(f"\n=== Sugestões Personalizadas ===")
    print(f"• Possível adotante: {adotantes[0]}")
    print(f"• Cuidados especiais: {cuidados[0]}")
    print(f"• Compatibilidade: {compatibilidade[0]}")
    print(f"• Atividades recomendadas: {atividades[0]}")

def ranking_aptidao():
    dados_animais = carregar_dados()
    ranking = []
    
    pontuacao_saude = {
        "boa": 20,
        "saudável": 20,
        "ótima": 20,
        "regular": 10,
        "precisa de atenção leve": 10,
        "ruim": 5,
        "precisa de muita atenção": 5
    }

    pontuacao_comportamento = {
        "dócil": 30,
        "docil": 30,
        "brincalhão": 30,
        "brincalhao": 30,
        "calmo": 30,
        "agitado": 20,
        "tímido": 20,
        "assustado":10,
        "bravo": 5,
        "agressivo": 5
    }
    
    if len(dados_animais) <= 1:
        print("Nenhum animal cadastrado.")
        return
    
    for animal in dados_animais[1:]:

        saude = animal[SAUDE].strip().lower()
        comportamento = animal[COMPORTAMENTO].strip().lower()

        pontos = 0
        pontos += pontuacao_saude.get(saude, 0)
        pontos += pontuacao_comportamento.get(comportamento, 0)

        ranking.append([
            animal[NOME],
            animal[ESPECIE],
            saude,
            comportamento,
            pontos
        ])

    for i in range(len(ranking)):
        for j in range(i + 1, len(ranking)):
            if ranking[j][4] > ranking[i][4]:
                ranking[i], ranking[j] = ranking[j], ranking[i]

    print(f"\n=== Ranking de Animais Mais Aptos Para Adoção ===")

    for animal in ranking:
        if animal[4] >= 50:
            aptidao = "Muito apto para adoção."
        elif animal[4] >= 40:
            aptidao = "Medianamente apto para adoção."
        else:
            aptidao = "Pouco apto para adoção."

        print(f"Nome: {animal[0]}")
        print(f"Espécie: {animal[1]}")
        print(f"Saúde: {animal[2]}")
        print(f"Comportamento: {animal[3]}")
        print(f"Aptidão: {aptidao}")
        print("-" * 30)

def cadastro_funcionario(nome): 
    with open("dados_funcionario.csv", "a", newline="", encoding="utf-8") as arq:
        escritor = csv.writer(arq)

        if arq.tell() == 0:
            escritor.writerow(["nome","pontos"])

        escritor.writerow([nome, 0])
    print("Funcionário cadastrado com sucesso!")

def adicionar_pontos_funcionario(nome_funcionario, tarefa):
    pontuacoes = {
        "banho": 5,
        "vacina": 10,
        "adocao": 20
    }

    if tarefa.lower() not in pontuacoes:
        print("Tarefa inválida.")
        return
    dados_funcionarios = []

    with open("dados_funcionario.csv", "r", newline="", encoding="utf-8") as arq:
        leitor = csv.reader(arq)
        dados_funcionarios = list(leitor)

    encontrado = False

    for funcionario in dados_funcionarios[:1]:
        if funcionario[0].lower() == nome_funcionario.lower():
            funcionario[1] = str(int(funcionario[1]) + pontuacoes[tarefa.lower()])

            encontrado = True
            break
    
    if encontrado:
        with open("dados_funcionario.csv", "w", newline="", encoding="utf-8") as arq:
            escritor = csv.writer(arq)
            escritor.writerows(dados_funcionarios)

        print(f"{nome_funcionario} ganhou {pontuacoes[tarefa.lower()]} pontos!")

    else:
        print("Funcionário não encontrado.")

def ranking_funcionarios():
    with open("dados_funcionario.csv", "r", newline="", encoding="utf-8") as arq:
        leitor = csv.reader(arq)
        dados_funcionarios = list(leitor)

    if len(dados_funcionarios) <= 1:
        print("nenhum funcionario cadastrado.")
        return

    ranking = []

    for funcionario in dados_funcionarios[1:]:
        ranking.append([funcionario[0],int(funcionario[1])])

    for i in range(len(ranking)):
        for j in range(i+1, len(ranking)):
            if ranking[j][1] > ranking[j][1]:
                ranking[i], ranking[j] =  ranking[j], ranking[i]

    print("\n=== Ranking de Funcionários ===")

    posicao = 1

    for funcionario in ranking:
        print(
            f"{posicao}º Lugar - "
            f"{funcionario[0]} - "
            f"{funcionario[1]} pontos"
        )
        posicao += 1