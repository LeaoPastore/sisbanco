class Cliente:
    def __init__(self, nome, cpf, end):
        self.nome = nome
        self.cpf = cpf
        self.end = end

    def get_nome(self):
        return self.nome

    def get_cpf(self):
        return self.cpf

    def get_idade(self):
        return self.end

    def __str__(self):
        return f'Nome: {self.nome}, CPF/CNPJ: {self.cpf}, Endereço: {self.end}'