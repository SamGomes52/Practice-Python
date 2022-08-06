class Veiculo:
    def __init__(self, cor):
        self._cor = cor
        self._quantidade_mudancas_cor = 0

    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor
        self._quantidade_mudancas_cor += 1

    @property
    def quantidade_mudancas_cor(self):
        return self._quantidade_mudancas_cor

    def mostra_infos_veiculo(self):
        print(f'A cor do veículo é {self.cor} e as vezes que a cor foi atualizada são: {self.quantidade_mudancas_cor}')

corsa = Veiculo('Vermelho')
corsa.cor = 'Amarelo'
corsa.cor = 'Verde'
corsa.mostra_infos_veiculo()