print("Rellena tu direccion postal:")
calle = input("Nombre de calle: ")
puerta = int(input("Numero de puerta: "))
piso = int(input("Numero de piso: "))

direccion = (calle, puerta, piso)

print("Nombre de calle:", direccion[0])
print("Numero de puerta:", direccion[1])
print("Numero de piso:", direccion[2])