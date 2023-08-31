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

def separador(titulo = ''):
    global separador_tamanho

    if titulo:
        titulo = ("{}{}{}".format(' ', titulo, ' '))
        titulo_original = titulo

        i = 0
        while len(titulo) < separador_tamanho:
            titulo = ("{}{}{}".format('-' * i, titulo_original, '-' * i))
            i += 1

        if len(titulo) == (separador_tamanho + 1):
            titulo = titulo[:-1]

        print(titulo)
    else:
        print('-' * separador_tamanho)

def cadastrar_colaborador(id):
    global lista_colaboradores
    global separador

    separador("MENU CADASTRAR COLABORADOR")
    nome = input("Por favor, entre com o nome: ").title()
    setor = input("Por favor, entre com o setor: ")
    salario = int(input("Por favor, entre com o pagamento (R$): "))

    dicionario = {"id": id, "nome": nome, "setor": setor, "salario": salario}

    lista_colaboradores.append(dicionario)

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
                for key, value in colaborador.items():
                    print("{}: {}".format(key.title(), value))

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
    resposta = int(input(""))

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
                cadastrar_colaborador(id_global + 1)

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