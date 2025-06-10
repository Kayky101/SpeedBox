from classes_speedbox.usuario import Administrador, Cliente, Entregador
from classes_speedbox.pedido import Pedido, FormaPagamento, Encomenda
from classes_speedbox.transporte import Transportadora, SimuladorEntrega, Moto, Carro, Caminhao
from classes_speedbox.servicos import Interface


#exemplo de uso
if __name__ == "__main__":
    print("Demonstração de uso do Sistema SpeedBox")
    print("-" * 70)

    #criando usuários
    admin1 = Administrador(1, "Alice Souza", "111.111.111-11", "Coordenadora")
    cliente1 = Cliente(2, "Roberto Figueiredo", "222.222.222-22", 101, "roberto@email.com", "99999-8888", "senha123")
    entregador1 = Entregador(3, "Carlos Oliveira", "333.333.333-33", 201, "CNH9876", None, "entpass")

    #admin gerenciando usuários
    admin1.login()
    admin1.cadastrar_usuario(cliente1)
    admin1.cadastrar_usuario(entregador1)
    print(f"Usuários cadastrados: {[u.nome for u in admin1.guardar_usuario()]}")
    admin1.logout()
    print("-" * 70)

    #cliente faz login e cria pedido
    cliente1.login()
    pedido1 = Pedido(1001, cliente1, "Notebook", "Loja Tech")
    cliente1.pedir_encomenda(pedido1)
    pedido1.mostrar_detalhes()
    cliente1.logout()
    print("-" * 70)

    #pagamento
    pagamento = FormaPagamento(7001, "Cartão", "Mastercard Crédito", True)
    pagamento.validar()
    pagamento.processar_pagamento()
    pagamento.gerar_notas()
    print("-" * 70)

    #criando encomenda vinculada ao pedido
    encomenda1 = Encomenda(9001, pedido1.origem, "Rua das Rosas, 123", pagamento)
    encomenda1.pedido = pedido1
    encomenda1.atualizar_pedido("Separando no estoque")
    print("-" * 70)

    #instanciando transportadora e meios de transporte
    moto = Moto("Moto Yamaha", "Yamaha", 60, 12)
    carro = Carro("Fiat Fiorino", "Fiat", 45, 20)
    transportadora = Transportadora("12.345.678/0001-00", "Av. Logística, 700")
    transportadora.adicionar_meio_transporte(moto)
    transportadora.adicionar_meio_transporte(carro)
    transportadora.listar_meio_transporte()
    print("-" * 70)

    #atribuindo meio de transporte ao entregador
    entregador1.meio_transporte = moto
    entregador1.login()
    entregador1.atribuir_pedido(pedido1)
    entregador1.relacionar_transporte()
    entregador1.logout()
    print("-" * 70)

    #simulação de entrega
    simulador = SimuladorEntrega(moto, entregador1)
    tempo = simulador.calcular_tempo(25)
    custo = simulador.calcular_custo()
    print(f"Tempo estimado: {tempo:.2f} horas")
    print(f"Custo estimado: R$ {custo:.2f}")
    print("-" * 70)

    #atualizando status da entrega
    encomenda1.atualizar_pedido("Saiu para entrega")
    # encomenda1.atualizar_pedido("Entregue com sucesso")
    print("-" * 70)

    #interface do sistema rastreando
    interface = Interface()
    interface.calcular_frete(pedido1.origem, encomenda1.destino, 2.5)
    interface.rastrear_entrega(pedido1.id_pedido, pedido1)
