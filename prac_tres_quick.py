import time
import random

# Funcion que particiona el arreglo en dos partes basado en un pivote
def particionar(arreglo, inicio, fin):
    pivote = arreglo[fin]  # Elegir el último elemento como pivote
    i = inicio - 1  # Indice del elemento más pequeño

    for j in range(inicio, fin):
        if arreglo[j] <= pivote:
            i += 1
            arreglo[i], arreglo[j] = arreglo[j], arreglo[i]  # Intercambiar

    arreglo[i + 1], arreglo[fin] = arreglo[fin], arreglo[i + 1]  # Mover pivote a su posición
    return i + 1

# Funcion recursiva de Quick Sort
def ordenar_quick(arreglo, inicio, fin):
    if inicio < fin:
        # Particionar el arreglo y obtener el índice del pivote
        pivote_indice = particionar(arreglo, inicio, fin)
        # Ordenar de forma recursiva las dos partes
        ordenar_quick(arreglo, inicio, pivote_indice - 1)
        ordenar_quick(arreglo, pivote_indice + 1, fin)

# Funcion para medir el tiempo de ejecucion
def medir_tiempo_quick(arreglo):
    tiempo_inicial = time.time()
    ordenar_quick(arreglo, 0, len(arreglo) - 1)
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicial

# Prueba con arreglos de diferentes tamanios
for tamano in [10, 100, 1000, 10000]:
    arreglo = random.sample(range(tamano * 10), tamano)  # Arreglo aleatorio
    tiempo_ejecucion = medir_tiempo_quick(arreglo)
    print(f"Tamano del arreglo: {tamano}, Tiempo de ejecucion Quick Sort: {tiempo_ejecucion:.6f} segundos")
