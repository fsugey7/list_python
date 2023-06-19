dogs = []
menu_option = ""

while menu_option != "3":
    print(f"1. inscribir cachorro\n"
          f"2. ver cachorritos\n"
          f"3. salir\n")
    menu_option = input()

    if menu_option == "1":
        dog = []
        name = input("Ingrese el nombre de su cachorro\n")
        age = input("Ingrese la edad de su cachorro\n")
        breed = input("Ingrese la raza de su cachorro\n")
        dog.append(name)
        dog.append(age)
        dog.append(breed)
        dogs.append(dog)
        print("Cachorrito agregado con exito")

    elif menu_option == "2":
        number = 0
        while number < len(dogs):
            print("----------------")
            print(f"nombre: {dogs[number][0]}")
            print(f"edad: {dogs[number][1]}")
            print(f"raza: {dogs[number][2]}")
            number += 1
    
    elif menu_option == "3":
        print("Gracias por su registro ¡Hasta pronto!")





