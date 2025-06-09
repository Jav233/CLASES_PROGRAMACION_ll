import random
import bisect
import matplotlib.pyplot as plt
import pandas as pd
import time
from tqdm import tqdm
from IPython.display import clear_output
import time as t

calificaciones = []
for i in range(15):
    calificaciones.append(random.randint(0, 21))

print("Calificaciones finales:")
for i, nota in enumerate(calificaciones, 1):
    print(f"Estudiante {i:2}: {nota}")
    

def bubble_sort_viz(lista, mostrar_pasos=False, pausa=0.3):
    # Creamos una copia de la lista para no modificar la original
    lista = lista.copy()

    # Inicializamos contadores para registrar la cantidad de comparaciones e intercambios
    comparaciones = 0
    intercambios = 0

    # Guardamos la longitud de la lista
    n = len(lista)

    # Lista donde se almacenarán los pasos intermedios (solo si mostrar_pasos=True)
    pasos = []
    
    for i in range(n):
        
        for j in range(0, n-i-1):
            
            comparaciones += 1
            
            if lista[j] > lista[j+1]:
                
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
                intercambios += 1
                
                pasos.append(lista.copy())
                if mostrar_pasos:
                    print(f"Paso {len(pasos)}: {lista}")
                    time.sleep(pausa)
                if mostrar_pasos:
                    plt.clf()
                    plt.bar(range(len(lista)), lista, color='blue')
                    plt.title(f'Paso {i*n+j+1}')
                    plt.pause(pausa)

    return lista, comparaciones, intercambios, pasos

ordenadas, comp, interc, pasos = bubble_sort_viz(calificaciones, mostrar_pasos=True, pausa=0.5)

print("\nCalificaciones ordenadas:")
for i, nota in enumerate(ordenadas, 1):
    print(f"Estudiante {i:2}: {nota}")

print(f"\nTotal comparaciones: {comp}")
print(f"Total intercambios: {interc}")

#Sorted

ordenado = sorted(calificaciones)
print("Calificaciones originales: ", calificaciones)
print("Calificaciones ordenadas (sorted):", ordenado)

def animar_comparacion_sorted_bubble_simulada(lista_original, pausa=0.2):

    # Creamos una copia de la lista original para Bubble Sort
    lista_bubble = lista_original.copy()

    # Calculamos el resultado final de sorted() (lista ordenada) para simularlo paso a paso
    lista_sorted_final = sorted(lista_original)

    # Inicializamos la lista de pasos del algoritmo Bubble Sort (comenzamos con el estado original)
    pasos_bubble = [lista_bubble.copy()]

    # Lista de pasos para simular el comportamiento de sorted()
    pasos_sorted = []

    # 🔄 Generamos los pasos reales de Bubble Sort
    n = len(lista_bubble)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_bubble[j] > lista_bubble[j + 1]:
                # Intercambiamos los elementos si están fuera de orden
                lista_bubble[j], lista_bubble[j + 1] = lista_bubble[j + 1], lista_bubble[j]
                # Guardamos el estado actual después del intercambio
                pasos_bubble.append(lista_bubble.copy())

    # 🧪 Simulamos cómo se vería el progreso de sorted() paso a paso
    # Aunque sorted() es inmediato, aquí lo representamos como una transformación progresiva
    lista_simulada = lista_original.copy()
    for i in range(len(lista_sorted_final)):
        if lista_simulada[i] != lista_sorted_final[i]:
            # Sustituimos el valor por el que estaría en la lista ordenada
            lista_simulada[i] = lista_sorted_final[i]
        # Guardamos el paso simulado
        pasos_sorted.append(lista_simulada.copy())

    # Definimos el número total de pasos que tendrá la animación (el mayor entre ambos procesos)
    total_pasos = max(len(pasos_bubble), len(pasos_sorted))
    
    # 🔄 Ventana única
    plt.ion()  # Modo interactivo activado
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))

    # 🖼️ Animación paso a paso
    for k in range(total_pasos):
        for ax in axs:
            ax.cla()  # Limpiar cada gráfico antes de redibujar
            
        clear_output(wait=True)  # Limpiamos la salida anterior para crear efecto de movimiento

        # Creamos una figura con dos gráficos uno al lado del otro
        #fig, axs = plt.subplots(1, 2, figsize=(12, 4))

        # 🎬 Animación de Bubble Sort (proceso real)
        if k < len(pasos_bubble):
            axs[0].bar(range(len(pasos_bubble[k])), pasos_bubble[k], color='skyblue')
            axs[0].set_title(f"Bubble Sort - Paso {k+1}")
            axs[0].set_ylim(0, max(lista_original) + 5)
        else:
            # Si se terminaron los pasos, mantenemos la vista final
            axs[0].bar(range(len(pasos_bubble[-1])), pasos_bubble[-1], color='skyblue')
            axs[0].set_title("Bubble Sort - Final")

        # 🎬 Simulación animada de sorted() (transformación progresiva)
        if k < len(pasos_sorted):
            axs[1].bar(range(len(pasos_sorted[k])), pasos_sorted[k], color='lightgreen')
            axs[1].set_title(f"sorted() - Paso {k+1}")
            axs[1].set_ylim(0, max(lista_original) + 5)
        else:
            axs[1].bar(range(len(lista_sorted_final)), lista_sorted_final, color='lightgreen')
            axs[1].set_title("sorted() - Final")

        # Acomoda ambos subgráficos para que no se encimen
        plt.tight_layout()

        # Pausa entre cada frame para que la animación sea visible
        plt.pause(pausa)

    # Muestra la última imagen estática al terminar
    plt.ioff()
    plt.show()
    
