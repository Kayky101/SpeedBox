class Usuario:
    def __init__(self, id_usuario, nome, cpf):
        self.id = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.logado = False 

    def login(self):
        self.logado = True
        print(f"{self.nome} realizou login.")

    def logout(self):
        self.logado = False
        print(f"{self.nome} realizou logout.")      
class Administrador(Usuario):
    def __init__(self, id_usuario, nome, cpf, cargo):
        super().__init__(id_usuario, nome, cpf)
        self.cargo = cargo
        self.lista_usuarios = []

    def cadastrar_usuario(self, usuario):
        # Lógica simples de adição, sem muita validação por enquanto
        if isinstance(usuario, Usuario):
            self.lista_usuarios.append(usuario)
            print(f"Admin {self.nome} cadastrou {usuario.nome}.")
        else:
            print("Erro: Objeto inválido.")

    def excluir_usuario(self, usuario):
        # Lógica simples de remoção
        if usuario in self.lista_usuarios:
            self.lista_usuarios.remove(usuario)
            print(f"Admin {self.nome} excluiu {usuario.nome}.")
        else:
            print(f"Usuário {usuario.nome} não encontrado.")
    
    def guardar_usuario(self):
        print(f"Administrador {self.nome} acessou a lista de usuários.")
        return self.lista_usuarios # Agora retorna a lista

class Cliente(Usuario):
    def __init__(self, id_usuario, nome, cpf, id_cliente, email, telefone, senha):
        super().__init__(id_usuario, nome, cpf)
        self.id_cliente = id_cliente
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.pedidos = []
    
    def pedir_encomenda(self, pedido):
        if isinstance(pedido, Pedido):
            self.pedidos.append(pedido)
            print(f"Cliente {self.nome} fez o pedido ID: {pedido.id_pedido}.")
        else:
            print("Erro: Objeto de pedido inválido.")
        
class Entregador(Usuario):
    def __init__(self, id_usuario, nome, cpf, id_entregador, cnh, meio_transporte, senha_entregador):
        super().__init__(id_usuario, nome, cpf)
        self.id_entregador = id_entregador
        self.cnh = cnh
        self.meio_transporte = meio_transporte
        self.senha = senha_entregador
        self.encomenda_atual = None #placeholder para o pedido
        
    def atribuir_pedido(self, pedido):
        if isinstance(pedido, Pedido):
            self.encomenda_atual = pedido
            print(f"Entregador {self.nome} atribuído ao pedido ID: {pedido.id_pedido}.")
        else:
            print("Erro: Objeto de pedido inválido para atribuição.")

    def relacionar_transporte(self):
        if self.encomenda_atual:
            print(f"Entregador {self.nome} está utilizando {self.meio_transporte} para a entrega do pedido {self.encomenda_atual.id_pedido}.")
        else:
            print(f"Entregador {self.nome} não possui encomenda atual para relacionar transporte.")

class Pedido:
    def __init__(self, id_pedido, cliente_obj, produto, origem):
        self.id_pedido = id_pedido
        self.cliente = cliente_obj # Associação com Cliente
        self.produto = produto
        self.origem = origem
        self.status = "Pendente" # Status inicial
    
    def mostrar_detalhes(self):
        print(f"--- Pedido ID: {self.id_pedido} ---")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Produto: {self.produto}")
        print(f"Origem: {self.origem}")
        print(f"Status: {self.status}")
        print("-------------------------")
        
class Interface:
    def __init__(self):
        pass

    def calcular_frete(self, origem, destino, peso_kg):
        taxa_base = 5.0
        custo_distancia = 10.0 # Fixo por enquanto
        custo_peso = peso_kg * 1.5
        frete = taxa_base + custo_distancia + custo_peso
        print(f"Frete de '{origem}' para '{destino}' ({peso_kg}kg): R$ {frete:.2f}")
        return float(frete)

    def rastrear_entrega(self, id_pedido, pedido_obj=None):
        if pedido_obj and isinstance(pedido_obj, Pedido) and pedido_obj.id_pedido == id_pedido:
            status = pedido_obj.status
            print(f"Rastreando Pedido ID {id_pedido}: Status '{status}'.")
            return f"Status: {status}"
        else:
            # Simulação básica se não tiver o objeto
            status_simulado = "Em trânsito"
            print(f"Rastreando Pedido ID {id_pedido}: Status '{status_simulado}'. (Simulado)")
            return f"Status: {status_simulado} (Simulado)"