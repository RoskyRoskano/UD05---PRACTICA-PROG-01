fichero=open("datos.txt","r")
for linea in fichero:
    print(linea, end='')
fichero.close()