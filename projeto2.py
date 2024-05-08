def inserir_funcionario(lista_funcionarios): 
    funcionario = {} 
    nova_matricula = str(input("\nDigite a matrícula do funcionário: ")) 
    matricula_valida = verificar_matricula(lista_funcionarios, nova_matricula) 
 
    while not matricula_valida: 
        print("Matrícula já existe! Tente novamente. ") 
        nova_matricula = str(input("Digite a matrícula do funcionário: ")) 
        matricula_valida = verificar_matricula(lista_funcionarios, nova_matricula) 

    nome = str(input("Digite o nome do funcionário: ")) 
    codigo_funcao = str(input("Digite o código da função (101 - Vendedor) (102 - Administrativo): ")) 

    while codigo_funcao != "101" and codigo_funcao != "102": 
        print("Código inválido! Tente novamente. ") 
        codigo_funcao = str(input("Digite o código da função (101 - Vendedor) (102 - Administrativo): ")) 

    if codigo_funcao == "101": 
        salario_bruto = 1500 
        numero_vendas = int(input("Digite o número de vendas: ")) 
        salario_bruto = salario_bruto + (salario_bruto * 0.09) * numero_vendas 

    else: 
        salario_bruto = float(input("Digite o salário bruto: ")) 
        while salario_bruto < 2150 or salario_bruto > 6950: 
            print("Salário inválido, o salário deve estar entre R$2150,00 e R$6950,00! ") 
            salario_bruto = float(input("Digite o salário bruto: ")) 

    numeros_faltas = int(input("Digite a quantidade de faltas: "))

    while numeros_faltas > 30:
        print("Valor inválido, o limite de faltas no mês é de 30 dias. Tente novamente! ")
        numeros_faltas = int(input("Digite a quantidade de faltas: "))
 

    funcionario["Matricula"] = nova_matricula 
    funcionario["Nome"] = nome 
    funcionario["Codigo"] = codigo_funcao 
    funcionario["Faltas"] = numeros_faltas
    funcionario["Desconto faltas"] = salario_bruto - calculo_faltas(salario_bruto, numeros_faltas) 
    salario_bruto = calculo_faltas(salario_bruto, numeros_faltas) 
    funcionario["Salario bruto"] = salario_bruto 
    salario_liquido = salario_bruto - calculo_imposto(salario_bruto) 
    funcionario["Salario liquido"] = salario_liquido
    
    if salario_bruto > 0:
        funcionario["Imposto"] = 100 * (salario_bruto - salario_liquido) / salario_bruto
    else:
        funcionario["Imposto"] = 0

    if codigo_funcao == "101": 
        funcionario["Quantidade vendas"] = numero_vendas 

    print("\nFuncionário cadastrado com sucesso!")
    return lista_funcionarios.append(funcionario) 


def remover_funcionario(lista_funcionarios): 
    matricula_deletar = str(input("\nDigite a matrícula do funcionário que deseja remover: "))
    matricula_valida = verificar_matricula(lista_funcionarios, matricula_deletar)

    while matricula_valida:
        print("Matrícula não existe no sistema. Tente novamente! ")
        matricula_deletar = str(input("Digite a matrícula do funcionário que deseja remover: "))
        matricula_valida = verificar_matricula(lista_funcionarios, matricula_deletar)
    
    confirmacao = str(input("Tem certeza que deseja excluir o funcionário? (S/N): "))

    while confirmacao != "S" and confirmacao != "N":
        print("Resposta inválida. Tente novamente!")
        confirmacao = str(input("Tem certeza que deseja excluir o funcionário? (S/N): "))
    
    if confirmacao == "N":
        return
    else:
        for funcionario in lista_funcionarios: 
            if funcionario["Matricula"] == matricula_deletar:
                print("\nFuncionário removido com sucesso!")
                return lista_funcionarios.remove(funcionario)


def folha_pagamento(lista_funcionarios): 
    matricula = str(input("\nDigite a matrícula do funcionário que deseja ver a folha de pagamento: "))
    matricula_valida = verificar_matricula(lista_funcionarios, matricula)

    while matricula_valida:
        print("Matrícula não existe no sistema. Tente novamente! ")
        matricula = str(input("Digite a matrícula do funcionário que deseja ver a folha de pagamento: "))
        matricula_valida = verificar_matricula(lista_funcionarios, matricula)   

    for funcionario in lista_funcionarios: 
        if funcionario["Matricula"] == matricula:
            print("="*50)
            print("Folha de Pagamento".center(50))
            print("="*50)
            print(("-"*40).center(50))
            for key, value in funcionario.items():
                if key == "Salario bruto" or key == "Salario liquido" or key == "Desconto faltas":
                    print(f"{key}: R${value:.2f}".center(50))
                elif key == "Imposto":
                    print(f"{key}: {value:.2f}%".center(50))
                else:
                    print(f"{key}: {value}".center(50))
                print(("-"*40).center(50))
            print("="*50)


def relatorio(lista_funcionarios):
    print("="*50)
    print("Relatório Geral".center(50))
    print("="*50) 
    for funcionario in lista_funcionarios:
        print(("-"*40).center(50))
        for key, value in funcionario.items():
            if key == "Faltas" or key == "Quantidade vendas" or key == "Imposto" or key == "Desconto faltas":
                pass
            elif key == "Salario bruto" or key == "Salario liquido":
                print(f"{key}: R${value:.2f}".center(50))
                print(("-"*40).center(50))
            else:
                print(f"{key}: {value}".center(50))
                print(("-"*40).center(50))
        print("="*50) 


