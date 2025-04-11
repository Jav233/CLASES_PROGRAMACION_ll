# print("Sistema de edades")
# edad = int(input("Ingrese la edad: "))
# peso = float(input("Ingrese el peso (kg): "))
# while True:
#     print("1. Estatura en CM")
#     print("2. Estatura en M")
#     opcion = int(input("Ingrese la opcion: "))
#     while opcion < 1 or opcion > 2:
#         print("Opcion invalida")
#         opcion = int(input("Ingrese la opcion: "))
#     if opcion == 1:
#         estatura = float(input("Ingrese la estatura (CM): "))
#         print(f"Su estatura es: {estatura} CM")
#         conversion = estatura/100
#         print(f"Su estatura en metros es: {conversion} M")
#     if opcion == 2:
#         estatura = float(input("Ingrese la estatura (M): "))
#         print(f"Su estatura es: {estatura} M")
#         break
# while True:
#     print("1. Peso en kg")
#     print("2. Peso en lb")
#     opcion = int(input("Ingrese la opcion: "))
#     while opcion < 1 or opcion > 2:
#         print("Opcion invalida")
#         opcion = int(input("Ingrese la opcion: "))
#     if opcion == 1:
#         peso = float(input("Ingrese el peso en kg: "))
#         print(f"El peso en KG es: {peso}")
#     if opcion == 2:
#         peso = float(input("Ingrese el peso en lb: "))
#         print(f"El peso en LB es: {peso} lb")
#         libras = peso / 2.2
#         print(f"El peso en KG es: {libras}")
#         break
while True:
    print("Bienvenido a la calculadora de IMC")
    print("1. Calcular IMC")
    print("2. Salir")
    op = int(input("Ingrese la opcion: "))
    while op < 1 or op > 2:
        print("Opcion invalida")
        op = int(input("Ingrese la opcion: "))
    if op == 1:
        edad = int(input("Ingrese la edad: "))
        if edad >0 and edad < 10:
            print("Peso")
            while True:
                print("1. Peso en kg")
                print("2. Peso en lb")
                opcion = int(input("Ingrese la opcion: "))
                while opcion < 1 or opcion > 2:
                    print("Opcion invalida")
                    opcion = int(input("Ingrese la opcion: "))
                if opcion == 1:
                    peso = float(input("Ingrese el peso en kg: "))
                    print(f"El peso en KG es: {peso}")
                    print("Usted pertenece a la categoria pitufo")
                    break
                if opcion == 2:
                    peso = float(input("Ingrese el peso en lb: "))
                    print(f"El peso en LB es: {peso} lb")
                    libras = peso / 2.2
                    print(f"El peso en KG es: {libras}")
                    print("Usted pertenece a la categoria pitufo")
                    break
            
        else:
            if edad >=18 and edad <80:
                print("Estatura")
                while True:
                    print("1. Estatura en CM")
                    print("2. Estatura en M")
                    opcion = int(input("Ingrese la opcion: "))
                    while opcion < 1 or opcion > 2:
                        print("Opcion invalida")
                        opcion = int(input("Ingrese la opcion: "))
                    if opcion == 1:
                        estatura = float(input("Ingrese la estatura (CM): "))
                        print(f"Su estatura es: {estatura} CM")
                        conversion = estatura/100
                        print(f"Su estatura en metros es: {conversion} M")
                        print("Pertenece a la categoria grandes")
                        break
                    if opcion == 2:
                        estatura = float(input("Ingrese la estatura (M): "))
                        print(f"Su estatura es: {estatura} M")
                        print("Pertenece a la categoria grandes")
                        break
                #print("Pertenece a la categoria grandes")
            else:
                if edad >=11 and edad <= 17:
                    print("Pertenece a la categoria medianos")
                else:
                    print("Ingrese una edad real")
    elif op == 2:
        print("Gracias por usar nuestro programa")
        break
    

        
