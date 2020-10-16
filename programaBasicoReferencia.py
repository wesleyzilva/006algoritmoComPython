#Biblioteca de consulta de código para lembrar em aula
print('')
print('Primeiro programa')
NOME = input('Digite seu nome: ');
print('Olá Mundo ! '+NOME);

#simulando soma de valores
print('')
print('Conversão de tipos primitivos')
print('Digite o valor1: ')
valor1 = input('Valor1: ') #Input sempre é string ""
print('Digite o valor2: ')
valor2 = input('Valor2: ')
soma = valor1 + valor2
print('Veja que é um operador de caracter, fazendo uma concatenação.')
print ('As strings concatenadas resultam:',soma)
soma = int(valor1)+int(valor2)
print ('A soma é: ',soma)

#melhorando a navegabilidade para reduzir a codificação
print('')
print('Redução de linhas')
valor = int(input('Digite um valor para teste de conversão de String e Int: '))
print('Valor1: ', valor)

#Exercícios.
print('')
anos = int(input('Digite sua idade: '))
dias =  (12*30) + (anos*365)
print(dias) #a linguagem é case sensitive para variáveis

#Exercícios.
print('')
raio = float(input('Digite o valor do raio: '))
area = raio*raio*3,14
print("Area:",area)
print(f"Area: {area}")

#Condições são identadas
print('')
print('Repetição While identada')
contador = 1
soma = 0
while (int(contador) <= 2):
    valor = int(input('Digite um valor: '))
    soma = int(soma) + valor
    contador = int(contador) + 1 #para repetição é necessário um limite final
    media = soma/2
print (f"A média é: {media}")

#
print('')
print('Repetição While com Condicional If')
valor = int(input('Digite um valor: '))
while (valor<99):
    if (valor%2) == 0:
        print(valor, ' par')
        valor=valor+1
    else:
        print(valor, 'impar')
        valor=valor+1

#Exercício calculo de raizes da equação de segundo grau
#ax²+bx+c=0 e delta=b²-4*a*c
#se delta < 0 não existem raizes reais
#se delta = 0 existe uma raiz real
#se delta > 0 existem duas raizes reais
    #x=(-b+-Raiz(delta))/2*a
print("");
print("Cálculo de equação de segundo grau.");
a = int(input("Digite um numero inteiro a: "));
b = int(input("Digite um numero inteiro b: "));
c = int(input("Digite um numero inteiro c: "));
delta = float(b*b-4*a*c)
print("Delta é: ", delta)

if (delta < 0):
    print("Não existem raizes reais, favor tentar com outros números.")
if (delta == 0): 
    x = float((-b)/2*a)
    print("O valor de x é: ", x)
if (delta > 0):
    raizDelta = math.sqrt(delta) #Raiz quadrada com uma bilbioteca
    x1 = (-b+raizDelta)/(2*a)
    x2 = (-b-raizDelta)/(2*a)
    print("X1: ", x1, " X2: ", x2)

#Exercicio de descontos
