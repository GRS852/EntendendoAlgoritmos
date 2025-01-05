
def invert(n, reversed_num=0):
    if n == 0:
        return reversed_num
    else:
        return invert(n // 10, reversed_num *  10 + n % 10)
    

numero = 12345
numero_revertido = invert(numero)
print(numero_revertido)