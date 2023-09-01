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

# Função para realçar a apresentação do programa
def realce(titulo): 
    print("{}{}{}".format('+', '-' * (len(titulo) + 2), '+'))
    print("{}{}{}".format('| ', titulo, ' |'))
    print("{}{}{}".format('+', '-' * (len(titulo) + 2), '+'))

# Função que permite criar separadores de maneira dinâmica, alterando seu tamanho,
# se deve conter um título ou não, e também sua aparência (se usará "-" ou "+").
def separador(titulo = '', limite = 0, tipo = 0):
    if titulo:
        titulo = ("{}{}{}".format(' ', titulo, ' '))
        titulo_original = titulo

        # Se o parâmetro "limite" não for informado, ele usará o tamanho padrão armazenado
        # na variável "separador_tamanho".
        if not limite: 
            i = 0      
            while len(titulo) < separador_tamanho:
                titulo = ("{}{}{}".format('-' * i, titulo_original, '-' * i))
                i += 1

            if len(titulo) == (separador_tamanho + 1):
                titulo = titulo[:-1]

        # Se não, usará o tamanho informado no parâmetro.
        else:
            i = 0
            while len(titulo) < limite:
                titulo = ("{}{}{}".format('-' * i, titulo, '-' * i))
                i += 1

            if len(titulo) == (limite + 1):
                titulo = titulo[:-1]

        print_delay(titulo)
    else:
        # Se o tipo não for informado, ele usará a aparência padrão de "-".
        if not tipo:
            if not limite:
                print_delay('-' * separador_tamanho)
            else:
                print_delay('-' * limite)
        elif tipo == 1:
            if not limite:
                print_delay('+' * separador_tamanho)
            else:
                print_delay('+' * limite)


# Função para tornar a exibição do programa menos abrupta. Ele utiliza da variável
# "tempo_delay" para determinar a velocidade em que os textos serão exibidos.
def print_delay(exibir, tempo = 0):
    if tempo:
       print(exibir) 
       sleep(tempo)
    else:
        print(exibir)
        sleep(tempo_delay)

# Função para cadastrar o colaborador. Como parâmetro, ele recebe a id do colaborador,
# que é definida de maneira automática pela variável "id_global".
def cadastrar_colaborador(id):
    global limpar_tela

    limpar_tela = False

    print_delay("")
    separador("MENU CADASTRAR COLABORADOR")
    nome = input("Por favor, entre com o nome: ").title()
    setor = input("Por favor, entre com o setor: ")
    salario = float(input("Por favor, entre com o pagamento (R$): "))

    dicionario = {"id": id, "nome": nome, "setor": setor, "salario": salario}

    lista_colaboradores.append(dicionario) # Envia o dicionário para a lista.

    print_delay("\n- Colaborador cadastrado com sucesso! -")
    sleep(3)

