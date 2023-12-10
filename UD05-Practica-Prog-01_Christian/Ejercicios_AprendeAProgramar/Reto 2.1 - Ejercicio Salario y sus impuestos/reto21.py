horastrabajadas = float(input("Ingrese el número de horas trabajadas: "))
preciohora = float(input("Ingrese el precio por hora: "))

impuestos25 = 0.25
impuestos254 = 0.45

if horastrabajadas <= 35:
    salariobruto = horastrabajadas * preciohora
else:
    horas_normales = 35
    horas_extra = horastrabajadas - horas_normales
    salariobruto = (horas_normales * preciohora) + (horas_extra * 1.5 * preciohora)

impuestos = 0
if salariobruto > 500:
    impuestos += min(400, salariobruto - 500) * impuestos25
if salariobruto > 900:
    impuestos += max(0, salariobruto - 900) * impuestos254

salario_neto = salariobruto - impuestos

print("El salario neto semanal es: euros", salario_neto, "euros")
