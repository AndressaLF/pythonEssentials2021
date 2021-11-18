# Criando lista vazia
numeros_sorteados = []

# Adicionando valores sequenciais em uma ordem decrescentes a partir da iteração
for numeros in range(5):
    numeros_sorteados.insert(0, numeros + 1) # o novo valor sempre será o valor do indice + 1. Este valor será adicionado ao indice zero a cada nova itercação. Dessa forma o primeiro valor (1) estará posicionado no último indice.
print("A lista criada a partir do for é: ", numeros_sorteados)
print("Tamanho da lista é: ", len(numeros_sorteados))
