#Encontrar valor mais alto de uma lista, recursivamente

def valor_mais_alto(list):                    

    if len(list) == 2:
        print(len(list))
        return list[0] if list[0] > list[1] else list[1]
    sub_max = valor_mais_alto(list[1:])
    return list[0] if list[0] > sub_max else sub_max
  
    

list = [100, 90, 80, 70, 55, 50, 1]
print(valor_mais_alto(list))