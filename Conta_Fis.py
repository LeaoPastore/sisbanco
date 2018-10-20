from SistemaBanco.Cliente import Cliente
class Conta_Fi(Cliente):
    def __init__(self, nome, cpf, end, numero, agencia, saldo):
        super(). __init__(nome, cpf, end)
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
    def __str__(self):
        return f"{super().__str__()},Número da Conta: {self.numero}, Agência: {self.agencia}, Saldo: {self.saldo}"