# Função para consultar colaborador(es), seja de todos eles, através de um ID específico
# ou de um setor inteiro.
def consultar_colaborador():
    global limpar_tela

    limpar_tela = False

    while True:
        print_delay("")
        separador("MENU CONSULTAR COLABORADOR")
        print_delay("1 - Consultar Todos")
        print_delay("2 - Consultar por Id")
        print_delay("3 - Consultar por Setor")
        print_delay("4 - Retornar ao menu")

        resposta = int(input("\nR: "))
        
        if resposta == 1: # consultar todos
            print_delay("")
            separador(limite = 25, tipo = 1)

            # Se houver colaboradores registrados:
            if lista_colaboradores:
                for colaborador in lista_colaboradores:
                    for key, value in colaborador.items():
                        print_delay("{}: {}".format(key.title(), value))

                    # Não pulará uma linha caso seja o último colaborador exibido, apenas para fins de estética.
                    if colaborador != lista_colaboradores[-1]: 
                        print_delay("")

            # Se não houver colaboradores registrados:
            else:
                print_delay("Nenhum colaborador cadastrado!")

            separador(limite = 25, tipo = 1)
            continue
        
        elif resposta == 2: # consultar por id
            print_delay("")
            separador()

            # Variável para definir se o ID informado foi validado ou não.
            id_valido = False

            consultar_id = int(input("Digite o ID do colaborador: "))
            print_delay("")

            separador(limite = 25, tipo = 1)
            for colaborador in lista_colaboradores:
                if consultar_id == colaborador["id"]:
                    for key, value in colaborador.items():
                        print_delay("{}: {}".format(key.title(), value))
                        id_valido = True

            # Se o ID não for validado, uma mensagem será exibida.
            if id_valido == False:
                print_delay("- ID inexistente! -")

            separador(limite = 25, tipo = 1)

        elif resposta == 3: # consultar por setor
            print_delay("")
            separador()

            # Variável para definir se o setor informado foi validado ou não.
            setor_valido = False

            setor = input("Informe o setor: ")
            print_delay("")

            separador(limite = 25, tipo = 1)
            for colaborador in lista_colaboradores:
                if setor == colaborador["setor"]:
                    for key, value in colaborador.items():
                        print_delay("{}: {}".format(key.title(), value))
                        setor_valido = True

                    if colaborador != lista_colaboradores[-1]:
                        print_delay("")

            # Se o setor não for validado, uma mensagem será exibida.
            if setor_valido == False:
                print_delay("- Setor inexistente! -")

            separador(limite = 25, tipo = 1)
                    
        elif resposta == 4: # retornar ao menu
            return 0

        else:
            print_delay("\nOpção inválida! Tente novamente.")
            sleep(3)

# Função para remover colaborador informando sua ID.
def remover_colaborador():
    while True:
        print_delay("")
        separador("MENU REMOVER COLABORADOR")
        remover = int(input("Digite o ID do colaborador a ser removido: "))

        id_valido = False

        for colaborador in lista_colaboradores:
            if remover == colaborador["id"]:
                print_delay("\n- Colaborador {} removido com sucesso -".format(colaborador["nome"]))
                sleep(3)
                lista_colaboradores.remove(colaborador)
                id_valido = True
        if id_valido == False:
            print("\n- ID inexistente! -")
            sleep(3)
        break
            

# Variável para definir se a tela será limpada ou não. Está só será verdadeira
# na primeira execução do programa.
limpar_tela = True

# Essa variável será incrementada em 1 sempre que um novo colaborador for cadastrado.
id_global = 0

# Lista dos colaboradores, contendo dicionários que armazenam os dados de cada um deles (id, nome, setor, salário).
lista_colaboradores = []

# Variável para definir o tamanho dos separadores.
separador_tamanho = 74

# Variável para definir o delay da exibição.
tempo_delay = 0.1

# Programa principal.
while True:
    if limpar_tela == True:
        limpar()
        sleep(tempo_delay)
        realce("Bem-vindo ao controle de Colaboradores do Eduardo Guimarães dos Santos")
    else:
        print_delay("")
    sleep(tempo_delay)
    separador("MENU PRINCIPAL")
    print_delay("Escolha a opção desejada:\n")
    print_delay("1 - Cadastrar Colaborador")
    print_delay("2 - Consultar Colaborador(res)")
    print_delay("3 - Remover Colaborador")
    print_delay("4 - Encerrar programa")

    try:
        option = int(input("\nR: "))

        if option == 1:
            id_global += 1 # Incrementa em um, como dito anteriormente.
            cadastrar_colaborador(id_global)

        elif option == 2:
            consultar_colaborador()

        elif option == 3:
            remover_colaborador()

        elif option == 4:
            print("\n- Até mais! -")
            sleep(3)
            break

        else:
            print("\n- Opção inválida! Por favor, tente novamente. -")
            sleep(3)
            continue
    
    except ValueError:
        print("\n- Opção inválida! Por favor, tente novamente. -")
        sleep(3)
