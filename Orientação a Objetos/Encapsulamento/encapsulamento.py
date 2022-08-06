class Pessoa:
    def __init__(self, nome, profissao, identidade):
        self._nome = nome
        self.profissao = profissao
        self.__identidade = identidade

    def __str__(self):
        return f'Nome: {self._nome}, Profissao: {self.profissao}, Identidade: {self.__identidade}'


pessoa1 = Pessoa('Ana', 'Programadora', '123456')

print(pessoa1)

pessoa1.profissao = 'Medica'
pessoa1._nome = 'Samara'

print(pessoa1)