#lista_demo = random.sample(range(1, 50), 20)

# 🎞️ Ejecutamos la función de animación comparativa simulada
# Esta función mostrará lado a lado:
# - A la izquierda: el proceso real paso a paso del algoritmo Bubble Sort.
# - A la derecha: una simulación paso a paso de cómo `sorted()` iría construyendo la lista ordenada.
animar_comparacion_sorted_bubble_simulada(calificaciones, pausa=0.5)

#Nueva calificacion
nueva_nota = 15  # puedes cambiar o pedir por input
bisect.insort(calificaciones, nueva_nota)
print("✅ Lista después de insertar la nueva nota:", calificaciones)

nota_buscar = 10  # puedes cambiar o pedir por input
posicion = bisect.bisect_left(calificaciones, nota_buscar)
if posicion < len(calificaciones) and calificaciones[posicion] == nota_buscar:
    print(f"🔍 La nota {nota_buscar} se encuentra en la posición {posicion}")
else:
    print(f"❌ La nota {nota_buscar} no está en la lista.")
    
# # Usamos tqdm para mostrar una barra de progreso mientras se ejecuta el ciclo
# for tam in tqdm(calificaciones):

#     # Generamos una lista aleatoria de 'tam' elementos, sin repetidos, en un rango proporcional
#     lista = random.sample(range(1, tam * 10), tam)

#     # Medimos el tiempo justo antes de ejecutar el algoritmo
#     inicio = time.time()

#     # Ejecutamos bubble_sort_viz pero no nos interesa la lista final ni los pasos,
#     # solo las estadísticas de comparaciones e intercambios
#     _, comp, interc, _ = bubble_sort_viz(lista)

#     # Medimos el tiempo al finalizar
#     fin = time.time()

#     # Guardamos los resultados en un diccionario y lo añadimos a la lista de resultados
#     resultados.append({
#         'Tamaño': tam,
#         'Comparaciones': comp,
#         'Intercambios': interc,
#         'Tiempo (s)': round(fin - inicio, 4)  # Redondeamos a 4 decimales para mayor claridad
#     })

# # 📊 Visualización de los resultados
# # Usamos pandas para crear una tabla (DataFrame) con los resultados obtenidos
# df = pd.DataFrame(resultados)

# # Mostramos la tabla
# df

