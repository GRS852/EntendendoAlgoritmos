
votaram = {}

def verifica_eleitor(nome):
    if votaram.get(nome):
         print ("Mande Embora!")
    else:
        votaram[nome] = True
        print ("Deixe votar!")
        
verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("mike")