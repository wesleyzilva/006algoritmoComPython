# Receber 2 notas de um aluno, e a quantidade de faltas.
# Verificar a situação do aluno:
#   reprovado por faltas: faltas > 20
#   aprovado: média ≥ 6.0
#   prova final: média entre 4.0 e 6.0
#   reprovado por média: média menor que 4.0
# algoritmo + código em Python

# Declare 
#     nota1, nota2, media real 
#     faltas inteiro
# inicio
#     Escreva("Digite a nota1 do aluno: ");   
#     leia nota1;
#     Escreva("Digite a nota2 do aluno: ");   
#     leia nota2;
#     Escreva("Digite a quantidade de faltas do aluno: ");   
#     leia faltas;
#     se (faltas < 20) então:
#         escreva ("Aluno não reprovado por faltas, validando notas");
#         media = (nota1 + nota2)/2;
#         se (media < 4) então:
#             escreva ("Aluno reprovado.");
#         senão se (media >=4 ) ou (media <6) então:
#             escreva ("Aluno em recuperação.");
#         senão se (media >6) então:
#             escreva ("Aluno aprovado.")
#     senão
#         escreva ("Aluno reprovado por faltas.");
#     fim_se
# fim

nota1 = float(input('Digite a nota1 do aluno: '));
nota2 = float(input('Digite a nota2 do aluno: '));
faltas = int(input('Digite o numero de faltas do aluno: '))
media = (nota1 + nota2)/2;
if (faltas > 20 ) :
    print('Aluno reprovado por falta. Não é necessário validar média de notas');
    pass
else:
    if (media < 4):
        print('Aluno reprovado por média baixa, porém, com presença.');
    if (media >= 4) and (media < 6):
        print('Aluno em recuperação, porém, com presença.');
    if (media >=6):
        print("Aluno aprovado.");