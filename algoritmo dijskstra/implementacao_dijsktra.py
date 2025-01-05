grafo = {}

# Representando o grafo, com uma tabela hash

grafo["inicio"] = {}
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2 
grafo["a"] = {}
grafo["a"]["fim"] = 1
grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5
grafo["fim"] = {}

# Para representar um tempo infinito em python:

infinito = float("inf")

#Tabela de pesos para cada parte do grafo. (para usar o dijsktra cada grafo tem que ter um peso/custo)

custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

#Tabela para os pais

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None

#Vertice para manter todos os arrays, que já foram procesasados pelo algoritmo

processados = []

#Função para achar o valor mais baixo

def ache_no_custo_mais_baixo(custos):
    custo_mais_baixo = float("inf")
    nodo_custo_mais_baixo = None
    for nodo in custos:
        custo = custos[nodo]
        if custo < custo_mais_baixo and nodo not in processados:
            custo_mais_baixo = custo
            nodo_custo_mais_baixo = nodo
    return nodo_custo_mais_baixo

nodo = ache_no_custo_mais_baixo(custos)

while nodo is not None:
    custo = custos[nodo]
    vizinhos = grafo[nodo]
    for n in vizinhos.keys():
        novo_custo = custo + vizinhos[n]
        if custos[n] > novo_custo:
            custos[n] = novo_custo
            pais[n] = nodo
    
    processados.append(nodo)
    nodo = ache_no_custo_mais_baixo(custos)

