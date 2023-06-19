grades = [2.9, 2.7, 1.7, 4.3, 3.4]

#Utilizando los métodos len() y for. Calcular el promedio de las notas 
sum = 0
for grade in grades: 
    sum += grade

print(f"El promedio de notas es: {sum/len(grades)}")