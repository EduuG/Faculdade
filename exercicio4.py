from os import system, name
from time import sleep

# Função para limpar a tela de acordo com o sistema operacional utilizado
def limpar(): 

    # caso seja Windows
    if name == 'nt':
        system('cls')

    # caso seja Linux, Mac ou afins
    else:
        system('clear')

def realce(titulo): 
    print("{}{}{}".format('+', '-' * (len(titulo) + 2), '+'))
    print("{}{}{}".format('| ', titulo, ' |'))
    print("{}{}{}".format('+', '-' * (len(titulo) + 2), '+'))

def separador(titulo = '', limite = 0):
    global separador_tamanho

    if titulo:
        titulo = ("{}{}{}".format(' ', titulo, ' '))
        titulo_original = titulo

        if not limite:
            i = 0
            while len(titulo) < separador_tamanho:
                titulo = ("{}{}{}".format('-' * i, titulo_original, '-' * i))
                i += 1

            if len(titulo) == (separador_tamanho + 1):
                titulo = titulo[:-1]

        else:
            i = 0
            while len(titulo) < limite:
                titulo = ("{}{}{}".format('-' * i, titulo, '-' * i))
                i += 1

            if len(titulo) == (limite + 1):
                titulo = titulo[:-1]

        print(titulo)
    else:
        if not limite:
            print('-' * separador_tamanho)
        else:
            print('-' * limite)

def cadastrar_colaborador(id):
    global lista_colaboradores
    global limpar_tela
    global separador

    limpar_tela = False

    separador("MENU CADASTRAR COLABORADOR")
    nome = input("Por favor, entre com o nome: ").title()
    setor = input("Por favor, entre com o setor: ")
    salario = int(input("Por favor, entre com o pagamento (R$): "))

    dicionario = {"id": id, "nome": nome, "setor": setor, "salario": salario}

    lista_colaboradores.append(dicionario)

    print("\nColaborador cadastrado com sucesso!")
    #sleep(3)

def consultar_colaborador():
    global limpar_tela
    global separador

    while True:
        separador("MENU CONSULTAR COLABORADOR")
        print("1 - Consultar Todos")
        print("2 - Consultar por Id")
        print("3 - Consultar por Setor")
        print("4 - Retornar ao menu")
        separador()

        resposta = int(input("R: "))
        
        if resposta == 1: # consultar todos
            limpar_tela = False

            for colaborador in lista_colaboradores:
                print("")
                for key, value in colaborador.items():
                    print("{}: {}".format(key.title(), value))

            separador(limite = 25)
            continue
        
        elif resposta == 2: # consultar por id
            return 0
        elif resposta == 3: # consultar por setor
            return 0
        elif resposta == 4: # retornar ao menu
            return 0
        else:
            print("\nOpção inválida! Tente novamente.")
            sleep(3)

def remover_colaborador():
    while True:
        remover = int(input("Digite o ID do colaborador a ser removido: "))
        for colaborador in lista_colaboradores:
            if remover in colaborador["id"].items():
                print("Colaborador {} removido com sucesso!".format(colaborador["nome"]))
                if colaborador["id"] > remover:
                    colaborador["id"] -= 1
                lista_colaboradores.pop(remover - 1)
                break
            else:
                print("contrei n")
        break
            

limpar_tela = True

id_global = 0
lista_colaboradores = []

separador_tamanho = 74

while True:
    if limpar_tela == True:
        limpar()
        realce("Bem-vindo ao controle de Colaboradores do Eduardo Guimarães dos Santos")
    separador("MENU PRINCIPAL")
    print("Escolha a opção desejada:\n")
    print("1 - Cadastrar Colaborador")
    print("2 - Consultar Colaborador(res)")
    print("3 - Remover Colaborador")
    print("4 - Sair")
    separador()

    try:
        option = int(input("R: "))

        if option == 1:
            id_global += 1
            cadastrar_colaborador(id_global)

        elif option == 2:
            consultar_colaborador()

        elif option == 3:
            remover_colaborador()

        elif option == 4:
            print("\nAté mais!")
            sleep(3)
            break

        else:
            print("\nOpção inválida! Por favor, tente novamente.")
            sleep(3)
            continue
    
    except ValueError:
        print("Opção inválida! Por favor, tente novamente.")
        sleep(3)
