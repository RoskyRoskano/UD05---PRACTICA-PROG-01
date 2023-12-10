negativos = 0
positivos = 0
multiplos = 0
acumulados = 0


for i in range(10):
    valor = int(input("Introduce un numero: "))
    
    if valor < 0:
        negativos += 1
    elif valor > 0:
        positivos += 1
    
    if valor % 15 == 0:
        multiplos += 1
    
    # Acumular el valor si es par
    if valor % 2 == 0:
        acumulados += valor

print("Cantidad de valores ingresados negativos: ",negativos)
print("Cantidad de valores ingresados positivos: ",positivos)
print("Cantidad de múltiplos de 15: ", multiplos)
print("Valor acumulado de los números ingresados que son pares: ", acumulados)
