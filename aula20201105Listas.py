#vetor é uma lista homogênea
#variáveis compostas (lista heterogênea)
#Gaveta é a lista onde está armazenado os elementos em índices
L = ['elemento01', 'elemento02', 'elemento03', 'elemento04', 'elemento05', 'elemento06', 'elemento07']
print("Conteudo da lista heterogênea L", L)
print("Indice/Posição 0: ", L[0])
print("Característica/Atributo: Tipo: ", type(L[0]))
print("Característica/Atributo: Comprimento: ", len(L))
print()

#Percorrer uma lista via loop
#FOR: Melhor para percorrer todos os elementos da lista sem o indice (apenas conteudo) 
for nota in L:
    print(nota)
print()

for indice in range(0,len(L)):
    print(L(indice))

#WHILE: Apenas para usar enquanto procura um valor.
print("Loop WHILE para ver elementos baseados no índice")
indice = 0
while indice < len(L):
    print(L[indice])
    indice=indice+1
