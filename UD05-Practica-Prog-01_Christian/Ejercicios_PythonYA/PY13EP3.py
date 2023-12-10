clave = input("Introduce una clave: ")

longitud = len(clave)

if 10 <= longitud <= 20:
    print("La clave ingresada es válida.")
else:
    print("Error: La clave debe tener entre 10 y 20 caracteres.")
