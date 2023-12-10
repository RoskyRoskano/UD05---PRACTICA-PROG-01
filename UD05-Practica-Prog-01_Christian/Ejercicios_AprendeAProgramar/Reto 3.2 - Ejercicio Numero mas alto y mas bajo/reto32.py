cantnumeros = int(input("Introduce un numero"))

maximo = float('-inf')
minimo = float('inf')

for i in range(cantnumeros):
    numero = int(input())
    maximo = max(maximo, numero)
    minimo = min(minimo, numero)

print("Numero mas mayor: ",maximo," Numero mas bajo: ", minimo)
