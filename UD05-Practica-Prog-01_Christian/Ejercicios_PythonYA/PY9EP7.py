pares = 0
impares = 0

n = int(input("Introduce una cantidad de numeros "))

i = 0

while i < n:
    numero = int(input("Ingrese el número: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    i += 1

print("Cantidad de números pares: ", pares)
print("Cantidad de números impares: ", impares)
