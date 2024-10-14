import datetime


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
numero_transacoes = 0
LIMITE_TRANSACOES = 10
data_hora = ""

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if numero_transacoes < LIMITE_TRANSACOES: 

            if valor > 0:
                saldo += valor
                data_hora = datetime.datetime.now()
                extrato += f"{data_hora.strftime("%d/%m/%Y %H:%M")} - depósito: R$ {valor:.2f}\n"
                numero_transacoes += 1 

            else:
                print("Operação falhou! O valor informado é inválido.")
        else:
                print("Operação falhou! Número máximo de transações diárias excedido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        excedeu_transacoes = numero_transacoes >= LIMITE_TRANSACOES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif excedeu_transacoes:
                print("Operação falhou! Número máximo de transações diárias excedido.")

        elif valor > 0:
            saldo -= valor
            data_hora = datetime.datetime.now()
            extrato += f"{data_hora.strftime("%d/%m/%Y %H:%M")} - saque: R$ {valor:.2f}\n"
            numero_saques += 1
            numero_transacoes += 1

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
   
