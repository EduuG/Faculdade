# Jokenpô by Eduardo

from random import randint
from time import sleep
from os import system

win = 5
vencedores = []
ganhou = False
empatou = False

while win != -1:
    system("clear")

    print("Rodadas restante: {}".format(win))
    print("\n1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura\n")

    jogada_player = input("R: ")

    try:
        jogada_player = int(jogada_player)
        if jogada_player < 0 or jogada_player > 3:
            print("\n- Valor inválido! -\n")
            continue

        elif jogada_player == 1:
            jogada_player = "pedra"

        elif jogada_player == 2:
            jogada_player = "papel"

        elif jogada_player == 3:
            jogada_player = "tesoura"

        elif jogada_player == 0:
            print("\n- Até mais! -\n")
            sleep(3)
            break

    except ValueError:
        print("\n- Valor inválido! -\n")

    jogada_pc = randint(1, 3)

    # Computador joga PEDRA
    if jogada_pc == 1:
        jogada_pc = "pedra"

        if jogada_player == "pedra":
            vencedores.append("player")
            vencedores.append("computador")
            ganhou = True
            empatou = True

        elif jogada_player == "papel":
            vencedores.append("player")
            ganhou = True
            empatou = False

        elif jogada_player == "tesoura":
            vencedores.append("computador")
            ganhou = False
            empatou = False

    # Computador joga PAPEL
    elif jogada_pc == 2:
        jogada_pc = "papel"

        if jogada_player == "pedra":
            vencedores.append("computador")
            ganhou = False
            empatou = False

        elif jogada_player == "papel":
            vencedores.append("player")
            vencedores.append("computador")
            ganhou = True
            empatou = True

        elif jogada_player == "tesoura":
            vencedores.append("player")
            ganhou = True
            empatou = False

    # Computador joga TESOURA
    elif jogada_pc == 3:
        jogada_pc = "tesoura"

        if jogada_player == "pedra":
            vencedores.append("player")
            ganhou = True
            empatou = False

        elif jogada_player == "papel":
            vencedores.append("computador")
            ganhou = False
            empatou = False

        elif jogada_player == "tesoura":
            vencedores.append("player")
            vencedores.append("computador")
            ganhou = True
            empatou = True

    print("\nJokenpô...")
    sleep(2)

    print("\nVocê: {}".format(jogada_player))
    print("Computador: {}".format(jogada_pc))

    if ganhou and empatou is False:
        print("\n- Você ganhou! -\n")

    elif ganhou is False and empatou is False:
        print("\n- Você perdeu! -\n")

    elif ganhou and empatou:
        print("\n- Vocês empataram! -\n")

    continuar = input("Aperte qualquer tecla para continuar")

    win -= 1

    if win == 0:
        player_pontos = vencedores.count("player")
        pc_pontos = vencedores.count("player")
        print("\n- FIM DE JOGO! -\n")
        print("Resultado:")
        print("\nVocê: {} pontos".format(player_pontos))
        print("Computador: {} pontos".format(pc_pontos))

        if player_pontos == pc_pontos:
            print("\n- Vocês empataram! -\n")

        elif player_pontos > pc_pontos:
            print("\n- Você ganhou! -\n")

        elif player_pontos < pc_pontos:
            print("\n- Você perdeu! -\n")

        break
