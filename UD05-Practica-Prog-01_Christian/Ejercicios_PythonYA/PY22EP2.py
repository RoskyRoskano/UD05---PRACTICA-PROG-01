lista = list()
for i in range(5):
    numero = int(input(f"Ingrese el entero {i + 1}: "))
    lista.append(numero)

nuevalista = list()
for elemento in lista:
    if elemento < 10:
        nuevalista.append(elemento)

print("Lista original:", lista)
print("Nueva lista sin elementos mayores o iguales a 10:", nuevalista)
