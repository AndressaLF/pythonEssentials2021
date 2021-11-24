
hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
new_number = int(input("Digite um novo valor para substitur o terceiro número: "))

# to replace the middle number with an integer number entered by the user.
hat_list[2] = new_number

# Step 2: write a line of code that removes the last element from the list.
del hat_list[4]

# Step 3: write a line of code that prints the length of the existing list.
print("O tamanho total da lista é:", len(hat_list))

print(hat_list)
