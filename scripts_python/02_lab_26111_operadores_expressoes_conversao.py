horas = 60 * int(input("Digite as horas do inicio do evento:")) # armazena as horas convertidas em minutos
minutos = int(input("Digite os minutos de inicio do evento:"))
duracao = int(input("Digite o valor, em minutos, da duração do evento:"))

resto = str(int((horas + minutos + duracao)%60)) # armazena apenas o resto da divisão por 60
tempo_final = str(((horas + minutos + duracao) // 60)%24) #armazena o resto da divisão de todos os minutos por 24h
print()
print("O evento terminará às " + tempo_final + ":" +resto+ ".")
