##Repetições com ENQUANTO(WHILE)
#soma de numeros positivos de 1 a 100
print("#1 soma de numeros positivos de 1 a 100")
numeroInicio = 0 
numeroFinal = 100
soma = contador = 0
while numeroInicio <= numeroFinal:
    numeroInicio = numeroInicio+1
    print(numeroInicio)
    if (numeroInicio % 2) == 0:    
        print("Número par, somar: ")
        soma = soma + numeroInicio
        print("Resultado da soma: ", soma)

#media aritimética entre 13 e 73
print("#2 media aritimética entre 13 e 73")
numeroInicio = 13
numeroFinal = 73
soma = quantidade = 0
while numeroInicio <= numeroFinal:
    numeroInicio=numeroInicio+1
    quantidade = quantidade +1
    soma = soma + numeroInicio
media = soma/quantidade
print("Média: ", media)


#comparação de alturas entre as pessoas/crescimento
print("#3 comparação de alturas entre as pessoas/crescimento")
anos = 0
alturaChico = 1.5
alturaZe = 1.1
while alturaChico > alturaZe:
    anos=anos+1
    alturaChico=alturaChico+0.02
    alturaZe=alturaZe+ 0.03
print("Em ", anos, "anos.")     

#divisao entre 2 numeros com condição de entrada e de saida (número negatívo).
#leitura de variável fora e dentro do loop.
# print("#4 divisao entre 2 números")
# n1 = int(input("Digite um número: "))
# n2 = int(input("Digite um número: "))
# resultado = 0
# while (n1>=0) and (n2>=0):
#     if n2>0:
#         resultado = n1/n2
#         print("Resultado: ", resultado)
#     else:
#         print("Não existe divisão por zero.")    
#     n1 = int(input("Digite outro número: "))
#     n2 = int(input("Digite outro número: "))

#exercicios mutantes
# print("#5 exercicos mutantes: media, tempo total, menor tempo")
# volta = 1
# tempoVolta = tempoTotal = 0
# while volta < 11:
#     tempoVolta=int(input("Digite o tempo da volta: "))
#     tempoTotal = tempoTotal + tempoVolta
#     if volta == 1 : #observe que no primeiro caso 
#         melhorTempo = tempoVolta
#         voltaMelhorTempo = 1
#         print("Primeira volta: ", tempoVolta, " segundos.")
#     elif tempoVolta < melhorTempo:
#         melhorTempo = tempoVolta
#         voltaMelhorTempo -1= volta
#     volta=volta+1

# tempoMedio = tempoTotal/10
# print("Tempo médio: ", tempoMedio)
# print("Melhor tempo: ", melhorTempo)
# print("Melhor volta: ", voltaMelhorTempo)


#exercicio numerador e denominador
# print("#9 numerador e denominador")
# numerador = denominador = 1
# soma = 0
# #Observe a utilização do comando "end" na string de impressão para imprimir na mesma linha
# print("S = ", end="")
# while numerador < 51:
#     if numerador == 1:
#         print(numerador, " / ",denominador, end="")
#     else:
#         print(" + ",numerador, " / ",denominador, end="")
#     numerador=numerador+1
#     denominador=denominador+2
#     resultado=denominador/numerador
#     # print(denominador, " / ", numerador,"=",resultado)
#     # print("Resultado: ", resultado)
#     soma=soma+resultado
# print("Somatória: ", soma)

# #Fatorial e multiplicação
# print("#10 fatorial ou multiplicação")
# numero=int(input("Digite um número para cálculo do fatorial:"))
# resultadoFatorial = 1
# while numero>1:
#     resultadoFatorial = resultadoFatorial*numero
#     print("Resultado do cálculo: ", resultadoFatorial)
#     numero= numero-1
#     print("Número antecessor: ", numero)
# print("Resultado fatorial: ", resultadoFatorial)


#Exercicio quem faltou dia 20201027
# 1 minuto = 60 segundos
# 1 hora = 60 minutos

segundos = 0
minutos = 59
horas = 23
print(horas, ":", minutos, ":", segundos)
while (horas != 1) and (minutos!=2):
    segundos=segundos+1
    print(horas, ":", minutos, ":", segundos)
    if (segundos >= 59):
        segundos=0
        minutos=minutos+1
        print(horas, ":", minutos, ":", segundos)
        if (minutos >= 59):
            minutos=0
            horas=horas+1
            print(horas, ":", minutos, ":", segundos)
            if (horas > 23):
                horas = 0
                print(horas, ":", minutos, ":", segundos)
                segundos = segundos+1
                if (segundos >= 59):
                    segundos=0
                    minutos=minutos+1
                    print(horas, ":", minutos, ":", segundos)