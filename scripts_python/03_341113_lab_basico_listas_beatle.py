# step 1
beatles = []
print("Step 1:", beatles)

# step 2
for i in range(3):
    integrante = input("Digite o nome do integrante da banda beatles: ")
    beatles.append(integrante)
print("Step 2:", beatles)

# step 3
for i in range(2):
    integrante = input("Digite o nome do integrante da banda beatles: ")
    beatles.append(integrante)
print("Step 3:", beatles)

# step 4
del beatles[3:5]
print("Step 4:", beatles)

# step 5
integrante = "Ringo Starr"
beatles.insert(0, integrante)
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
