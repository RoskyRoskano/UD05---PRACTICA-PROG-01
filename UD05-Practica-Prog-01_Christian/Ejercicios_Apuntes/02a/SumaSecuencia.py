numeros = input("Dame numeros separdos por espacios:")
lista = list()

lista = numeros.split(" ")
suma = 0

for i in range(len(lista)):
    suma += int(lista[i])

print("El resultado es:",suma)