nombres = input("Escribe 3 nombres: ")

nombresseparados = nombres.split(",")

lista = list()

for nombres in nombresseparados:
    lista.append(nombres)

lista.reverse()

print(lista)