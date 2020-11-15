#Repetições com PARA(FOR)
#Variável com quantidade definida de iterações.
#for <variavel> in range (valorInicial, condicionalParada, passo)
#condicionalParada = limite de 1 acima.

for contadorLista in range(1,11):
    print (contadorLista)

#
soma = 0
for contadorLista in range(1,11):
    if (contadorLista % 2 == 0):
        print(contadorLista)
        soma=soma+contadorLista
print(soma)

#
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
        print(format(hora,'03d'), ":",format(minuto,'03d'))

#tabuada
for numeroTabuada in range (0,11):
    print(numeroTabuada , " X 3 = ",format(numeroTabuada*3, '02d'))

# numero = 1
# while (numero != 0):
#     numero = int(input("Digite um numero para ver a tabuada:"))
#     for numeroTabuada in range (0,11):
#         print(numeroTabuada , " X ", numero, " = ",format(numeroTabuada*numero, '02d'))

#
# for contador in range (1,11):
#     numero=int(input("Digite: "))
#     soma=soma+numero
#     media=soma/contador
# print(soma)
# print(media)

###########################################
#Exercicio 5,6,9 10 quem faltou dia 20201029
#5
# volta = 1
# tempoVolta = tempoTotal = 0
# melhorTempo = 0
# for volta in range (0,4):
#      tempoVolta=int(input("Digite o tempo da volta: "))
#      tempoTotal = tempoTotal + tempoVolta
#      if volta == 1 : #observe que no primeiro caso 
#          melhorTempo = tempoVolta
#          voltaMelhorTempo = 1
#          print("Primeira volta: ", tempoVolta, " segundos.")
#      elif tempoVolta < melhorTempo:
#          melhorTempo = tempoVolta
#          voltaMelhorTempo = volta
# tempoMedio = tempoTotal/4
# print("Tempo médio: ", tempoMedio)
# print("Melhor tempo: ", melhorTempo)
# print("Melhor volta: ", voltaMelhorTempo)

###########################################
#6
# idade = peso = altura = 0
# quantidadePessoas = somaIdade = mediaIdade = 0
# contadorPessoasObesas = contadorPessoasAltas = 0
# for pessoas in range (0,2):
#     idade = int(input("Idade: "))
#     peso = int(input("Peso: "))
#     altura = float(input("Altura: "))
#     if (peso > 90 and altura < 1.5):
#         contadorPessoasObesas=contadorPessoasObesas+1
#     elif (((idade>10) and (idade<30)) and (altura > 1.9)):
#         contadorPessoasAltas=contadorPessoasAltas+1
#     quantidadePessoas=quantidadePessoas+1
#     somaIdade = somaIdade+idade
#     mediaIdade = somaIdade / quantidadePessoas

#     print(quantidadePessoas)
#     print(somaIdade)
#     print(mediaIdade)
#     print(contadorPessoasObesas)
#     print(contadorPessoasAltas)

###########################################
#9
#S = numerador/denominador
# numerador = denominador = 1
# print ("S = ")
# for denominador in range (1,99):
#     numerador=numerador+2
#     if numerador == 1:
#         print(numerador,"/",denominador)
#     else:
#         print("+",numerador,"/",denominador)
#     resultadoDivisao = numerador/denominador
#     print(resultadoDivisao)
#     soma=soma+resultadoDivisao
# print(soma)

#10 fatorial
#5!=5x4x3x2x1=120
numero=int(input("numero:"))
resultadoFatorial = 1
for numero in range (1,numero+1):
    print(numero)
    resultadoFatorial = resultadoFatorial*numero
print(resultadoFatorial)