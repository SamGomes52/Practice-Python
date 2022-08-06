class Cliente:
    def __init__(self, nome, telefone, renda_mensal):
        self.__nome = nome
        self.__telefone = telefone
        self.__renda_mensal = renda_mensal
        self.__possui_cheque_especial = False

    @property
    def nome(self):
        return self.__nome
    
    @property
    def telefone(self):
        return self.__telefone

    @property
    def renda_mensal(self):
        return self.__renda_mensal

    @property
    def possui_cheque_especial(self):
        return self.__possui_cheque_especial

    def __str__(self):
        return f'Cliente nome: {self.nome} | Telefone: {self.telefone} | Renda Mensal: {self.renda_mensal} reais\nTem cheque especial? {self.possui_cheque_especial}'

class ClienteHomem(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.__possui_cheque_especial = False

    @property
    def possui_cheque_especial(self):
        return self.__possui_cheque_especial

class ClienteMulher(Cliente):
    def __init__(self, nome, telefone, renda_mensal):
        super().__init__(nome, telefone, renda_mensal)
        self.__possui_cheque_especial = True

    @property
    def possui_cheque_especial(self):
        return self.__possui_cheque_especial

class ContaCorrente():
    def __init__(self, cliente):
        self.__cliente = cliente
        self.__saldo = 0

    @property
    def cliente(self):
        return self.__cliente

    @property
    def saldo(self):
        return self.__saldo

    def deposita(self, valor):
        self.__saldo += valor
        print(f'O valor {valor} reais foi depositado com sucesso! O novo saldo é: {self.saldo} reais\n')

    def saca(self, valor):
        if (self.cliente.possui_cheque_especial == True and -self.cliente.renda_mensal <= (self.saldo - valor)) or (valor <= self.__saldo):
            self.__saldo -= valor
            print(f'O valor {valor} reais foi debitado da conta com sucesso! O novo saldo é: {self.saldo} reais\n')
        else:
            print(f'Não foi possível sacar, pois não há saldo suficiente! O saldo é: {self.saldo} reais\n')
        
    
    def __str__(self):
        return f'Conta - cliente: {self.cliente.nome}\nSaldo: {self.saldo} reais'


cliente_1 = ClienteMulher('Juliana', '40028922', 5000)
cliente_2 = ClienteHomem('Marcelo', '3218181', 5000)
conta_1 = ContaCorrente(cliente_1)
conta_2 = ContaCorrente(cliente_2)

# A conta 1 pode ficar negativa porque é de uma mulher
conta_1.deposita(20)
conta_1.saca(30)
conta_1.saca(4990)

print(cliente_1)
print()
print(conta_1)
print()

# A conta 2 não pode ficar negativa
conta_2.deposita(20)
conta_2.saca(30)
conta_2.saca(5)

print(cliente_2)
print()
print(conta_2)