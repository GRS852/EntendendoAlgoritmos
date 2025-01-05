def quicksort(array):
    if len(array):
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]
        return quicksort(menores) + [pivo] + quicksort(maiores)

array = [ 10, 5, 2, 3]

print(quicksort(array))