from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .pedido import Pedido

class Interface:
    def __init__(self):
        pass

    def calcular_frete(self, origem, destino, peso_kg):
        taxa_base = 5.0
        custo_distancia = 10.0 
        custo_peso = peso_kg * 1.5
        frete = taxa_base + custo_distancia + custo_peso
        print(f"Frete de '{origem}' para '{destino}' ({peso_kg}kg): R$ {frete:.2f}")
        return float(frete)

    def rastrear_entrega(self, id_pedido, pedido_obj: 'Pedido' = None):
        from .pedido import Pedido
        if pedido_obj and isinstance(pedido_obj, Pedido) and pedido_obj.id_pedido == id_pedido:
            status = pedido_obj.status
            print(f"Rastreando Pedido ID {id_pedido}: Status '{status}'.")
            return f"Status: {status}"
        else:
            status_simulado = "Em trânsito"
            print(f"Rastreando Pedido ID {id_pedido}: Status '{status_simulado}'. (Simulado)")
            return f"Status: {status_simulado} (Simulado)"