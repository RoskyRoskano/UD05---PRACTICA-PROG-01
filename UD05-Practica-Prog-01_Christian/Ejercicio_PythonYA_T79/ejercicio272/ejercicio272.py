fichero=open("datos.txt","a")
fichero.write("nueva línea 1\n")
fichero.write("nueva línea 2\n")
fichero.close()
fichero=open("datos.txt","r")
contenido=fichero.read()
print(contenido)
fichero.close()