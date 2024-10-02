# Desafio - Criando um sistema bancário

# Saque
#   * Permite 3 saques diários;
#   * Limite de 500 reais por saque;
#   * Se não tiver saldo suficiente, exibir mensagem informando a falta de dinheiro;
#   * Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato;
# Depósito
#   * Depositar valores positivos;
#   * v1 trabalha apenas com 1 usuário;
#   * Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato;
# Extrato
#   * Listar todos os depósitos e saques;
#   * No final da listagem exibir o saldo atual da conta;
#   * Valores no formato R$xxx.xx (R$1500.45);    

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
   
