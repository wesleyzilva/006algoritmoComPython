#Programa de calculo para venda de tintas baseado na área á ser pintada.
#Considere 1 litro de tinta = 3 metros quadrados de parede pintada = R$80,00
#Informe quantas latas de tintas o usuário vai precisa comprar
#Observe que caso use inteiro ou real vamos ter uma variação do valor devido a precisão.
metragemPintura = int(input('Digite a área á ser pintada: '));
litrosnecessarios = int((metragemPintura/3));
print ("Serão necessários ", litrosnecessarios, " litros.");
valor = int(litrosnecessarios * 80);
print ("Valor total R$", valor);