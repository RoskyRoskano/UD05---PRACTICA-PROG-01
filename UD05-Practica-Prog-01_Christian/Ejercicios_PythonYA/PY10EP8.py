edadmanana = 0
edadtarde = 0
edadnoche = 0

print("Introduce las edades de los estudiantes del turno mañana:")
for i in range(5):
    edad = int(input("Estudiante : ", i+1))
    edadmanana += edad

print("Introduce las edades de los estudiantes del turno tarde:")
for i in range(6):
    edad = int(input("Estudiante: ", i+1))
    edadtarde += edad

print("Introduce las edades de los estudiantes del turno noche:")
for i in range(11):
    edad = int(input("Estudiante: ", i+1))
    edadnoche += edad

mediamanana = edadmanana / 5
mediatarde = edadtarde / 6
medianoche = edadnoche / 11

print("Media de edades del turno mañana:", mediamanana)
print("Media de edades del turno tarde:", mediatarde)
print("Media de edades del turno noche:", medianoche)

if mediamanana > mediatarde and mediamanana > medianoche:
    print("El turno mañana tiene la media de edades mayor.")
elif mediatarde > mediamanana and mediatarde > medianoche:
    print("El turno tarde tiene la media de edades mayor.")
else:
    print("El turno noche tiene la media de edades mayor.")
