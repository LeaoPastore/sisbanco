from SistemaBanco.Conta import Conta
class Conta_Jur(Conta):
    def __init__(self, nome, cpf, end, numero, agencia, saldo, autorizados):
        super(). __init__(nome, cpf, end)
        self.numero = numero
        self.agencia = agencia
        self.saldo = saldo
        self.autorizados = autorizados

    def __str__(self):
        return f"{super().__str__()},Número da Conta: {self.numero}, Agência: {self.agencia}, Saldo: {self.saldo} Pessoal Autorizado:{self.autorizados}"