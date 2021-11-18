# Criando lista vazia
numeros_sorteados = []

# Adicionando valores na lista utilizando o input a partir de cada iteração
for numeros in range(5):
    novo_numero = int(input("Digite um novo número para a lista: "))
    numeros_sorteados.insert(numeros, novo_numero)

print("A lista criada a partir do for é: ", numeros_sorteados)
print("Tamanho da lista é: ", len(numeros_sorteados))
