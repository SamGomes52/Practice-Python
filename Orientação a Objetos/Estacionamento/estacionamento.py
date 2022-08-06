class Estacionamento:
    def __init__(self):
        self._vagas_de_carro = 5
        self._vagas_de_moto = 5
        self._total_vagas_livres_carro = 5
        self._total_vagas_livres_moto = 5

    def estacionar_carro(carro):
        carro.estacionar()