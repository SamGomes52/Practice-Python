class Carro:
    def __init__(self):
        self._placa = ''
        self._estacionado = False

    def __str__(self):
        return f'Placa do carro: {self.placa} | Estacionado: {self.estacionado}'
        
    # Getters e Setters
    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self, placa):
        self._placa = placa
    
    @property
    def estacionado(self):
        return self._estacionado
    
    # Ações do carro
    def estacionar(self, vaga):
        self._estacionado = True
        vaga.ocupar(self.placa)

    def sair_da_vaga(self):
        self._estacionado = False
