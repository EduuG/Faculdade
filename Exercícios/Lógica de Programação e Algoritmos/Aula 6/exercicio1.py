palavras = ('sonic', 'eduardo', 'mario', 'andressa', 'linux',
            'python', 'backend', 'michael', 'beatles', 'madrugada')

# Minha forma
vogais = ('a', 'e', 'i', 'o', 'u')
for palavra in palavras:
    print("\n{} = ".format(palavra), end=' ')
    for vogal in vogais:
        if vogal in palavra:
            print("{}".format(vogal.upper()), end=' ')
print()

# Forma do professor
for palavra in palavras:
    print("\n{} =".format(palavra), end=' ')
    for letra in palavra:
        if letra in "aeiou":
            print(letra.upper(), end=' ')
print()
