string = input("Digite uma string:")
nstring = ""

for digito in string:
    if digito == "0":
        digito = "x"
        nstring += digito
        continue
    else:
        nstring += digito
        
print(nstring)
