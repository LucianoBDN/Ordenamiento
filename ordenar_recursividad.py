c = 0
def swap(a: int, b: int):                          #esta funcion lo que hace es el cambio de ordern de elementos
    return b,a

def particionar(array, low, high):                 #lo que hace es particionar el array en dos tomando el primer elemento y ultimo
    pivote = array[high]                           #El pivote sera el ultimo elemento de la lista
    i = low - 1                                    #i empieza de
        
    for j in range(low, high):                     #itera desde low hasta high -1 inclusive
        
        if array[j] <= pivote:                    
            i += 1
            array[i], array[j] = swap(array[i], array[j])
             #si el elemento de array[j] es menor o igual al pivote se incrementa i y se cambian array[i] y array[j]  
    
    array[i + 1], array[high] = swap(array[i + 1], array[high] )
    #despues que haga todos los intercambios se intercambia array[i + 1] con array [high] reacomodando el pivote en una posicion correcta
    
    return i + 1 #retorna i + 1 que es la posicion final del pivote
    
def quick_sort(array, low, high):
    global c
    c += 1
    if low < high:
        pi = particionar(array, low, high)
        #esta linea llama a la funcion particionar que reordena el array de manera que los elementos menores al pivote esten a la ezquierda y 
        #mayores a la derecha, pi es la posicion final del pivote despues de la particion
        quick_sort(array, low, pi - 1)
        #despues de particionar, se llama recursivamente a quick sort para oredenar la sublista de la izquierda del pivote desde low hasta pi -1
        quick_sort(array, pi + 1, high)
        #se llama a quick sort para ordenar la sublista que esta a la derecha del pivote desde pi + 1 hasta high
        

import time

vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3]
start = time.time()
quick_sort(vector, 0 , len(vector) - 1)
end = time.time()
print(end)
print(start)
print(f"Tiempo: {(end - start)*1000}")
print(c)
print(len(vector))
print(vector)
