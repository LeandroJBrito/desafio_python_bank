#Desafio python - Desenvolver um protótipo para sistema bancário, inicialmente com as opções: Depósito, saque e extrato

saldo_conta = 0
limite = 500
extrato = ""
saques_realizados = 0
limite_saques = 3

print("Bem vindo ao Banco *Selecione uma opção no menu:*")
    
menu="""
[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair
"""  

while True:
    opcao = input(menu)

    if opcao == "1":
        print("### Depósito ###")
        valor = float(input("Digite o valor a ser depositado? "))
        if valor > 0:
            saldo_conta += valor
            extrato == (f"Deposito de: {valor:.2f}")
        else:
            print("Valor inválido, favor inserir outro!")

    elif opcao == "2":
        print("### Saque ###")
        print(f"SALDO ATUAL R${saldo_conta:.2f} ")
        valor = float(input("Qual o valor que seseja Sacar? "))
        
        if valor > saldo_conta:
            print("Saldo em conta Insuficiente!")
        
        elif valor > limite:
            print(f"Excedeu limite de saque, seu limite atual é de {limite:.2f}")
        
        elif saques_realizados>=limite_saques:
            print(f"Limite máximo de {limite_saques} saques diários foi excedido, retorne amanhã! ")
        
        elif valor > 0:
            saldo_conta -= valor
            limite_saques -=1
            extrato == print(f"Saque de R$ {valor:.2f} realizado com sucesso!! Hoje você ainda pode realizar {limite_saques} saques")
        
        else:
            print("Operação inválida, favor tente novamente!!")

    elif opcao == "3":
        print("\n ############ Extrato ############")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo_conta:.2f}")
        print("####################################")    
    
    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços, volte sempre!!")

        break
        
    else:
        ("Opção inválida, favor selecionar opçao disponível!!")


