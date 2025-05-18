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

class Cliente(Usuario):
    def __init__(self, id_usuario, nome, cpf, id_cliente, email, telefone, senha):
        super().__init__(id_usuario, nome, cpf)
        self.id_cliente = id_cliente
        self.email = email
        self.telefone = telefone
        self.senha = senha
        self.pedidos = []
    
    def pedir_encomenda(self, pedido):
        pass
        print(f"Cliente {self.nome} pediu encomenda (a ser detalhado).")