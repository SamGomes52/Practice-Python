class Vaga:
    def __init__(self, id, tipo):
        self.__id = id
        self.__tipo = tipo
        self._livre = True
        self._placa = ''

    def __str__(self):
        return f'Vaga: {self.id} | Tipo: {self.tipo} | Livre: {self.livre} | Placa veículo estacionado: {self.placa}'

    # Getters e Setters
    @property
    def id(self):
        return self.__id

    @property
    def tipo(self):
        return self.__tipo

    @property
    def livre(self):
        return self._livre

    @property
    def placa(self):
        return self._placa

    # Ações da vaga
    def ocupar(self, placa):
        self._livre = False
        self._placa = placa

    def desocupar(self):
        self._livre = True
        self._placa = ''
