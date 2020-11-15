opcao = 0
while ( opcao != 4 ):
    print()
    print("MENU DE OPÇÕES:")
    print()
    print("<1> Fazer alguma coisa")
    print("<2> Fazer outra coisa")
    print("<3> Fazer algo diferente")
    print("<4> Sair do sistema")
    print()
    opcao = int( input("Digite a opção desejada:") )
    while ( (opcao < 1) or (opcao > 4) ):
        opcao = int( input("Opção inválida! Digite novamente!") )
        if (opcao == 1):
            print()
            print("Fazendo alguma coisa...")
            input("Digite <ENTER> para continuar...")
        elif (opcao == 2):
            print()
            print("Fazendo outra coisa...")
            input("Digite <ENTER> para continuar...")
        elif (opcao == 3):
            print()
            print("Fazendo algo diferente...")
            input("Digite <ENTER> para continuar...")
        elif (opcao == 4):
            print()
            print("Saindo do sistema...")
print()
print()
print("*** Sistema finalizado! ***")