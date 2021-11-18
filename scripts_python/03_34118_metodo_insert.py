numeros_sorteados = [92, 2, 8, 55, 15, 32, 41, 17, 25]
print("Lista original: ", numeros_sorteados)
print("Tamanho da lista original: ", len(numeros_sorteados))  # imprimi na tela o comprimento total da lista

# Usando o método insert(arg1, arg2)
numeros_sorteados.insert(3, -2) # será adicionado o valor -2 na posição 3, ou seja, no local do 55.
print("Lista após usar o método insert(3, -2):", numeros_sorteados)
print("Tamanho da lista original: ", len(numeros_sorteados))
