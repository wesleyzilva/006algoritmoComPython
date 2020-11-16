opcaoSubMenuSubMenu = 0
while ( opcaoSubMenuSubMenu != 11 ):
    print()
    print(">>>>>SUBMENU DE OPÇÕES:")
    print()
    print("<1> Listar todos")
    print("<2> Listar específico")
    print("<3> Incluir")
    print("<4> Alterar")
    print("<5> Excluir")
    print("<11> Voltar ao MENU DE OPÇÕES")
    print()
    opcaoSubMenu = int( input("Digite a opção desejada:") )
    while ( (opcaoSubMenu < 1) or (opcaoSubMenu > 11) ):
        opcaoSubMenu = int( input("Opção inválida! Digite novamente!") )
    if (opcaoSubMenu == 1):
        print()
        print("---------LISTANDO")
        input("Digite <ENTER> para continuar...")
    elif (opcaoSubMenu == 2):
        print()
        print("---------LISTANDO ESPECÌFICO")
        input("Digite <ENTER> para continuar...")
    elif (opcaoSubMenu == 3):
        print()
        print("---------INCLUINDO")
        input("Digite <ENTER> para continuar...")
    elif (opcaoSubMenu == 4):
        print()
        print("---------ALTERANDO")
        input("Digite <ENTER> para continuar...")
    elif (opcaoSubMenu == 5):
        print()
        print("---------EXCLUINDO")
        input("Digite <ENTER> para continuar...")
    elif (opcaoSubMenu == 11):
        print()
        print("Saindo do submenu...")   
print()
print()
print("*** Sistema finalizado! ***")