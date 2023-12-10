fichero=open("datos.txt","r")
linea=fichero.readline()
while linea!='':
    print(linea, end='')
    linea=fichero.readline()
fichero.close()