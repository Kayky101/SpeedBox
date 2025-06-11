import tkinter as tk
from tkinter import messagebox

from classes_speedbox.usuario import Administrador, Cliente, Entregador
from classes_speedbox.pedido import Pedido
from classes_speedbox.transporte import Moto 

#dados para simulação
usuarios_do_sistema = [
    Administrador(1, "Alice", "111.111.111-11", "Coordenadora"),
    Cliente(2, "Cliente1", "222.222.222-22", 101, "cliente1@email.com", "99999-8888", "cliente1-senha"),
    Entregador(3, "Carlos Entregador", "333.333.333-33", 201, "CNH1234", Moto("Pop", "Honda", 10, 80), "entregador-senha")
]
admin_global = usuarios_do_sistema[0]
admin_global.cadastrar_usuario(usuarios_do_sistema[1])
admin_global.cadastrar_usuario(usuarios_do_sistema[2])

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("SpeedBox - Sistema de Entregas")
        self.root.geometry("400x350")
        self.usuario_logado = None
        self.id_pedido_counter = 1000
        self.tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def tela_login(self):
        self.limpar_tela()
        tk.Label(self.root, text="Login no Sistema", font=("Arial", 14)).pack(pady=10)
        
        tk.Label(self.root, text="Nome:").pack()
        self.entry_nome = tk.Entry(self.root, width=30)
        self.entry_nome.pack()

        tk.Label(self.root, text="Senha:").pack()
        self.entry_senha = tk.Entry(self.root, show="*", width=30)
        self.entry_senha.pack()

        tk.Button(self.root, text="Entrar como Cliente", command=self.fazer_login_cliente, width=25).pack(pady=5)
        tk.Button(self.root, text="Entrar como Entregador", command=self.fazer_login_entregador, width=25).pack(pady=5)
        tk.Button(self.root, text="Entrar como Administrador", command=self.fazer_login_admin, width=25).pack(pady=5)

    def login_generico(self, tipo_usuario):
        nome_digitado = self.entry_nome.get().strip()
        senha_digitada = self.entry_senha.get()
        
        for usuario in usuarios_do_sistema:
            if isinstance(usuario, tipo_usuario) and usuario.nome == nome_digitado:
                if isinstance(usuario, Administrador) or (hasattr(usuario, 'senha') and usuario.senha == senha_digitada):
                    usuario.login()
                    self.usuario_logado = usuario
                    return True
        return False

    def fazer_login_cliente(self):
        if self.login_generico(Cliente): self.tela_cliente()
        else: messagebox.showerror("Erro", "Credenciais de Cliente inválidas.")

    def fazer_login_entregador(self):
        if self.login_generico(Entregador): self.tela_entregador()
        else: messagebox.showerror("Erro", "Credenciais de Entregador inválidas.")

    def fazer_login_admin(self):
        if self.login_generico(Administrador): self.tela_admin()
        else: messagebox.showerror("Erro", "Credenciais de Administrador inválidas.")

    def tela_cliente(self):
        self.limpar_tela()
        tk.Label(self.root, text=f"Bem-vindo, {self.usuario_logado.nome}!", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Produto:").pack()
        self.entry_produto = tk.Entry(self.root, width=30)
        self.entry_produto.pack()
        tk.Label(self.root, text="Origem:").pack()
        self.entry_origem = tk.Entry(self.root, width=30)
        self.entry_origem.pack()
        tk.Button(self.root, text="Fazer Pedido", command=self.fazer_pedido).pack(pady=10)
        tk.Button(self.root, text="Meus Pedidos", command=self.visualizar_pedidos_cliente).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack()

    def tela_admin(self):
        self.limpar_tela()
        tk.Label(self.root, text=f"Admin: {self.usuario_logado.nome}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Visualizar Usuários", command=self.visualizar_usuarios).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack()

    def tela_entregador(self):
        self.limpar_tela()
        tk.Label(self.root, text=f"Entregador: {self.usuario_logado.nome}", font=("Arial", 14)).pack(pady=10)
        if self.usuario_logado.encomenda_atual:
            tk.Label(self.root, text=f"Encomenda atual: Pedido ID {self.usuario_logado.encomenda_atual.id_pedido}").pack(pady=5)
        else:
            tk.Label(self.root, text="Nenhuma encomenda atribuída.").pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=10)

    def fazer_pedido(self):
        produto = self.entry_produto.get()
        origem = self.entry_origem.get()
        if produto and origem:
            self.id_pedido_counter += 1
            novo_pedido = Pedido(self.id_pedido_counter, self.usuario_logado, produto, origem)
            if isinstance(self.usuario_logado, Cliente):
                self.usuario_logado.pedir_encomenda(novo_pedido)
                messagebox.showinfo("Sucesso", f"Pedido de '{produto}' criado!")
                self.entry_produto.delete(0, 'end')
                self.entry_origem.delete(0, 'end')
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")

    def visualizar_usuarios(self):
        lista = "\n".join([f"{u.nome} ({u.__class__.__name__})" for u in usuarios_do_sistema])
        messagebox.showinfo("Usuários do Sistema", lista or "Nenhum usuário no sistema.")

    def visualizar_pedidos_cliente(self):
        if isinstance(self.usuario_logado, Cliente):
            if not self.usuario_logado.pedidos:
                messagebox.showinfo("Meus Pedidos", "Você não tem pedidos.")
                return
            lista_pedidos = "\n".join([f"ID: {p.id_pedido}, Produto: {p.produto}, Status: {p.status}" for p in self.usuario_logado.pedidos])
            messagebox.showinfo("Meus Pedidos", lista_pedidos)

    def logout(self):
        if self.usuario_logado:
            self.usuario_logado.logout()
        self.usuario_logado = None
        self.tela_login()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()