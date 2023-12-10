nombres = list()
notas = list()

for i in range(4):
    nombre = input("Introduce el nombre del alumno: ")
    nota = float(input("Introduce la nota del alumno: "))

    nombres.append(nombre)
    notas.append(nota)

print("Listado de alumnos:")
for i in range(4):
    nombre = nombres[i]
    nota = notas[i]

    if nota >= 8:
        condicion = "Muy Bueno"
    elif 4 <= nota <= 7:
        condicion = "Bueno"
    else:
        condicion = "Insuficiente"

    print("Nombre: ",nombre," , Nota:", nota, " Condición: ",condicion)

alumnosmuybueno = 0
for nota in notas:
    if nota >= 8:
        alumnosmuybueno += 1

print("Cantidad de alumnos con Muy Bueno: ", alumnosmuybueno)