def maior_salario_liquido(lista_funcionarios):
    funcionario_maior_salario = lista_funcionarios[0]
    maior_salario = funcionario_maior_salario["Salario liquido"]

    for funcionario in lista_funcionarios:
        if funcionario["Salario liquido"] > maior_salario:
            maior_salario = funcionario["Salario liquido"]
            funcionario_maior_salario = funcionario

    print("="*50)
    print("Funcionário com maior salário líquido".center(50))
    print("="*50)
    print(("-"*40).center(50))
    for key, value in funcionario_maior_salario.items():
        if key == "Faltas" or key == "Quantidade vendas" or key == "Desconto faltas":
            pass
        elif key == "Salario bruto" or key == "Salario liquido":
            print(f"{key}: R${value:.2f}".center(50))
            print(("-"*40).center(50))
        elif key == "Imposto":
            print(f"{key}: {value:.2f}%".center(50))
            print(("-"*40).center(50))
        else:
            print(f"{key}: {value}".center(50))
            print(("-"*40).center(50))
    print("="*50)


def maior_numero_falta(lista_funcionarios): 
    funcionario_maior_faltas = lista_funcionarios[0]
    maior_falta = funcionario_maior_faltas["Faltas"]

    for funcionario in lista_funcionarios:
        if funcionario["Faltas"] > maior_falta:
            maior_falta = funcionario["Faltas"]
            funcionario_maior_faltas = funcionario

    print("="*50)
    print("Funcionário com maior número de faltas".center(50))
    print("="*50)
    print(("-"*40).center(50))
    for key, value in funcionario_maior_faltas.items():
        if key == "Quantidade vendas":
            pass
        elif key == "Salario bruto" or key == "Salario liquido" or key == "Desconto faltas":
            print(f"{key}: R${value:.2f}".center(50))
            print(("-"*40).center(50))
        elif key == "Imposto":
            print(f"{key}: {value:.2f}%".center(50))
            print(("-"*40).center(50))
        else:
            print(f"{key}: {value}".center(50))
            print(("-"*40).center(50))
    print("="*50)


def verificar_matricula(lista_funcionarios, nova_matricula): 
    for funcionario in lista_funcionarios: 
        if funcionario["Matricula"] == nova_matricula: 
            return False 
    return True 


def calculo_imposto(salario_bruto): 
    faixa1 = 2259.2
    faixa2 = 2828.65
    faixa3 = 3751.05
    faixa4 = 4664.68

    porcentagem_faixa1 = 0.075
    porcentagem_faixa2 = 0.15
    porcentagem_faixa3 = 0.225
    porcentagem_faixa4 = 0.275

    if salario_bruto <= faixa1:
        imposto = 0

    elif salario_bruto <= faixa2: 
        imposto = (salario_bruto - faixa1) * porcentagem_faixa1

    elif salario_bruto <= faixa3: 
        imposto = (faixa2-faixa1) * porcentagem_faixa1 
        imposto += (salario_bruto - faixa2) * porcentagem_faixa2

    elif salario_bruto <= faixa4: 
        imposto = ((faixa2-faixa1) * porcentagem_faixa1) + ((faixa3-faixa2) * porcentagem_faixa2)
        imposto += (salario_bruto - faixa3) * porcentagem_faixa3

    else:  
        imposto = ((faixa2-faixa1) * porcentagem_faixa1) + ((faixa3-faixa2) * porcentagem_faixa2)  + ((faixa4 - faixa3) * porcentagem_faixa3)
        imposto += (salario_bruto - faixa4) * porcentagem_faixa4 

    return imposto
 

def calculo_faltas(salario_bruto, numeros_faltas): 
    salario = salario_bruto - (salario_bruto/30) * numeros_faltas 
    return salario 


def menu():
    menu = """ 
    =====================================================
                M a r k e t i n g  é  T u d o
    =====================================================

                       Seja bem-vindo 
           Sistema de gerenciamento de funcionários

    =====================================================

                     Escolha uma opção:

    [1] Inserir Funcionários 
    [2] Remover Funcionários
    [3] Ver a folha de pagamento de um funcionário
    [4] Relatório Geral
    [5] Funcionário com maior salário líquido
    [6] Funcionário com maior número de faltas
    [7] Sair do sistema
    
    =====================================================

    ==> """

    return menu
 

def verificar_lista_possui_elementos(lista_funcionarios):
    if len(lista_funcionarios) > 0:
        return True
    else:
        return False

def main(): 
    funcionarios = []
    escolha = str(input(menu()))

    while escolha != "7":
        if escolha == "1":
            inserir_funcionario(funcionarios)

        elif escolha == "2":
            if verificar_lista_possui_elementos(funcionarios):
                remover_funcionario(funcionarios)
            else:
                print("\nA lista de funcionários está vazia, insira algum funcionário antes de utilizar essa opção!")

        elif escolha == "3":
            if verificar_lista_possui_elementos(funcionarios):
                folha_pagamento(funcionarios)
            else:
                print("\nA lista de funcionários está vazia, insira algum funcionário antes de utilizar essa opção!")

        elif escolha == "4":
            relatorio(funcionarios)

        elif escolha == "5":
            if verificar_lista_possui_elementos(funcionarios):
                maior_salario_liquido(funcionarios)
            else:
                print("\nA lista de funcionários está vazia, insira algum funcionário antes de utilizar essa opção!")

        elif escolha == "6":
            if verificar_lista_possui_elementos(funcionarios):
                maior_numero_falta(funcionarios)
            else:
                print("\nA lista de funcionários está vazia, insira algum funcionário antes de utilizar essa opção!")

        else:
            print("Escolha inválida! Tente novamente.")

        input("\nAperte ENTER para continuar...")
        escolha = str(input(menu()))
    
    print("\nEncerrando o sistema... \nSistema encerrado!")


main() 