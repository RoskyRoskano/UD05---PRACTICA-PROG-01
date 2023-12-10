fichero=open("datos.txt","r")
lineas=fichero.readlines()
print('El archivo tiene', len(lineas), 'líneas')
print('El contenido del archivo')
for linea in lineas:
    print(linea, end='')
fichero.close()