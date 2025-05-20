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
        if isinstance(usuario, Usuario):
            self.lista_usuarios.append(usuario)
            print(f"Admin {self.nome} cadastrou {usuario.nome}.")
        else:
            print("Erro: Objeto inválido.")

    def excluir_usuario(self, usuario):
        if not isinstance(usuario, Usuario):
            print("Erro: Tentativa de excluir objeto inválido.")
            return
        if usuario in self.lista_usuarios:
            self.lista_usuarios.remove(usuario)
            print(f"Administrador {self.nome} excluiu o usuário: {usuario.nome}.")
        else:
            print(f"Usuário {getattr(usuario, 'nome', 'desconhecido')} não encontrado para exclusão.") # Mais seguro
    
    def guardar_usuario(self):
        print(f"Administrador {self.nome} acessou a lista de usuários.")
        return self.lista_usuarios

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
        self.encomenda_atual = None 
        
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
    
    # --- Demonstração de Uso ---
if __name__ == "__main__":
    print("--- Iniciando Demonstração ---")
    # Criando usuários
    admin1 = Administrador(1, "Alice", "111.111.111-11", "Gerente")
    cliente1 = Cliente(2, "Beto", "222.222.222-22", 101, "beto@email.com", "99999-8888", "senha123")
    entregador1 = Entregador(4, "Daniel", "444.444.444-44", 201, "CNH123", "Moto", "entpass")

    # Admin em ação
    admin1.login()
    admin1.cadastrar_usuario(cliente1)
    admin1.cadastrar_usuario(entregador1)
    print(f"Usuários guardados pelo admin: {[u.nome for u in admin1.guardar_usuario()]}")
    admin1.logout()
    print("-" * 20)

    # Cliente em ação
    cliente1.login()
    pedido_beto_1 = Pedido(1001, cliente1, "Livro OOP", "Livraria Saber")
    cliente1.pedir_encomenda(pedido_beto_1)
    pedido_beto_1.mostrar_detalhes()
    cliente1.logout()
    print("-" * 20)

    # Entregador em ação
    entregador1.login()
    entregador1.atribuir_pedido(pedido_beto_1)
    # Simulando mudança de status pelo entregador
    if entregador1.encomenda_atual:
        entregador1.encomenda_atual.status = "A caminho"
    entregador1.relacionar_transporte()
    entregador1.logout()
    print("-" * 20)

    # Interface em ação
    sistema_ui = Interface()
    sistema_ui.calcular_frete("Livraria Saber", "Casa do Beto", 0.5)
    sistema_ui.rastrear_entrega(1001, pedido_beto_1)

    # Teste de rastreio sem objeto direto
    sistema_ui.rastrear_entrega(1002) # Pedido não existente ou sem objeto
    print("--- Fim da Demonstração ---")











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

    def gerar_notas(self):
        return f"Nota gerada para pagamento {self.tipo}"


class Encomenda:
    def __init__(self, id_encomenda, origem, destino, forma_pagamento):
        self.id = id_encomenda
        self.origem = origem
        self.destino = destino
        self.status = "Criada"
        self.historico = [self.status]
        self.forma_pagamento = forma_pagamento
        self.pedido = None

    def atualizar_pedido(self, novo_status):
        self.status = novo_status
        self.historico.append(novo_status)
        print(f"Encomenda ID {self.id} atualizada para status: {novo_status}")


class SimuladorEntrega:
    def __init__(self, meio_transporte, entregador):
        self.meio_transporte = meio_transporte
        self.entregador = entregador

    def calcular_tempo(self, distancia):
        tempo = distancia / self.meio_transporte.velocidade
        print(f"Tempo estimado de entrega: {tempo:.2f} horas")
        return tempo

    def calcular_custo(self):
        custo = self.meio_transporte.custo
        print(f"Custo estimado de transporte: R$ {custo:.2f}")
        return custo


class MeioTransporte:
    def __init__(self, tipo, velocidade, custo):
        self.tipo = tipo
        self.velocidade = velocidade
        self.custo = custo

    def calculo_tempo_estimado(self, distancia):
        sim = SimuladorEntrega(self, None)
        return sim.calcular_tempo(distancia)

    def calculo_custo_transporte(self):
        sim = SimuladorEntrega(self, None)
        return sim.calcular_custo()


class Carro(MeioTransporte):
    def __init__(self, modelo, marca, capacidade_max, velocidade_max):
        super().__init__("Carro", float(velocidade_max), 30.0)
        self.modelo = modelo
        self.marca = marca
        self.capacidade_max = capacidade_max
        self.velocidade_max = velocidade_max


class Moto(MeioTransporte):
    def __init__(self, modelo, marca, capacidade_max, velocidade_max):
        super().__init__("Moto", float(velocidade_max), 15.0)
        self.modelo = modelo
        self.marca = marca
        self.capacidade_max = capacidade_max
        self.velocidade_max = velocidade_max


class Caminhao(MeioTransporte):
    def __init__(self, modelo, marca, capacidade_max, velocidade_max):
        super().__init__("Caminhão", float(velocidade_max), 60.0)
        self.modelo = modelo
        self.marca = marca
        self.capacidade_max = capacidade_max
        self.velocidade_max = velocidade_max


class Transportadora:
    def __init__(self, cnpj, endereco):
        self.cnpj = cnpj
        self.endereco = endereco
        self.meios_transporte = []

    def adicionar_meio_transporte(self, meio):
        if isinstance(meio, MeioTransporte):
            self.meios_transporte.append(meio)
            print(f"Transporte {meio.tipo} adicionado à transportadora.")
        else:
            print("Transporte inválido.")

    def listar_meio_transporte(self):
        return self.meios_transporte

