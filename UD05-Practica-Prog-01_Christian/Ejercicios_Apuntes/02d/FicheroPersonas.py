lectura = open("personas.txt", "r", encoding="utf-8")

lineas = lectura.readlines()

lista = list()

for linea in lineas:
    lista.append(linea.split(";"))

edadmayor = ["", 0]


for i in range(len(lista)):
    if(int(lista[i][1])>int(edadmayor[1])):
        edadmayor = [lista[i][0],lista[i][1]]
    
print("El mas mayor es:", edadmayor[0], "y su edad es: ", edadmayor[1])
edadmenor = ["", edadmayor[1]]

for i in range(len(lista)):
    if(int(lista[i][1])<int(edadmenor[1])):
        edadmenor = [lista[i][0],lista[i][1]]

print("Y el mas pequeño es:", edadmenor[0], "y su edad es: ", edadmenor[1])
