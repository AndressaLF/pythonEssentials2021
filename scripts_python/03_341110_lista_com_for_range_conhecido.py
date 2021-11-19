# criação da lista e da variável que armazenará o valor da soma
minha_lista = [3,7,8,2,9]
soma_total = 0

# O for começará em 0 e irá até o tamanho total da lista = 5.
for i in range(5):
    soma_total += minha_lista[i] # a cada iteração o valor de soma_total será adicionado ao valor armazenado na posição da iterção, em minha_lista[i].
    
print("A soma total dos elementos da lista", minha_lista, "é = ", soma_total)
