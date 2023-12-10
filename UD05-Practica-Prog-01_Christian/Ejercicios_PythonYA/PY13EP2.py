texto = input("Introduce una oración: ")

minusculas = texto.lower()

contadorvocales = 0

vocales = "aeiou"

for letra in minusculas:
    if letra in vocales:
        contadorvocales += 1

print("Cantidad de vocales en la oración: ", contadorvocales)
