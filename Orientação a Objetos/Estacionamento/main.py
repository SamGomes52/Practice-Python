from estacionamento import Estacionamento

maximo_vagas_para_cada_tipo_veiculo = 5

estacionamento = Estacionamento(maximo_vagas_para_cada_tipo_veiculo)

def opcao_invalida():
    print('A opção inserida é inválida, por favor digite novamente.')

msg_menu = '''---------------------------------------------------
Bem vindo ao estacionamento!\n
Digite a opção desejada:\n
1 - Visualizar quantidade de vagas disponíveis
2 - Estacionar um carro
3 - Estacionar uma moto
4 - Remover um veículo
0 - Sair
---------------------------------------------------\n'''
opcao_escolhida = int(input(msg_menu))

while(opcao_escolhida != 0):

    if (opcao_escolhida == 1):
        estacionamento.visualizar_quantidade_vagas()
    elif (opcao_escolhida == 2):
        estacionamento.estacionar_carro()
    elif (opcao_escolhida == 3):
        estacionamento.estacionar_moto()
    elif (opcao_escolhida == 4):
        estacionamento.remover_veiculo()
    elif (opcao_escolhida != 0):
        opcao_invalida()

    opcao_escolhida = int(input(msg_menu))

