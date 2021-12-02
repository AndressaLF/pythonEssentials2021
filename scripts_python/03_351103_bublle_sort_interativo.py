minha_lista = []
troca = True
numero = int(input("Quantos elementos haverá em sua lista? "))

for i in range(numero):
    novo_valor = int(input(f'Digite o elemento {i}: '))
    minha_lista.append(novo_valor) #adicionando o valor digitado na última posição da lista

while troca:
    troca = False
    for i in range(len(minha_lista)-1):
        if minha_lista[i] > minha_lista[i+1]:
            troca = True
            minha_lista[i], minha_lista[i+1] = minha_lista[i+1], minha_lista[i]


print("\nOrdenados:")
print(minha_lista)