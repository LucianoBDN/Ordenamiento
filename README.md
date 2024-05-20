# TP GRUPAL ORDENAMIENTO

- Pio Acosta Abasto
- Luciano Ezequiel Bordon

## Quick_sort sin recursividad

```Python
def swap(array, a, b):
    array[a], array[b] = array[b], array[a]

def particionar(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            swap(array, i, j)
    
    swap(array, i + 1, high)
    
    return i + 1

def quick_sort(array):
    stack = [(0, len(array) - 1)]
    
    while stack:
        low, high = stack.pop()
        if low < high:
            pi = particionar(array, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))
```
---
## Quick_sort con recursividad
```Python
def swap(a: int, b: int):                          
    return b,a

def particionar(array, low, high):                 
    pivote = array[high]                           
    i = low - 1                                       
    for j in range(low, high):                         
        if array[j] <= pivote:                    
            i += 1
            array[i], array[j] = swap(array[i], array[j])      
    array[i + 1], array[high] = swap(array[i + 1], array[high] )
    return i + 1 
    
def quick_sort(array, low, high):
    global c
    c += 1
    if low < high:
        pi = particionar(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
```
Comparando los dos métodos que usamos para ordenar, el que no usa la recursión resultó más rápido. Esto indica que en este caso, esa forma de hacer las cosas es más eficiente.
---
## Insert_sort
```Python
def insert_sort(lista:list) -> list:
     for i in range(1, len(lista)):

        elemento = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > elemento:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento
        
    return lista
```
- Es más eficiente para listas pequeñas y casi ordenadas, con menos comparaciones e intercambios.

## Burbujeo
```Python
def burbujeo(lista:list)-> list:
    for i in range(0, len(lista)-1):
    for j in range(i + 1, len(lista)):
        if lista[i] > lista[j]:
            auxiliar = lista[i]
            lista[i] = lista[j]
            lista[j] = auxiliar
    return lista
```
- Es más simple de entender y puede ser optimizado, pero generalmente menos eficiente debido al mayor número de operaciones.

### conclusión
- Para aplicaciones prácticas, el ordenamiento por inserción suele ser preferido sobre el ordenamiento por burbuja debido a su mayor eficiencia, especialmente en listas parcialmente ordenadas. Sin embargo, para listas pequeñas o en un contexto educativo, ambos algoritmos son útiles para entender los conceptos básicos de ordenamiento.