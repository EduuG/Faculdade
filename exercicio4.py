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
def realce(nome): 
    print("{}{}{}".format('+', '-' * (len(nome) + 2), '+'))
    print("{}{}{}".format('| ', nome, ' |'))
    print("{}{}{}".format('+', '-' * (len(nome) + 2), '+'))

limpar_tela = True

while True:
    if limpar_tela == True:
        limpar()
        realce("Bem-vindo ao controle de Colaboradores do Eduardo Guimarães dos Santos")