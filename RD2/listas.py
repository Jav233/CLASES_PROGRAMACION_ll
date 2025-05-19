lista = [1,2,3,4,5,6,7,8,9,9,10]
lista.remove(9)
#
# lista.remove(9)
print(lista)
#Un arreglo debe contener el mismo tipo de datos, pero una lista puede contener diferentes tipos de datos
#Ejercico 1: Recorrer una lista e imprimir sus elementos

numeros = [5,8,2,9,1,1]
for num in numeros:
    print(num, end=" ")

suma = 0
for num in numeros:
    suma += num
print(f"\nLa suma de los elementos de la lista es: {suma}")

numeros_1 = [12,45,3,22,89,5]
mayor = numeros_1[0]
for num in numeros_1:
    if num > mayor:
        mayor = num
print(f"El mayor elemento de la lista es: {mayor}")

numeros_2 = [4,7,10,3,2,9,8]
pares  = 0
for num in numeros_2:
    if num % 2 == 0:
        pares += 1
print(f"El número de elementos pares en la lista es: {pares}")

cuadrados = []
for i in range(1, 6):
    cuadrados.append(i**2)
print(f"Los cuadrados de los números del 1 al 5 son: {cuadrados}")