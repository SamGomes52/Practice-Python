class Moto:
    def __init__(self):
        self.__placa = ''
        self.__estacionado = False

    def __str__(self):
        return f'Placa do moto: {self.placa} | Estacionado: {self.estacionado}'
        
    # Getters e Setters
    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa
    
    @property
    def estacionado(self):
        return self.__estacionado
    
    # Ações da moto
    def estacionar(self, vaga):
        self.__estacionado = True
        vaga.ocupar(self.placa)

    def sair_da_vaga(self, vaga):
        self.__estacionado = False
        vaga.desocupar()
