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

def cachorro_peso():
    global limpar_tela
    global valor_total

    peso = ''
    valor_base = 0
    valido = False

    try:
        peso = int(input("\nEntre com o peso do cachorro: "))

        if peso < 3:
            valor_base = 40
            valor_total =+ valor_base
            valido = True
        elif peso >= 3 and peso < 10:
            valor_base = 50
            valor_total =+ valor_base
            valido = True
        elif peso >= 10 and peso < 30:
            valor_base = 60
            valor_total =+ valor_base
            valido = True
        elif peso >= 30 and peso < 50:
            valor_base = 70
            valor_total =+ valor_base
            valido = True
        else:
            valido = False
            print("\nNão aceitamos cachorros tão grandes.")
            limpar_tela = False
            sleep(3)
    except ValueError:
        valido = False
        print("\nValor inválido! Por favor, tente novamente.")
        limpar_tela = False
        sleep(3)

    return peso, valor_base, valido

def cachorro_pelo():
    global valor_total

    pelo = ''
    multi = 0
    valido = False

    try:
        pelo = input("\n- Entre com o pelo do cachorro -\nc - Pelo Curto\nm - Pelo Médio\nl - Pelo Longo\n\nR: ")

        if pelo == 'c':
            multi = 1
            valido = True
        elif pelo == 'm':
            multi = 1.5
            valor_total *= multi
            valido = True
        elif pelo == 'l':
            multi = 2
            valor_total *= multi
            valido = True
        else:
            valido = False
            print("\nTamanho de pelo inválido! Tente novamente.")
            sleep(3)

    except ValueError:
        valido = False
        print("\nValor inválido! Por favor, tente novamente.")
        sleep(3)

    return pelo, multi, valido

def cachorro_extra():
    global valor_total
    global valor_adicionais
    global servicos

    valido = False

    print("\n- Deseja adicionar mais algum serviço? -\n")
    print("1 - Corte de unhas - R$ 10,00")
    print("2 - Escovar dentes - R$ 12,00")
    print("3 - Limpeza de orelhas - R$ 15,00")
    print("0 - Não desejo mais nada")

    try:
        extra = int(input("\nR: "))

        if extra == 1:
            nome = "Cortes de unha"

            if nome not in servicos:
                servicos.append(nome)
                valor_total += 10
                valor_adicionais += 10
                valido = True
            else:
                valido = False
                print("\nEste serviço já foi selecionado!")
                sleep(3)

        elif extra == 2:
            nome = "Escovar dentes"

            if nome not in servicos:
                servicos.append(nome)
                valor_total += 12
                valor_adicionais += 12
                valido = True
            else:
                valido = False
                print("\nEste serviço já foi selecionado!")
                sleep(3)

        elif extra == 3:
            nome = "Limpeza de orelhas"

            if nome not in servicos:
                servicos.append(nome)
                valor_total += 15
                valor_adicionais += 15
                valido = True
            else:
                valido = False
                print("\nEste serviço já foi selecionado!")
                sleep(3)

        elif extra == 0:
            valor_total += 0
            valido = True
        else:
            valido = False
            print("\nValor inválido! Por favor, tente novamente.")
            sleep(3)
    
    except ValueError:
        valido = False
        print("\nValor inválido! Por favor, tente novamente.")
        sleep(3)

    return extra, valido

valor_total = 0
valor_adicionais = 0
servicos = []
limpar_tela = True

while True:
    if limpar_tela == True:
        limpar()
        print("--- Bem-vindo ao petshop do Eduardo Guimarães dos Santos ---")
    
    peso, valor_base, valido = cachorro_peso()

    if valido == True:
        while True:
            pelo, multi, valido = cachorro_pelo()    

            if valido == True:
                while True:
                    extra, valido = cachorro_extra()

                    if valido == True:
                        if extra == 0:
                            print("\nTotal a pagar(R$): {:.2f} (peso: {} * pelo: {} + adicional(is): {})".format(valor_total, valor_base, multi, valor_adicionais))
                            break
                    else:
                        continue
            else:
                continue

            break

    else:
        continue

    break
