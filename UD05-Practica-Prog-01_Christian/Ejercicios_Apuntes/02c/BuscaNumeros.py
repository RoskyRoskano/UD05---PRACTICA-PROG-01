numero = -1
lista = list()
while numero == -1:
    numusuario = int(input("Escribe un numero: "))
    if numusuario == 0:
        numero = 0
    else: 
        lista.append(numusuario)

numbuscar = int(input("Dime un numero y te dire en que posiciones esta: "))

posiciones = list()
for x in range(0,len(lista)):
    aux = lista.index(numbuscar, x)
    posiciones.append(aux)

conjunto = set(posiciones)
print("El numero ", numbuscar, " aparece ", conjunto)

