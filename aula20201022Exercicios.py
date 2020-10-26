#Media aritmética entre 13 e 93
inicio = int(13);
fim = int(93);
contadorNumeros = 0;
somaNumeros = 0;
while inicio <= fim:
    contadorNumeros = contadorNumeros+1;
    somaNumeros = somaNumeros + inicio;
    inicio = inicio+1;
    print(inicio, contadorNumeros, somaNumeros);

media = somaNumeros/contadorNumeros;
print(media);
print('');

#meninoHeitor = 1,5 e cresce = 0,02cm/ano
#meninoSamuel = 1,1 e cresce = 0,03cm/ano
#Em quantos anos Samuel será Maior que Heitor?
alturaSamuel = float(1.1);
alturaHeitor = float(1.5);
crescimentoSamuel = float(0.03);
crescimentoHeitor = float(0.02);
ano = int(0);
while alturaSamuel <= alturaHeitor:
    ano = ano+1;
    print("ANO:", ano,"aSamuel", '{0:.2f}'.format(alturaSamuel),"aHeitor", '{0:.2f}'.format(alturaHeitor));
    alturaSamuel = alturaSamuel+crescimentoSamuel;
    alturaHeitor = alturaHeitor + crescimentoHeitor;
print("Em",ano, "anos. ");
print("")

#exercico4
from random import randrange
resultado = 1;
if resultado > 0:
    numero1 = randrange(0,999);
    numero2 = randrange(-10,100);
    resultado = numero1/numero2;    
else:
    print("Divisão por zero !!! FIM")
print("Resultado: ",'{0:.2f}'.format(resultado));
print('');

#exercicio5
tempoMedioVoltas = 0;
menorTempo = 100;
voltaMenorTempo = 0;

voltas = 3;
totalVoltas = 0;
somaTempos = 0;
# for i in range (voltas):
#     tempoVolta = int(input('Digite o tempo da volta: '));
#     somaTempos = somaTempos + tempoVolta;
#     if tempoVolta < menorTempo:
#         menorTempo = tempoVolta;
#         voltaMenorTempo = i;
#     totalVoltas = totalVoltas + i;
#     print(totalVoltas);
mediaTempos = somaTempos/voltas;
print("");
print("Menor tempo: ",menorTempo);
print("Volta com o menor tempo: ", voltaMenorTempo);
print("Média de tempos: ",mediaTempos)

#exercício6
pessoaQuantidade = 2;
somaIdades=0;
contaObeso=0;
contaMagricelo=0;
# for i in range (pessoaQuantidade):
#     pessoaIdade = int(input("Digite a idade da pessoa: "))
#     pessoaAltura = float(input("Digite a altura da pessoa: "))
#     pessoaPeso = float(input("Digite o peso da pessoa: "))
#     somaIdades = somaIdades + pessoaIdade;
#     mediaIdades = somaIdades / pessoaQuantidade;
#     if (pessoaPeso > 90) and (pessoaAltura < 1.50):
#         contaObeso = contaObeso +1;
#     elif (pessoaIdade >= 10) and (pessoaIdade <= 30) and (pessoaAltura > 1.90):
#         contaMagricelo = contaMagricelo + 1;
#print("Media das idades: ", mediaIdades,"Obesos: ", contaObeso,"Magricelos: ", contaMagricelo);

#exercicio8
nota = 10;
totalAlunos = qtdNotaMenor = qtdNotas6 = qtdNotas46 = 0;
while nota > 0:
    totalAlunos = totalAlunos + 1;
    nota = int(input("Nota do aluno: "));
    if nota >= 6:
        qtdNotas6 = qtdNotas6+1;
    elif (nota >=4) and (nota<6):
        qtdNotas46 = qtdNotas46+1;
    elif (nota < 4):
        qtdNotaMenor = qtdNotaMenor+1;
print(totalAlunos, qtdNotas6, qtdNotas46, qtdNotaMenor);
print("");