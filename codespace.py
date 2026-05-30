# Local destinado para resolução dos exercicios. Após término, excluir e encaminhar para a pasta de resolução.

# ex005
# Crie uma classe ContaBancaria com os atributos titular e saldo.
# Adicione métodos para depositar() e sacar().

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor_do_deposito):
        self.saldo += valor_do_deposito

    def sacar(self, valor_do_saque):
        self.saldo -= valor_do_saque
    
# ---- Programa Principal ----

minha_conta = ContaBancaria("Paulo", 2000)
print(f"Saldo Inicial do {minha_conta.titular}: R$ {minha_conta.saldo}")

minha_conta.depositar(50)
print(f"Saldo Após depósito: R$ {minha_conta.saldo}")

minha_conta.sacar(10)
print(f"Saldo Após saque: R$ {minha_conta.saldo}")

