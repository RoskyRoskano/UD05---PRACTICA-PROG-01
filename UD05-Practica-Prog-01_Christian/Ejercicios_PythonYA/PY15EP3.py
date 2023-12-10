sueldosmanana = list()
sueldostarde = list()

print("Introduce los sueldos de los empleados del turno de mañana:")
for i in range(4):
    sueldo = float(input("Sueldo del empleado: "))
    sueldosmanana.append(sueldo)

print("Introduce los sueldos de los empleados del turno de tarde:")
for i in range(4):
    sueldo = float(input("Sueldo del empleado: "))
    sueldostarde.append(sueldo)

print("Lista de sueldos del turno de mañana:", sueldosmanana)
print("Lista de sueldos del turno de tarde:", sueldostarde)
