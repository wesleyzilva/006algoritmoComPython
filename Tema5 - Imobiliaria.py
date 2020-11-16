# Tema 5: Imobiliária
# Uma aplicação para uma Imobiliária precisa armazenar 
# informações sobre os seus clientes,
# imóveis e sobre os aluguéis (ou seja, quando um cliente aluga um imóvel). 
# Os dados a serem armazenados sobre cada uma dessas entidades
# são apresentados a seguir:

# Cliente = (CPF, Nome, Data de Nascimento, Salário, E-mail, Telefone)
# Imóvel = (CÓDIGO, Descrição, Endereço, Tipo (comercial, residencial), Valor aluguel)
# Aluguel = (CPF CLIENTE, CÓDIGO IMÓVEL, DATA ENTRADA, Nomes Fiadores, Valor Mensal)

# Atenção: os atributos (dados) EM MAÍUSCULO NÃO podem se repetir no cadastro.
# Utilizando os conhecimentos aprendidos sobre Dicionários, Listas e Funções, desenvolva um
# programa em Python que apresente o seguinte menu de opções para o usuário e implemente cada
# operação usando função. Escolha a estrutura de dados mais apropriada para armazenar os dados
# de cada entidade descrita anteriormente.
# Menu de Opções:
# 1 Submenu de Clientes
# 2 Submenu de Imóveis
# 3 Submenu de Aluguéis
# 4 Submenu Relatórios
# 5 Sair
opcao = 0
while ( opcao != 10 ):
    print()
    print("############ MENU PRINCIPAL:")
    print()
    print("< 1> Clientes")
    print("< 2> Imóveis")
    print("< 3> Aluguéis")
    print("< 4> Relatórios")
    print("<10> Sair do sistema")
    print()
    opcao = int( input("Digite a opção desejada:") )
    while ( (opcao < 1) or (opcao > 10) ):
        opcao = int( input("Opção inválida! Digite novamente!") )
    if (opcao == 1):
        print()
        print("############### Clientes ###############")
        input("Digite <ENTER> para continuar...")
    elif (opcao == 2):
        print()
        print("############### Imóveis ###############")
        input("Digite <ENTER> para continuar...")
    elif (opcao == 3):
        print()
        print("############### Alugueis ###############")
        input("Digite <ENTER> para continuar...")
    elif (opcao == 4):
        print()
        print("############### Relatórios ###############")
        input("Digite <ENTER> para continuar...")
    elif (opcao == 10):
        print()
        print("Saindo do sistema...")   
print()
print()
print("*** Sistema finalizado! ***")

# Cada Submenu deverá oferecer as opções: Listar todos, Listar um elemento específico do
# conjunto, Incluir (sem repetição), Alterar e Excluir (após confirmação dos dados) um elemento do
# conjunto. Observe que os atributos que estão no plural indicam que deverá ser possível incluir
# vários itens daquele mesmo atributo. Por exemplo, o atributo “nomes fiadores” indica que um
# imóvel alugado pode ter vários fiadores associados (a quantidade é indefinida). Portanto, deve-se
# utilizar uma estrutura que seja adequada para armazenar os dados.
# O Submenu Relatórios deverá ter uma opção para cada um dos relatórios solicitados a seguir.
# • Mostrar todos os dados de todos os clientes que tenham salário entre X e Y, informados
# pelo usuário;
# • Mostrar todos os dados de todos os imóveis que possuem de um tipo específico fornecido
# pelo usuário;
# • Mostrar o CPF do cliente, nome do cliente, código do imóvel, descrição e os demais dados
# dos imóveis com data de entrada entre X e Y, onde ambas as datas devem ser fornecidas
# pelo usuário.
# Obs: Não utilize variáveis globais. Use parâmetros para fazer a transferência de valores entre as
# funções. Dê nomes significativos para variáveis e funções.