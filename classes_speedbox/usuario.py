from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .pedido import Pedido
    from .transporte import MeioTransporte

class Usuario:
    def __init__(self, id_usuario, nome, cpf):
        self.id = id_usuario
        self.nome = nome
        self.cpf = cpf
        self.logado = False

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if isinstance(novo_cpf, str) and len(novo_cpf) == 14:
            self._cpf = novo_cpf
        else:
            raise ValueError("CPF inválido. Deve conter 14 caracteres.")

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
        self.lista_usuarios: List[Usuario] = []

    def cadastrar_usuario(self, usuario: Usuario):
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
            print(f"Usuário {getattr(usuario, 'nome', 'desconhecido')} não encontrado.")
    
    def guardar_usuario(self) -> List[Usuario]:
        print(f"Administrador {self.nome} acessou a lista de usuários.")
        return self.lista_usuarios

class Cliente(Usuario):
    def __init__(self, id_usuario, nome, cpf, id_cliente, email, telefone, senha):
        super().__init__(id_usuario, nome, cpf)
        self.id_cliente = id_cliente
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.pedidos: List['Pedido'] = []

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        if isinstance(nova_senha, str) and len(nova_senha) >= 6:
            self._senha = nova_senha
        else:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
    
    def pedir_encomenda(self, pedido: 'Pedido'):
        from .pedido import Pedido
        if isinstance(pedido, Pedido):
            self.pedidos.append(pedido)
            print(f"Cliente {self.nome} fez o pedido ID: {pedido.id_pedido}.")
        else:
            print("Erro: Objeto de pedido inválido.")
        
class Entregador(Usuario):
    def __init__(self, id_usuario, nome, cpf, id_entregador, cnh, meio_transporte: Optional['MeioTransporte'], senha_entregador):
        super().__init__(id_usuario, nome, cpf)
        self.id_entregador = id_entregador
        self.cnh = cnh
        self.meio_transporte = meio_transporte
        self.senha = senha_entregador
        self.encomenda_atual: Optional['Pedido'] = None

    @property
    def cnh(self):
        return self._cnh

    @cnh.setter
    def cnh(self, nova_cnh):
        if isinstance(nova_cnh, str) and len(nova_cnh) >= 7:
            self._cnh = nova_cnh
        else:
            raise ValueError("CNH inválida. Deve conter pelo menos 7 caracteres.")

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        if isinstance(nova_senha, str) and len(nova_senha) >= 6:
            self._senha = nova_senha
        else:
            raise ValueError("A senha deve ter pelo menos 6 caracteres.")
        
    def atribuir_pedido(self, pedido: 'Pedido'):
        from .pedido import Pedido
        if isinstance(pedido, Pedido):
            self.encomenda_atual = pedido
            print(f"Entregador {self.nome} atribuído ao pedido ID: {pedido.id_pedido}.")
        else:
            print("Erro: Objeto de pedido inválido.")

    def relacionar_transporte(self):
        if self.encomenda_atual and self.meio_transporte:
            print(f"Entregador {self.nome} está utilizando {self.meio_transporte} para a entrega do pedido {self.encomenda_atual.id_pedido}.")
        else:
            print("Entregador sem encomenda ou transporte definido.")