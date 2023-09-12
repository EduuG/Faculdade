palavras = ('sonic', 'eduardo', 'mario', 'andressa', 'linux',
            'python', 'backend', 'michael', 'beatles', 'madrugada')

vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    print("\n{} = ".format(palavra), end=' ')
    for vogal in vogais:
        if vogal in palavra:
            print("{}".format(vogal), end=' ')
print()
