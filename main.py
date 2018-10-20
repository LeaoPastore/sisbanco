from SistemaBanco.Cliente import Cliente
from SistemaBanco.Conta import Conta

p1 = Cliente("João", 12345, "SQSW")
print(p1.get_nome())
print(p1.get_cpf())
print(p1.get_idade())
print(p1)

cf1 = Conta("José", 45685, "WWW", "0099", "001", 5.000)
print(cf1)

#p1 = Professor("Jorge","456", 45, "852456", 10.000, "Biologia")
#print(p1)
