from carro import Carro
from vaga import Vaga
from moto import Moto


class Estacionamento:
    def __init__(self, maximo_vagas_para_cada_tipo_veiculo):
        self.__maximo_vagas_para_cada_tipo_veiculo = maximo_vagas_para_cada_tipo_veiculo
        self.__vagas_de_carro = maximo_vagas_para_cada_tipo_veiculo
        self.__vagas_de_moto = maximo_vagas_para_cada_tipo_veiculo
        self.__veiculos_estacionados = []
        self.__vagas = self.cria_vagas()

    @property
    def vagas_de_carro(self):
        return self.__vagas_de_carro

    @property
    def vagas_de_moto(self):
        return self.__vagas_de_moto
    
    @property
    def maximo_vagas_para_cada_tipo_veiculo(self):
        return self.__maximo_vagas_para_cada_tipo_veiculo

    @property
    def vagas(self):
        return self.__vagas

    @property
    def veiculos_estacionados(self):
        return self.__veiculos_estacionados

    def cria_vagas(self):
        vagas = []

        for vaga in range(self.maximo_vagas_para_cada_tipo_veiculo):
            vagas.append(Vaga(f'C{vaga}', 'Carro'))
            vagas.append(Vaga(f'M{vaga}', 'Moto'))

        return vagas

    def visualizar_quantidade_vagas(self):
        print(f'Existem {self.vagas_de_carro} vagas para carro e {self.vagas_de_moto} vagas para moto disponíveis.')


    def estacionar_carro(self):
        estacionado = False

        for vaga in self.vagas:
            if vaga.livre and vaga.tipo == 'Carro':
                self.veiculos_estacionados.append(Carro())

                placa_carro = input('Insira a placa do carro: ')
                self.veiculos_estacionados[-1].placa = placa_carro

                self.veiculos_estacionados[-1].estacionar(vaga)
                self.__vagas_de_carro -= 1
                estacionado = True
                print(f'Carro estacionado na vaga: {vaga}')
                break

        if not estacionado:
            print('Não há vagas disponíveis, volte mais tarde!')

    def estacionar_moto(self):
        estacionado = False

        for vaga in self.vagas:
            if vaga.livre and vaga.tipo == 'Moto':
                self.veiculos_estacionados.append(Moto())

                placa_moto = input('Insira a placa da moto: ')
                self.veiculos_estacionados[-1].placa = placa_moto

                self.veiculos_estacionados[-1].estacionar(vaga)
                self.__vagas_de_moto -= 1
                estacionado = True
                print(f'Moto estacionada na vaga: {vaga}')
                break

        if not estacionado:
            for vaga in self.vagas:
                if vaga.livre and vaga.tipo == 'Carro':
                    self.veiculos_estacionados.append(Moto())

                    placa_moto = input('Insira a placa da moto: ')
                    self.veiculos_estacionados[-1].placa = placa_moto

                    self.veiculos_estacionados[-1].estacionar(vaga)
                    self.__vagas_de_moto -= 1
                    estacionado = True
                    print(f'Moto estacionada na vaga: {vaga}')
                    break
        
        if not estacionado:
            print('Não há vagas disponíveis, volte mais tarde!')

    def remover_veiculo(self):
        placa = input('Insira a placa do veículo: ')

        removido = False

        for vaga in self.vagas:
            if vaga.placa == placa:
                for veiculo in self.veiculos_estacionados:
                    if veiculo.placa == placa:
                        veiculo.sair_da_vaga(vaga)

                        if vaga.tipo == 'Moto':
                            self.__vagas_de_moto += 1
                        else:
                            self.__vagas_de_carro += 1

                        removido = True
                        print(f'O veiculo com a placa: {placa} foi removido.')
                        break

        if not removido:
            print('Veiculo não encontrado no estacionamento.')

