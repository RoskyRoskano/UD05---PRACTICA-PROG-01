
preguntas = int(input("Ingrese la cantidad total de preguntas: "))
correctas = int(input("Ingrese la cantidad de preguntas respondidas correctamente: "))

porcentaje = (correctas / preguntas) * 100

if porcentaje >= 90:
    nivel = "Nivel máximo"
elif 75 <= porcentaje < 90:
    nivel = "Nivel medio"
elif 50 <= porcentaje < 75:
    nivel = "Nivel regular"
else:
    nivel = "Fuera de nivel"

print("Porcentaje de respuestas correctas: ", porcentaje,"%")
print("Nivel del postulante: ",nivel)