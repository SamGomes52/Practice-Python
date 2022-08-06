from carro import Carro
from vaga import Vaga

corsa = Carro()
vaga_carro1 = Vaga('C01', 'Carro')
vaga_moto1 = Vaga('M01', 'Moto')


corsa.placa = 'ABC123'
print(corsa)
corsa.estacionar(vaga_carro1)
print(corsa)
corsa.sair_da_vaga()
print(corsa)

print(vaga_carro1)
print(vaga_moto1)


