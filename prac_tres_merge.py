import time
import random

# Funcion merge que combina los subarreglos
def combinar(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Funcion recursiva de Merge Sort
def ordenar_merge(arreglo):
    if len(arreglo) <= 1:
        return arreglo
    mitad = len(arreglo) // 2
    izquierda = ordenar_merge(arreglo[:mitad])
    derecha = ordenar_merge(arreglo[mitad:])
    return combinar(izquierda, derecha)

# Funcion para medir el tiempo de ejecucion
def medir_tiempo(arreglo):
    tiempo_inicial = time.time()
    arreglo_ordenado = ordenar_merge(arreglo)
    tiempo_final = time.time()
    return tiempo_final - tiempo_inicial

# Prueba con arreglos de diferentes tamanios
for tamano in [10, 100, 1000, 10000]:
    arreglo = random.sample(range(tamano * 10), tamano)  # Arreglo aleatorio
    tiempo_ejecucion = medir_tiempo(arreglo)
    print(f"Tamano del arreglo: {tamano}, Tiempo de ejecucion: {tiempo_ejecucion:.6f} segundos")
