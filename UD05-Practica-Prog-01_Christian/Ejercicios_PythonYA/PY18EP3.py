lista = list()

for i in range(5):
    numero = int(input("Introduce un número: "))
    lista.append(numero)

lista.sort()
print("Lista ordenada de menor a mayor:", lista)

lista.sort(reverse=True)
print("Lista ordenada de mayor a menor:", lista)
