from os import system, name
from time import sleep

def limpar(): # função para limpar a tela de acordo com o sistema operacional utilizado

    # caso seja Windows
    if name == 'nt':
        system('cls')

    # caso seja Linux, Mac ou afins
    else:
        system('clear')

def realce(nome): # função apenas para estilizar a apresentação
    print("{}{}{}".format('+', '-' * (len(nome) + 2), '+'))
    print("{}{}{}".format('| ', nome, ' |'))
    print("{}{}{}".format('+', '-' * (len(nome) + 2), '+'))

def validar(pergunta, opcoes):
    """
    Função para validar resposta do usuário de acordo com o número de opções existentes.

    :param pergunta: Pergunta que será feita ao usuário.
    :param opcoes: Número de opções pela qual o usuário poderá escolher.
    """
    while True:
        try:
            resp = int(input(pergunta))

            if (resp <= 0) or (resp > opcoes):
                print('\nOpção inválida!')
                continue

            else:
                return resp

        except ValueError:
            print('\nOpção inválida!')
            continue

while True:

    limpar()

    realce("Bem-vindo a loja do Eduardo Guimarães dos Santos")

    # validando a resposta
    try:
        valor = float(input("Valor do produto: ")) # valor do produto
        quantidade = int(input("Quantidade do produto: ")) # quantidade do produto

    except ValueError:
        print("\nValor inválido!\n")
        sleep(3)
        continue

    if quantidade < 200: # se quantidade for menor que 200
        desconto = 0

    elif quantidade >= 200 and quantidade < 1000: # se quantidade for maior ou igual à 200 e menor que 1000
        desconto = 5

    elif quantidade >= 1000 and quantidade < 2000: # se quantidade for maior ou igual a 1000 e menor que 2000
        desconto = 10

    else: # se a quantidade for maior que 2000
        desconto = 15

    valor_SEM_desconto = valor * quantidade
    valor_COM_desconto = valor_SEM_desconto - (valor_SEM_desconto * desconto/100)

    print("\nValor SEM desconto: R$ {:.2f}".format(valor_SEM_desconto))
    print("Valor COM desconto: R$ {:.2f}\n".format(valor_COM_desconto))

    sleep(3)

    realce("Deseja calcular novamente?")
    print("1 - Sim\n2 - Não")

    resposta = validar('\nR: ', 2)

    if resposta == 1:
        continue
    elif resposta == 2:
        print('\nAté mais!')
        sleep(3)
        break
