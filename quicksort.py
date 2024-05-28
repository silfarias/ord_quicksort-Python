def quicksort(lista, inicio, fin):
    if inicio >= fin:
        return lista 
    else:
        pivote = lista[inicio]

        i = inicio + 1
        j = fin

        while i <= j: 
            while i <= j and lista[i] <= pivote: 
                i += 1 
            while i <= j and lista[j] > pivote: 
                j -= 1
            
            if i < j: 
                (lista[i], lista[j]) = (lista[j], lista[i]) 

        (lista[inicio], lista[j]) = (lista[j], lista[inicio])

        quicksort(lista, inicio, j - 1)
        quicksort(lista, j + 1, fin)
    return lista

list_des = [6, 5, 2, 5, 9, 6, 3, 2, 1, 8, 6, 3, 9, 4, 9]
use_quicksort = quicksort(list_des, 0, len(list_des)-1)
print(use_quicksort)