# a=5
# b=0 

# if b==0:
#     print("Error: Division por cero")
# else:
#     print(a/b)
# #---------------------------------------------------------   
# if b!=0:
#     print(a/b)
# else:
#     print("Error: Division por cero")
# #-----------------------------------------------------------
# if b==0:print("Error: Division por cero")
# else:print(a/b)
#------------------------------------------------------


print("Menu de operaciones")


print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")



opcion = int(input("Ingrese la opcion que desee: "))

if opcion >= 1 and opcion <= 5:
    num1 = float(input("Ingrese el primer numero: "))
    num2 = float(input("Ingrese el segundo numero: "))
    if opcion == 1:
        print("Sumar")
        suma = num1+num2

        if suma > 0:
            print("La suma es positiva")
            print(f"El resultado de la suma es: {suma}")
            print(f"Suma es un tipo de dato ", type(suma))
            print("----------------------------------------------")
        else:
            print("La suma es negativa")
            print(f"El resultado de la suma es: {suma}")
            print(f"Suma es un tipo de dato ", type(suma))
            print("----------------------------------------------")

#---------------------------------------------------------

#2. Restar
    elif opcion == 2:
        print("Restar")
        resta= num1-num2
        if resta > 0:
            print("La resta es positiva")
            print(f"El resultado de la resta es: {resta}")
            print(f"Resta es un tipo de dato ", type(resta))
            print("----------------------------------------------")
        else:
            print("La resta es negativa")
            print(f"El resultado de la resta es: {resta}")
            print(f"Resta es un tipo de dato ", type(resta))
            print("----------------------------------------------")
        
    #----------------------------------------------

    #3. Multiplicar
    elif opcion == 3:
        print("Multiplicar")
        
        multiplicacion = num1 * num2

        if multiplicacion > 0:
            print("La multiplicación es positiva")
            print(f"El resultado de la multiplicación es: {multiplicacion}")
            print(f"Multiplicación es un tipo de dato ", type(multiplicacion))
            print("----------------------------------------------")
        elif multiplicacion == 0:
            print("La multiplicacion es 0")
            print(f"El resultado de la multiplicación es: {multiplicacion}")
            print(f"Multiplicación es un tipo de dato ", type(multiplicacion))
            print("----------------------------------------------")
        elif multiplicacion < 0:
            print("La multiplicación es negativa")
            print(f"El resultado de la multiplicación es: {multiplicacion}")
            print(f"Multiplicación es un tipo de dato ", type(multiplicacion))
            print("----------------------------------------------")

    #---------------------------------------------------------

    #4. Dividir
    elif opcion == 4:
        print("Dividir")
        
        if num2 == 0:
            print("No se puede dividir entre 0")
        else: 
            
            dividir = num1/num2

            if dividir > 0:
                print("La división es positiva")
                print(f"El resultado de la división es: {dividir}")
                print(f"División es un tipo de dato ", type(dividir))
                print("----------------------------------------")
            
    elif opcion == 5:
        print("El programa ha terminado")
    else:
        print("No puede ingresar un valor fuera del rango")
        

else:
    print("Opción no válida")

#---------------------------------------------------------

    
#5. Salect option


#6. Ingresar por teclado 2 numeros verifique el tipo de dato

#print(num1, f"El valor {num1} es un tipo de dato : ", type(num1))
#7. Validar que el segundo numero no sea cero
#8. Realizar la Operacion seleccionada
#9. Mostrar el resultado
#10. Validar que la operacion seleccionada sea correcta
#11. Mostrar un mensaje de error si la opcion no es correcta



    