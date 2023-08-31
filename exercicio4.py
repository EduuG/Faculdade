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

# Função apenas para estilizar a apresentação
def realce(tipo, titulo = '', tamanho = 0): 
    tamanho_linha = 43

    if tipo == 1:
        print("{}{}{}".format('+', '-' * (len(titulo) + 2), '+'))
        print("{}{}{}".format('| ', titulo, ' |'))
        print("{}{}{}".format('+', '-' * (len(titulo) + 2), '+'))

    elif tipo == 2:
        tamanho_nome = len(titulo)
        metade_nome = tamanho_nome // 2
        linha = '-' * (tamanho_linha - tamanho_nome)
        print("{} {} {}".format(linha, titulo, linha))

    elif tipo == 3:
        print('-' * tamanho_linha)


def cadastrar_colaborador(id):
    global lista_colaboradores

    nome = input("Por favor, entre com o nome: ")
    setor = input("Por favor, entre com o setor: ")
    pagamento = int(input("Por favor, entre com o pagamento (R$): "))

    dicionario = {"id": id, "nome": nome, "setor": setor, "pagamento": pagamento}

    lista_colaboradores.append(dicionario)

def consultar_colaborador():
    print("1 - Consultar Todos")
    print("2 - Consultar por Id")
    print("3 - Consultar por Setor")
    print("4 - Retornar ao menu")

    resposta = int(input("\nR: "))
    
    if resposta == 1: # consultar todos
        for colaborador in lista_colaboradores:
            for dados in colaborador:
                print(dados)
       
    elif resposta == 2: # consultar por id
        return 0
    elif resposta == 3: # consultar por setor
        return 0
    elif resposta == 4: # retornar ao menu
        return 0

limpar_tela = True
id_global = 0
lista_colaboradores = []
tamanho_linha = 0

while True:
    if limpar_tela == True:
        limpar()
        tamanho_linha = realce(1, "Bem-vindo ao controle de Colaboradores do Eduardo Guimarães dos Santos")
        realce(2, "MENU PRINCIPAL", tamanho_linha)
        print("Escolha a opção desejada:")
        print("1 - Cadastrar Colaborador")
        print("2 - Consultar Colaborador(res)")
        print("3 - Remover Colaborador")
        print("4 - Sair")
        realce(3)

        try:
            option = int(input("\nR: "))

            if option == 1:
                cadastrar_colaborador()

            elif option == 2:
                consultar_colaborador()

            elif option == 3:
                remover_colaborador()

            elif option == 4:
                break

            else:
                print("\nOpção inválida! Por favor, tente novamente.")
                sleep(3)
                continue
        
        except ValueError:
            print("Opção inválida! Por favor, tente novamente.")
            sleep(3)