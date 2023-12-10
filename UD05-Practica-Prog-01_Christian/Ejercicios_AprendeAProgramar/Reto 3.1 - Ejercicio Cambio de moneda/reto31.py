cantdinero = int(input("ntroduce una cantidad de dinero que debe ser múltiplo de 5: "))

if cantdinero % 5 != 0:
    print("La cantidad ingresada no es un múltiplo de 5")
else:
    bill500 = 0
    bill200 = 0
    bill100 = 0
    bill50 = 0
    bill20 = 0
    bill10 = 0
    bill5 = 0

    while cantdinero > 0:
        if cantdinero >= 500:
            bill500 += 1
            cantdinero -= 500
        elif cantdinero >= 200:
            bill200 += 1
            cantdinero -= 200
        elif cantdinero >= 100:
            bill100 += 1
            cantdinero -= 100
        elif cantdinero >= 50:
            bill50 += 1
            cantdinero -= 50
        elif cantdinero >= 20:
            bill20 += 1
            cantdinero -= 20
        elif cantdinero >= 10:
            bill10 += 1
            cantdinero -= 10
        elif cantdinero >= 5:
            bill5 += 1
            cantdinero -= 5

    print("Desglose: ")
    print("Billetes de 500: ", bill500)
    print("Billetes de 200: ",bill200)
    print("Billetes de 100: ", bill100)
    print("Billetes de 50: ",bill50)
    print("Billetes de 20: ", bill20)
    print("Billetes de 10: ", bill10)
    print("Billetes de 5: ", bill5)
