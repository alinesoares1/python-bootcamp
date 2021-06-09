from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Aline', 24)
cliente2 = Cliente('Luiz', 50)
cliente3 = Cliente('Marina', 18)

conta1 = ContaPoupanca(1111, 254192, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_conta(conta1)

banco.inserir_clientes(cliente2)
banco.inserir_conta(conta2)

banco.inserir_clientes(cliente3)
banco.inserir_conta(conta3)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(50)
    cliente1.conta.sacar(20)
else:
    print("Cliente não autenticado")

print('####################################')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print("Cliente não autenticado")

print('####################################')

if banco.autenticar(cliente3):
    cliente3.conta.depositar(100)
    cliente3.conta.sacar(35)
else:
    print("Cliente não autenticado")

