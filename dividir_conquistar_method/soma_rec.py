
def soma_rec(list):

    if list == []:
        return 0
    resultado = list[0] + soma_rec(list[1:])
    return resultado

list = [2,4,6]

print(soma_rec(list))