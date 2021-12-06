my_list = [17, 13, 11, 15, 1, 9, 7, 15, 13]
nova_lista = []

for i in my_list:
    if i not in nova_lista:
        nova_lista.append(i)

print(nova_lista)