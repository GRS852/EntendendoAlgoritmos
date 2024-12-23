def cont_rec(list):
    
    if list == []:
        return  0
    return 1 + cont_rec(list[1:]) 

list = [1,2,3]

print(cont_rec(list))