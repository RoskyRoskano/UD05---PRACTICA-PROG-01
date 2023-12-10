
sueldo = float(input("Introduce el sueldo del operario: "))
antiguedad = int(input("Ingrese los años de antigüedad del operario: "))

if sueldo < 500:
    if antiguedad >= 10:
        sueldopagar = sueldo * 1.20
        print("El nuevo sueldo con aumento del 20% es:", sueldopagar)
    else:
        sueldopagar = sueldo * 1.05
        print("El nuevo sueldo con aumento del 5% es:", sueldopagar)
else:

    print("El sueldo sin cambios es:", sueldo)