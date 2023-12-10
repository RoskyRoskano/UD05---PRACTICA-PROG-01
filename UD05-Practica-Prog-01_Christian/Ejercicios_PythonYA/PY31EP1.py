def carga_datos():
    listaenteros=list()
    for i in range(5):
        entero=int(input("Introduce un entero : "))
        listaenteros.append(entero)
    return listaenteros
def mayor_menor(listaenteros):
    mayor=listaenteros[0]
    menor=listaenteros[0]
    for i in range(1,len(listaenteros)):
        if listaenteros[i]> mayor:
            mayor=listaenteros[i]
        else:
            if listaenteros[i]<menor:
                menor=listaenteros[i]
    return (mayor,menor)

datos=carga_datos()
tuplaMaymen=mayor_menor(datos)

print(tuplaMaymen)
may,men=tuplaMaymen
print("El entero MAYOR es : ",may)
print("El entero menor es : ",men)
