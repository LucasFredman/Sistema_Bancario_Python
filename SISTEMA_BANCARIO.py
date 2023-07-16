class ContaBancaria:
    def __init__(self, numero_conta, titular_conta, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.titular_conta = titular_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("O valor de depósito deve ser maior que zero.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                print(f"Saque de R${valor:.2f} realizado.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("O valor de saque deve ser maior que zero.")

    def extrato(self):
        print("----- Extrato Bancário -----")
        print(f"Número da conta: {self.numero_conta}")
        print(f"Titular da conta: {self.titular_conta}")
        print(f"Saldo atual: R${self.saldo:.2f}")
        print("-----------------------------")


def realizar_deposito(conta, valor):
    conta.depositar(valor)


def realizar_saque(conta, valor):
    conta.sacar(valor)


def exibir_extrato(conta):
    conta.extrato()


# Teste do sistema
conta1 = ContaBancaria(1234, "João", 1000)

exibir_extrato(conta1)  # Exibe informações iniciais da conta

realizar_deposito(conta1, 500)  # Deposita R$500
realizar_saque(conta1, 200)  # Sacar R$200

exibir_extrato(conta1)  # Exibe informações atualizadas da conta
