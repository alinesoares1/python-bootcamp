from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def detalhes(self):
        return print(f"Agência: {self.agencia}\nNúmero da conta: {self.conta}\nSaldo: {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes()

    @abstractmethod
    def sacar(self, valor): pass

class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.detalhes()
        else:
            print("Saldo insuficiente.")
            return

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente.")
            return
        self.saldo -= valor
        self.detalhes()

