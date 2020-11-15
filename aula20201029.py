#Repetições com PARA(FOR)
#Variável com quantidade definida de iterações.
#for <variavel> in range (valorInicial, condicionalParada, passo)
#condicionalParada = limite de 1 acima.

for contadorLista in range(1,11):
    print (contadorLista)


soma = 0
for contadorLista in range(1,11):
    if (contadorLista % 2 == 0):
        print(contadorLista)
        soma=soma+contadorLista
print(soma)


for contadorLista in range(2,11,2):
    print(contadorLista)
    soma=soma+contadorLista
print(soma)

#Engregagem de testes de um relógio.
#Formatação de saída de string/inteiro
hora = 13
minuto = 00
for hora in range(13, 19):
    for minuto in range(0,60):
        print(hora, ":",format(minuto,'03d'))

