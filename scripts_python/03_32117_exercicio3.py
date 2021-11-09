email = input("Digite o endereço de e-mail:")

for caracter in email:
    if caracter != "@":
        ultimo = caracter
    else:
        break
print(ultimo)
