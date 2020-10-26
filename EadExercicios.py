# frase = "Eu posso ajudar respondendo perguntas no fórum!"
# sorteio = [5, -8, 11]  
# acertos = 0
# for i in sorteio:
#     resposta = input("Qual o caractere de índice %d? "%(i))
#     if frase[i] == resposta:
#        print("Parabéns, você acertou!")
#        acertos+=1
#     else:
#        print("Você errou. O caractere de índice %d é: %s"%(i, frase[i]))
# print("Você acertou %d de %d perguntas."%(acertos, len(sorteio)))

# 1. Escreva um programa que remove a primeira ocorrência de uma letra
# de uma string. A string e a letra devem ser fornecidas pelo usuário.
print('Tratamento de strings como lista (vetores)');
stringEscrita = input('Digite seu "nome por completo" com maiúsculas e minúsculas para operações com string: ')
print("String digitada: \n", stringEscrita);
print('Digite a operação que gostaria realizar: ');
print('1: Digite a posição que deseja ver o caracter na string digitada:')
print('2: Digite o caracter que você deseja substituir/remover da String digitada:')
print('3: Total de caracteres maiúsculas e minúsculas: ')
print('4: Validando palíndromo: ')
print('5: Contador de palavras: ')
print('6: Imprimir em escada: ')
print('7: Escreva de tras para frente: ')
print('8: ')
print('9: ')
print('10: ')
opcao = int(input('Opção de 1 á 10: '));
if (opcao==1):
    print('Opção 1');
    posicaoStringEscrita = input('Digite a posição que deseja ver o caracter na string digitada: ')
    print("A posição da string ", stringEscrita[int(posicaoStringEscrita)]);
# 2. Escreva um programa que remove todas as ocorrências de uma letra
# de uma string. A string e a letra devem ser fornecidas pelo usuário.
elif (opcao==2):
    print('Opção 2');
    caracterString = input('Digite o caracter que você deseja substituir/remover da String digitada: ')
    print("String digitada: \n",stringEscrita);
    print('');
    print("Tipo: ", type(stringEscrita));
    print("Tamanho do vetor/string", len(stringEscrita));
    print("Formas de impressão de vetores")
    for i in stringEscrita:
        print(i);
    print('');
    for i in stringEscrita:
        if (i == caracterString):
            print(stringEscrita.replace(caracterString, ' '));
    print('');
# 3. Escreva um programa que verifique se duas strings fornecidas pelo
# usuário são iguais e mostre o total de caracteres de cada uma delas.
# Diferencie letras maiúsculas das minúsculas.
elif(opcao==3):
    print('Opção 3');
    print('Validando caracteres da string: ');
    for i in stringEscrita:
        if i.islower():
            print(i, 'caractér minúsculo');

        else:
            print(i, 'CARACTÉR MAÍSCULO');
#print('');
# 4. Escreva um programa que reconhece se uma string é um palíndromo,
# ou seja, se lida do início para o fim é igual se lida do fim para o início.
# Exemplos: arara, ovo, reter, Renner e Miriam.
elif (opcao==4):
    print('Opção 4');
    print('Caracter em lowCase, tirando espaços e substitundo strings vazias ');
    stringEscritaSemEspaco = stringEscrita.lower().strip().replace(' ', '');
    if stringEscrita == stringEscritaSemEspaco[::-1]:
        print(stringEscrita, "é um palindromo.");
    else:
        print('String não é um palíndromo.');
    print('');
# 5. Faça um programa que recebe uma frase e retorna o número de
# palavras que a frase contém.
# 8. Dada uma string com uma frase informada pelo usuário (incluindo
# espaços em branco), conte a quantidade de espaços em branco e a
# quantidade de vezes que aparecem as vogais a, e, i, o, u.
elif (opcao==5):
    print("Opção 5");
    for i in stringEscrita:
        # print(type(i));
        # if type(stringEscrita) == str:
        #     print(stringEscrita);
        # print(i.isspace());
        contadorPalavras = 0;
        teste = i.split();
        print(teste);    
        if (i.isspace() == True):
            # print(i.isspace());
            contadorPalavras=contadorPalavras+1;
            print(contadorPalavras);
        print("Palavras digitadas: ", contadorPalavras);
    print('');
# 6. Faça um programa que solicite o nome do usuário e imprima-o na
# vertical e em formato de escada. Por exemplo, o nome “Fulano”, o
# programa deverá imprimir:
# F
# Fu
# Ful
# Fula
# Fulan
# Fulano
elif (opcao==6):
    for i in range(0, len(stringEscrita)+1):
        print(stringEscrita[:i]);
# 7. Faça um programa que permita ao usuário digitar o seu nome e em
# seguida mostre-o de trás para frente utilizando somente letras
# maiúsculas.
elif (opcao==7):
    for i in range(0, len(stringEscrita)+1):
        print(stringEscrita.upper()[::-1]);

# 9. Um anagrama é uma palavra que é feita a partir da transposição das
# letras de outra palavra ou frase. Por exemplo, “Iracema” é um
# anagrama para “America”. Escreva um programa que decida se uma
# string é um anagrama de outra string, ignorando os espaços em
# branco. O programa deve considerar maiúsculas e minúsculas como
# sendo caracteres iguais, ou seja, “a” = “A”.

# 10. Escreva um programa que solicite ao usuário a entrada de um
# número inteiro positivo ou negativo e mostre a quantidade de dígitos
# desse número.