usuarios = {}

for i in range(4): 
    print("Usuario", i+1)
    dni = input("DNI: ")
    calle = input("Nombre de calle: ")
    puerta = int(input("Numero de puerta: "))
    piso = int(input("Numero de piso: "))
    usuarios[dni] = (dni, calle, puerta, piso)

usuariobuscar = input("Que usuario quieres consultar: ")

if usuariobuscar in usuarios:
    print("DNI: ",usuarios[usuariobuscar][0])
    print("Calle: ",usuarios[usuariobuscar][1])
    print("Puerta: ",usuarios[usuariobuscar][2])
    print("Piso: ",usuarios[usuariobuscar][3])
else:
    print("El DNI no se encuentra almacenado")


