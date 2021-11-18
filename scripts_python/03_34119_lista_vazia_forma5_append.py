# Criando lista vazia
numeros_sorteados = []

# Adicionando valores sequenciais em ordem decrescente utilizando a iteração
for numeros in range(4, -1, -1): # 4 = valor de inicio     -1 = valor final    -1 = valor do passo
    numeros_sorteados.append(numeros + 1) # o valor de numeros + 1 sempre será adicionado ao index de numeros - 1 a cada iteração.
    
print("A lista criada a partir do for é: ", numeros_sorteados)
print("Tamanho da lista é: ", len(numeros_sorteados))
