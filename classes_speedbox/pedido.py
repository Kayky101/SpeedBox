from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .usuario import Cliente

class Pedido:
    def __init__(self, id_pedido: int, cliente_obj: 'Cliente', produto: str, origem: str):
        self.id_pedido = id_pedido
        self.cliente = cliente_obj 
        self.produto = produto
        self.origem = origem
        self.status = "Pendente" 
    
    def mostrar_detalhes(self):
        print(f"--- Pedido ID: {self.id_pedido} ---")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Produto: {self.produto}")
        print(f"Origem: {self.origem}")
        print(f"Status: {self.status}")
        print("-------------------------")

class FormaPagamento:
    def __init__(self, id_pagamento, tipo, descricao, ativo=True):
        self.id_pagamento = id_pagamento
        self.tipo = tipo
        self.descricao = descricao
        self.ativo = ativo

    def validar(self):
        return self.ativo

    def processar_pagamento(self):
        if self.validar():
            print(f"Pagamento {self.tipo} processado com sucesso.")
            return True
        print("Pagamento inválido.")
        return False

class Encomenda:
    def __init__(self, id_encomenda, origem, destino, forma_pagamento: FormaPagamento):
        self.id = id_encomenda
        self.origem = origem
        self.destino = destino
        self.status = "Criada"
        self.historico: List[str] = [self.status]
        self.forma_pagamento = forma_pagamento
        self.pedido: Optional[Pedido] = None

    def atualizar_pedido(self, novo_status):
        self.status = novo_status
        self.historico.append(novo_status)
        print(f"Encomenda ID {self.id} atualizada para status: {novo_status}")