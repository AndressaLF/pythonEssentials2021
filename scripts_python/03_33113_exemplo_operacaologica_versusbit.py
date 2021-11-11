i = 15  # inteiro armazendo em 32bits. Bitwise: 00000000000000000000000000001111
j = 22  # inteiro armazendo em 32bits. Bitwise: 00000000000000000000000000010110


# Conjunção lógica
log = i and j   
print("O resultado da operação and lógica é: log = ", log)


# Conjunção bitwise
bit = i & j
print("O resultado da operação and bitwise é: bit = ", bit)

# Operador lógico de negação
lognet = not i
print("O resultado da operação da negação lógica: lognet = ", lognet)

# Operador bitwise de negação
bitneg = ~i
print("O resultado da operação da negação bitwise: bitneg = ", bitneg)
