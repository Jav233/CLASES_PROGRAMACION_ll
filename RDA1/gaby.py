# # print("Sistema de edades")
# # edad = int(input("Ingrese la edad: "))
# # peso = float(input("Ingrese el peso (kg): "))
# # while True:
# #     print("1. Estatura en CM")
# #     print("2. Estatura en M")
# #     opcion = int(input("Ingrese la opcion: "))
# #     while opcion < 1 or opcion > 2:
# #         print("Opcion invalida")
# #         opcion = int(input("Ingrese la opcion: "))
# #     if opcion == 1:
# #         estatura = float(input("Ingrese la estatura (CM): "))
# #         print(f"Su estatura es: {estatura} CM")
# #         conversion = estatura/100
# #         print(f"Su estatura en metros es: {conversion} M")
# #     if opcion == 2:
# #         estatura = float(input("Ingrese la estatura (M): "))
# #         print(f"Su estatura es: {estatura} M")
# #         break
# # while True:
# #     print("1. Peso en kg")
# #     print("2. Peso en lb")
# #     opcion = int(input("Ingrese la opcion: "))
# #     while opcion < 1 or opcion > 2:
# #         print("Opcion invalida")
# #         opcion = int(input("Ingrese la opcion: "))
# #     if opcion == 1:
# #         peso = float(input("Ingrese el peso en kg: "))
# #         print(f"El peso en KG es: {peso}")
# #     if opcion == 2:
# #         peso = float(input("Ingrese el peso en lb: "))
# #         print(f"El peso en LB es: {peso} lb")
# #         libras = peso / 2.2
# #         print(f"El peso en KG es: {libras}")
# #         break
# while True:
#     print("Bienvenido a la calculadora de IMC")
#     print("1. Calcular IMC")
#     print("2. Salir")
#     op = int(input("Ingrese la opcion: "))
#     while op < 1 or op > 2:
#         print("Opcion invalida")
#         op = int(input("Ingrese la opcion: "))
#     if op == 1:
#         edad = int(input("Ingrese la edad: "))
#         if edad >0 and edad < 10:
#             print("Peso")
#             while True:
#                 print("1. Peso en kg")
#                 print("2. Peso en lb")
#                 opcion = int(input("Ingrese la opcion: "))
#                 while opcion < 1 or opcion > 2:
#                     print("Opcion invalida")
#                     opcion = int(input("Ingrese la opcion: "))
#                 if opcion == 1:
#                     peso = float(input("Ingrese el peso en kg: "))
#                     print(f"El peso en KG es: {peso}")
#                     print("Usted pertenece a la categoria pitufo")
#                     break
#                 if opcion == 2:
#                     peso = float(input("Ingrese el peso en lb: "))
#                     print(f"El peso en LB es: {peso} lb")
#                     libras = peso / 2.2
#                     print(f"El peso en KG es: {libras}")
#                     print("Usted pertenece a la categoria pitufo")
#                     break
            
#         else:
#             if edad >=18 and edad <80:
#                 print("Estatura")
#                 while True:
#                     print("1. Estatura en CM")
#                     print("2. Estatura en M")
#                     opcion = int(input("Ingrese la opcion: "))
#                     while opcion < 1 or opcion > 2:
#                         print("Opcion invalida")
#                         opcion = int(input("Ingrese la opcion: "))
#                     if opcion == 1:
#                         estatura = float(input("Ingrese la estatura (CM): "))
#                         print(f"Su estatura es: {estatura} CM")
#                         conversion = estatura/100
#                         print(f"Su estatura en metros es: {conversion} M")
#                         print("Pertenece a la categoria grandes")
#                         break
#                     if opcion == 2:
#                         estatura = float(input("Ingrese la estatura (M): "))
#                         print(f"Su estatura es: {estatura} M")
#                         print("Pertenece a la categoria grandes")
#                         break
#                 #print("Pertenece a la categoria grandes")
#             else:
#                 if edad >=11 and edad <= 17:
#                     print("Pertenece a la categoria medianos")
#                 else:
#                     print("Ingrese una edad real")
#     elif op == 2:
#         print("Gracias por usar nuestro programa")
#         break
print("--------------------------------------------------------------")
print("Bienvenido al programa de clasificación para el Mundial")
print("--------------------------------------------------------------")
europa=int(input("Cuantos jugadores hay en Europa: "))
Asia=int(input("Cuantos jugadores hay el Asia: "))
Latino_America=int(input("Cuantos jugadores hay enn Latino America: "))

# Clasificación general según puntos
puntos = int(input("Ingrese el puntaje del equipo: "))
#los puntos tienen que ser mayores o igual a 25
if puntos >= 25:
    print(" Clasifica directamente al Mundial")# se escribe
# de ser menor o igual que20  los puntos ingresados y los puntos tiene que ser menores que 25
elif 20 <= puntos < 25:
    print("El equipo entra a repechaje")
    

    #  Se Análisis en caso de repechaje
    jugador_europa = input("¿Tiene al menos un jugador que juegue en Europa? (sí/no): ").lower()
  #bono
    bono = 0
    
    if jugador_europa == "sí" or jugador_europa == "si":
        #ingresar el valor el millones de dolares 
        precio = float(input("Ingrese el precio del jugador en millones de dólares: "))
        #El precio tiene que ser mayor a 10
        if precio > 10:
            bono = 2
            #Se escribe que el ugador en Europa con precio mayor a 10 millones .  Buen refuerzo (+2 puntos)
            print("Jugador en Europa con precio mayor a 10 millones .  Buen refuerzo (+2 puntos)")
        else:
            bono = 1
            print("Jugador en Europa con precio menor o igual a 10 millones . Refuerzo regular (+1 punto)")
    else:
        print("No tiene jugador destacado en Europa . No se suma nada")
        #Se suma los puntos con el bono 
    puntos_totales = puntos + bono
    print("Puntaje total con bonificación: ")
        #El totald e puntos debe ser mayor o igual que 25
    if puntos_totales >= 25:
        print(" Clasifica al Mundial tras repechaje")
    else:#si no se cumple permanecera en rechaje pero sin certeza de clasificacion 
        print("Permanece en repechaje pero sin certeza de clasificación")
 # si esto no se cumple eL equipo queda eliminado 
else:
    print(" El equipo queda eliminado por puntaje")

    #  Revisión de lesiones y compensación
    lesiones = int(input("¿Cuántos jugadores lesionados tuvo el equipo? (0, 1, 2 o 3): "))
    bono_lesion = 0
   # la lecion tiene que ser igual a 1 para que se cumpla la condicion 
    if lesiones == 1:
        bono_lesion = 1
        print("Tuvo 1 jugador lesionado .Compensación de +1 punto")
    #No se cumple la condicion si lesiones son iguales a 2 o leciones ens igual a 3
    elif lesiones == 2 or lesiones == 3:
        bono_lesion = 2
        print("Tuvo 2 o 3 jugadores lesionados .Compensación de +2 puntos")
    # No se cumplen la condicion 
    else:
        print("No se suma bonificación por lesiones")

    puntos_totales = puntos + bono_lesion
    print("Puntaje total después de compensación por lesiones: ,puntos",puntos_totales,)

    # Nueva verificación con el bono
    if puntos_totales >= 25:
        print(" Clasifica al Mundial por compensación")
    # tiene que ser menor e igual  que 
    elif 20 <= puntos_totales < 25:
        print(" Accede al repechaje por compensación")
    # No se cumple la condicon 
    else:
        print(" Sigue eliminado, no alcanza a clasificar ni con compensación")

        
