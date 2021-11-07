numero = int(input("Digite um número:"))
passos = 0

if numero > 0:
    while numero != 1:
        passos += 1
        if numero % 2 == 0:
            numero = int(numero/2)
            print(numero)
        else:
            numero = ((3 * numero)+1)
            print(numero)
    print("A quantidade de passos:", passos)
