#xn = x * xn-1


def two_numbers(x, n):

    if n == 0:
        return 1
    
    else:
        return  x * two_numbers(x, n -1)

      
print (two_numbers(3, 2))
    
#Caso  base: n == 2
