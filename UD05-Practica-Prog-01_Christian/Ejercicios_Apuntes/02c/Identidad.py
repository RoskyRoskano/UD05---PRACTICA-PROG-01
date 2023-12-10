tamaño = int(input("Dime un tamaño para la tabla: "))
lista = []

for i in range(tamaño):
    lista.append([])
    for j in range(tamaño):
        numero = input("Dame un numero: ")
        lista[i] += numero

correcto = 0
for i in range(tamaño):
    for j in range(tamaño):
        if(i == j):
            if "1" in lista[i][j]:
                correcto += 1

if(correcto == tamaño):
    print("Es una matriz identidad")
else:
    print("No es una matriz identidad")


