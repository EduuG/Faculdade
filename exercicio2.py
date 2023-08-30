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

# Função para imprimir o cardápio
def cardapio(): 
    print("Bem-vindo à sorveteria do Eduardo Guimarães dos Santos")
    print("{}{}{}".format('-' * 38, "Cardápio", '-' * 39))
    print("|  N° DE BOLAS ", "| Sabor Tradicional (tr)", "| Sabor Premium (pr)", "| Sabor Especial (es) |")
    print("|       1     ", " |         R$ 6,00       ", "|       R$ 7,00     ", "|       R$ 8,00       |")
    print("|       2     ", " |         R$ 10,00      ", "|       R$ 12,00    ", "|       R$ 14,00      |")
    print("|       3     ", " |         R$ 14,00      ", "|       R$ 17,00    ", "|       R$ 20,00      |")
    print('-' * 85)


# Função que define os sabores disponíveis
def fun_sabor(sabor):
    global limpar_tela

    if sabor == 'tr':
        nome = 'TRADICIONAL'
        sabor_valido = True

    elif sabor == 'pr':
        nome = 'PREMIUM'
        sabor_valido = True

    elif sabor == 'es':
        nome = 'ESPECIAL'
        sabor_valido = True

    else:
        nome = ''
        sabor_valido = False
        limpar_tela = False
        print("\nSabor inválido! Tente novamente.")
        sleep(3)

    return sabor_valido, nome

# Função que define a quantidade disponível
def fun_quantidade(quantidade): 
    global limpar_tela

    if quantidade == '1' or quantidade == '2' or quantidade == '3':
        quantidade_valida = True

    else:
        quantidade_valida = False
        limpar_tela = False
        print("\nQuantidade inválida! Tente novamente.")
        sleep(3)

    return quantidade_valida

# Essa função retornará o preço de acordo com a quantidade e sabor selecionado. Além disso, ela também é responsável por enviar os preços à variável "preco_total"
def fun_preco(quantidade, sabor): 
    global preco_total

    if sabor == 'tr':
        if quantidade == '1':
            preco = 6.00
            preco_total += preco
        elif quantidade == '2':
            preco = 10.00
            preco_total += preco
        elif quantidade == '3':
            preco = 14.00
            preco_total += preco

    elif sabor == 'pr':
        if quantidade == '1':
            preco = 7.00
            preco_total += preco
        elif quantidade == '2':
            preco = 12.00
            preco_total += preco
        elif quantidade == '3':
            preco = 17.00
            preco_total += preco

    elif sabor == 'es':
        if quantidade == '1':
            preco = 8.00
            preco_total += preco
        elif quantidade == '2':
            preco = 14.00
            preco_total += preco
        elif quantidade == '3':
            preco = 20.00
            preco_total += preco

    return preco

# o preço de cada sorvete comprado será somado e armazenado nessa variável
preco_total = 0

# Limpar ou não a tela
limpar_tela = True

# Programa principal
while True:

    # Irá limpar a tela e exibir o cardápio somente se for a primeira vez executando o programa, ignorando o loop
    if limpar_tela == True:
        limpar()
        cardapio()

    sabor = input("\nEntre com o sabor desejado (tr|pr|es): ")

    sabor_valido, nome = fun_sabor(sabor)

    # Se o sabor inserido for válido
    if sabor_valido == True:

        quantidade = input("Entre com o número de bolas de sorvete desejado (1|2|3): ")
        quantidade_valida = fun_quantidade(quantidade)

        if quantidade_valida == True:
            preco = fun_preco(quantidade, sabor) # Recebe o preço da função "fun_preco" de acordo com o sabor e quantidade

            # Quando somente uma bola de sorvete for selecionada, a palavra "bola"
            if quantidade == '1':
                print("Você pediu 1 bola de sorvete no sabor {}: R$ {:.2f}".format(nome, preco))
                sleep(3)

            else:
                print("Você pediu {} bolas de sorvete no sabor {}: R$ {:.2f}".format(quantidade, nome, preco))
                sleep(3)

        else:
            continue
            
        continuar = input('\nDeseja mais algum sorvete (s|digite outra tecla)? R: ')

        # Caso o usuário deseje continua, o loop será reiniciado
        if continuar == 's':
            continue

        else:
            print('\nValor total a ser pago: R$ {:.2f}'.format(preco_total))
            sleep(3)
            break





