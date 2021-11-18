# Criando lista vazia
numeros_sorteados = []

# Adicionando valores sequencias em ordem crescentes a partir da iteração
for numeros in range(5):
    numeros_sorteados.insert(numeros, numeros + 1) # a cada index, começando do zero, será adicionado o valor do indice + 1. No final o valor 1 estará na primeira posição e o 5 na última.
print("A lista criada a partir do for é: ", numeros_sorteados)
print("Tamanho da lista é: ", len(numeros_sorteados))
