nombres = list()

for i in range(5):
    nombre = input("Introduce el nombre de una persona: ")
    nombres.append(nombre)

nombremenor = min(nombres)

print("El nombre menor en orden alfabético es:", nombremenor)
