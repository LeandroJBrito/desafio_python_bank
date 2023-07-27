#Desafio python V2 - Desenvolver melhorias no sistema criado na Versão 1

import textwrap

def menu():
    menu = """\n
######## - Bem vindo ao Banco *Selecione uma opção no menu: ########
[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Nova Conta
[5] - Listar Contas
[6] - Novo Usuário 
[0] - Sair
Opção: ==> 
"""  
    return input(textwrap.dedent(menu))


def depositar (saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato == (f"Deposito de: {valor:.2f}")
    else:
        print("Valor inválido, favor inserir outro!")

    return saldo, extrato    


def sacar(*,saldo,valor,extrato, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo em conta Insuficiente!")
        
    elif valor > limite_saques:
        print(f"Excedeu limite de saque, seu limite atual é de {limite_saques:.2f}")
        
    elif numero_saques>=limite_saques:
        print(f"Limite máximo de {limite_saques} saques diários foi excedido, retorne amanhã! ")
        
    elif valor > 0:
        saldo -= valor
        limite_saques -=1
        extrato == print(f"Saque de R$ {valor:.2f} realizado com sucesso!! Hoje você ainda pode realizar {limite_saques} saques")
        
    else:
        print("Operação inválida, favor tente novamente!!")
    
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n ############ Extrato ############")
    print("Não foram realizadas movimentações.") if not extrato else extrato
    print(f"\n Saldo: R$ {saldo:.2f}")
    print("####################################")    
 
def criar_usuario(usuarios):
    cpf= input("informe o numero do cpf (somente numeros): ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuarios:
        print("Já existe usuário com esse CPF: ")
        return
    
    nome =  input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimemnto (dd-mm-aaaa): ") 
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereço":endereco})
    
    print("Usuário criado com sucesso")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"]== cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o cpf do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!!")
        return{"Agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n Usuario não encontrado, fluxo de ciração de conta encerrado!!")


def listar_contas(contas):
    for conta in contas:
        linha =f"""\
        Agência: {conta["agencia"]}
        C/C: {conta["numero_conta"]}
        Titular: {conta["usuario"]["nome"]}
        """
        print("=" , 100)
        print(textwrap.dedent(linha))



def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    AGENCIA = "0001"
    usuarios =[]
    contas=[]
    usuario = []

while True:
    opcao = menu()

    if opcao == "1":
        print("### Depósito ###")
        valor = float(input("Digite o valor a ser depositado? "))
        saldo, extrato = depositar(saldo,valor,extrato)

    elif opcao == "2":
        print("### Saque ###")
        print(f"SALDO ATUAL R${saldo:.2f} ")
        valor = float(input("Qual o valor que seseja Sacar? "))
        
        saldo, extrato = sacar(
            saldo =saldo,
            valor=valor,
            extrato=extrato,
            limite= limite,
            numero_saques=numero_saques,
            limite_saques=limite_saques,
        )
        
    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)
    
    elif opcao=="4":
        criar_usuario(usuarios)

    elif opcao=="5":
        listar_contas(conta)
        
    elif opcao=="6":  
        numero_conta = len(conta)+1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            conta.append(conta)


    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços, volte sempre!!")

        break
        
    else:
             print("Opção inválida, favor selecionar opçao disponível!!")

main()