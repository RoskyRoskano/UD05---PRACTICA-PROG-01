lista = [[100, 7, 85, 8], [4, 8, 56, 25], [67, 89, 23, 1], [78, 56]]

print("Lista original:")
for fila in lista:
    print(fila)

for i in range(len(lista[0])):
    if lista[0][i] > 50:
        lista[0][i] = 0

print("Lista después de fijar a cero elementos mayores a 50 del primer elemento:")
for fila in lista:
    print(fila)
