


def buscaMenor(arr):

    menor = arr[0]
    menor_indice = 0

    for i in range(2, len(arr)):
        print(f"Esse é o I: {i}")
        if arr[i] < menor:

            print(f"esse é o array: {arr[i]}")
            menor = arr[i]
            menor_indice = i

    return menor_indice


def ordenacaoporSelecao(arr):
    novoArr = []
    for i in range(len(arr)):
        menor = buscaMenor(arr)
        novoArr.append(arr.pop(menor))
    return novoArr


print(ordenacaoporSelecao([5, 3 ,6, 2, 10]))