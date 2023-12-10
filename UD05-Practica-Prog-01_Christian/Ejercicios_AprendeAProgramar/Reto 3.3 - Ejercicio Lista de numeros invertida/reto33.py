cantnumeros = input("Introduce un numero: ")

numeros = cantnumeros.split(" ")

numeros = list(map(int, numeros))

resultado = ' '.join(map(str, reversed(numeros)))
print(resultado)
