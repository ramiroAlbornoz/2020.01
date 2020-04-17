frase=input("introduzca una frase: ")
letra=input("introduzca una letra: ")
veces=0
for i in frase:
    if i==letra:
        veces+=1
print("la letra esta ",veces," veces")
