def quicksort(lista, inicio, fin):
    if inicio >= fin: # si el indice de inicio es mayor o igual al indice de fin (lista con 0 o 1 elementos)
        return lista # no hay que ordenar nada y retornamos la lista como está
    else:
        pivote = lista[inicio] # elegimos el primer elemento de la lista como pivote 

        # comenzamos proceso de particion
        i = inicio + 1 # indice inicial de la lista, apunta al segundo elemento
        j = fin # indice final de la lista

        while i <= j: # mientras los indices i y j no se crucen
            while i <= j and lista[i] <= pivote: 
                i += 1 # mueve i hacia la derecha
            while i <= j and lista[j] > pivote: 
                j -= 1 # mueve j hacia la izquierda 
            
            if i < j: 
                (lista[i], lista[j]) = (lista[j], lista[i]) # intercambia los dos elementos que estan en el lado incorrecto del pivote

        (lista[inicio], lista[j]) = (lista[j], lista[inicio]) # colocamos el pivote en la posicion correcta (se intercambia con el elemento en la posicion j)

        # llamamos recursivamente a la lista izquierda y derecha
        quicksort(lista, inicio, j - 1)
        quicksort(lista, j + 1, fin)

    return lista # retornamos la lista ordenada

list_des = [6, 5, 2, 5, 9, 6, 3, 2, 1, 8, 6, 3, 9, 4, 9]
use_quicksort = quicksort(list_des, 0, len(list_des)-1)
print(use_quicksort)