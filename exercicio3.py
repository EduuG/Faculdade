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

# Função para perguntar o peso do cachorro e valida-la
def cachorro_peso():
    global limpar_tela
    global valor_total

    peso = ''
    valor_base = 0
    valido = False # Caso essa varável continue falsa, ou seja, o usuário insira um valor inválido,
                   # o mesmo permanecerá preso no loop até que insira um valor válido.

    try:
        peso = int(input("\nEntre com o peso do cachorro: "))

        # O valor base do peso será somado à variável "valor_total"
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

# Função para perguntar o tamanho do peso do cachorro e valida-la.
def cachorro_pelo():
    global valor_total

    pelo = ''
    multi = 0
    valido = False

    try:
        pelo = input("\n- Entre com o pelo do cachorro -\nc - Pelo Curto\nm - Pelo Médio\nl - Pelo Longo\n\nR: ")

        # A variável global "valor_total" multiplicará ela mesmo pela variável "multi", na qual
        # armazena o fator da multiplicação com base no tamanho do pelo do cachorro.
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

# Função para perguntar se o usuário deseja serviços adicionais e valida-la.
def cachorro_extra():
    global valor_total
    global valor_adicionais
    global servicos # Chama a lista onde estão armazenados os serviços escolhidos, evitando que
                    # o usuário selecione o mesmo serviço mais de uma vez.

    valido = False
    extra = 0

    print("\n- Deseja adicionar mais algum serviço? -\n")
    print("1 - Corte de unhas - R$ 10,00")
    print("2 - Escovar dentes - R$ 12,00")
    print("3 - Limpeza de orelhas - R$ 15,00")
    print("0 - Não desejo mais nada")

    try:
        extra = int(input("\nR: "))

        if extra == 1:
            nome = "Cortes de unha"

            # Caso o serviço selecionado ainda não tiver sido escolhido, ou seja, não estiver na lista "servicos",
            # o serviço estará disponível para ser selecionado.
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

# Armazena o valor total, incluindo o preço base para o tamanho do cachorro,
# o fator de multiplicação para o tamanho do pelo e o serviço adicional.
valor_total = 0

# Armazena somente o preço dos serviços adicionais.
valor_adicionais = 0

# Lista que armazenará os serviços adicionais já selecionados, evitando que
# o usuário selecione-o mais de uma vez.
servicos = []

# Variável que decidirá se a tela deve ou não ser limpada.
limpar_tela = True

# Programa principal.
while True:
    if limpar_tela == True:
        limpar()
        print("--- Bem-vindo ao petshop do Eduardo Guimarães dos Santos ---")
    
    peso, valor_base, valido = cachorro_peso()

    # Caso o peso do cachorro seja válido, prosseguirá para próxima etapa.
    if valido == True:
        while True:
            pelo, multi, valido = cachorro_pelo()    

            # Caso o pelo do cachorro seja válido, prosseguirá para próxima etapa.
            if valido == True:
                while True:
                    extra, valido = cachorro_extra()

                    # Caso o serviço adicional seja válido, irá perguntar se deseja adicionar mais algum.
                    if valido == True:

                        # Caso o usuário não deseje mais nada, o total a pagar e o calculo da conta serão exibidos.
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
