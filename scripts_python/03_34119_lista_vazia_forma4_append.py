# Criando lista vazia
numeros_sorteados = []

# Adicionando valores sequenciais em ordem crescente utilizando a iteração
for numeros in range(5):
    numeros_sorteados.append(numeros + 1) # o valor de numeros + 1 sempre será adicionado ao index numeros a cada iteração
    
print("A lista criada a partir do for é: ", numeros_sorteados)
print("Tamanho da lista é: ", len(numeros_sorteados))
