def insert_sort(lista:list) -> list:
    """_summary_: 1.Comienza desde el segundo elemento (índice 1) de la lista.

    2.Considera este elemento como temporalmente "extraído" de la lista.

    3.Compara este elemento con los elementos a su izquierda uno por uno, comenzando desde su posición actual hacia la izquierda.

    4.Si encuentra un elemento que es mayor que el elemento temporal, desplaza ese elemento hacia la derecha para hacer espacio para el elemento temporal.

    5.Repite el paso 4 hasta encontrar el lugar adecuado para insertar el elemento temporal.

    6.Inserta el elemento temporal en la posición adecuada.

    7.Repite los pasos 2 a 6 para todos los elementos restantes en la lista.

    Args:
        lista (list): Recibe una lista

    Returns:
        list: Retorna la lista ordenada
    """
    for i in range(1, len(lista)):

        elemento = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > elemento:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elemento
        
    return lista

import time
start = time.time()
vector = [2,3,4,1,5,8,9]
resultado = insert_sort(vector)
end = time.time()
print(end)
print(start)
print(f"Tiempo: {(end - start)*1000}")
print(resultado)

