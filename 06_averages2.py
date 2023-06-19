#Cada arreglo de grades corresponde a las clasificaciones de una estudiante
grades_list = [[2.9, 2.7, 1.7, 4.3, 3.4],[3.9, 4.7, 2.7, 4.3, 3.4],[4.9, 2.7, 3.7, 4.3, 3.4],[5.9, 2.7, 3.7, 2.3, 1.4],[1.9, 4.7, 4.7, 2.3, 3.6]]

#Se pide calcular el promedio de cada estudiante en un nuevo arreglo llamado averages

averages = []

for grades in grades_list:
    sum = 0
    for grade in grades:
        sum += grade
    average = sum/len(grades)    
    averages.append(average)


print(averages)