import tkinter as tk
from tkinter import messagebox
from projeto import Administrador, Cliente, Pedido

admin = Administrador(1, "Alice", "111.111.111-11", "Coordenadora")
cliente = Cliente(2, "Cliente1", "222.222.222-22", 101, "cliente1@email.com", "99999-8888", "cliente1-senha")
admin.cadastrar_usuario(cliente)



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("SpeedBox - Sistema de Entregas")
        self.root.geometry("400x300")

        self.usuario_logado = None

        self.tela_login()

    def tela_login(self):
        self.limpar_tela()

        tk.Label(self.root, text="Login no Sistema", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Nome:").pack()
        self.entry_nome = tk.Entry(self.root)
        self.entry_nome.pack()


        tk.Label(self.root, text="Senha:").pack()
        self.entry_senha = tk.Entry(self.root, show="*")
        self.entry_senha.pack()

        tk.Button(self.root, text="Entrar como Cliente", command=self.login_cliente).pack(pady=5)
        tk.Button(self.root, text="Entrar como Administrador", command=self.login_admin).pack()


    def login_cliente(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()

        if nome == cliente.nome and senha == cliente.senha:
            cliente.login()
            self.usuario_logado = cliente
            self.tela_cliente()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas para Cliente.")



    def login_admin(self):
        nome = self.entry_nome.get()
        senha = self.entry_senha.get()

        if nome == admin.nome:
            admin.login()
            self.usuario_logado = admin
            self.tela_admin()
        else:
            messagebox.showerror("Erro", "Credenciais inválidas para Administrador.")




    def tela_cliente(self):
        self.limpar_tela()
        tk.Label(self.root, text=f"Bem-vindo, {self.usuario_logado.nome}!", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Produto:").pack()
        self.entry_produto = tk.Entry(self.root)
        self.entry_produto.pack()

        tk.Label(self.root, text="Origem:").pack()
        self.entry_origem = tk.Entry(self.root)
        self.entry_origem.pack()

        tk.Button(self.root, text="Fazer Pedido", command=self.fazer_pedido).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.logout).pack()

    def tela_admin(self):
        self.limpar_tela()
        tk.Label(self.root, text=f"Admin: {self.usuario_logado.nome}", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Visualizar Usuários", command=self.visualizar_usuarios).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack()

    def fazer_pedido(self):
        produto = self.entry_produto.get()
        origem = self.entry_origem.get()
        if produto and origem:
            novo_pedido = Pedido(1001, self.usuario_logado, produto, origem)
            self.usuario_logado.pedir_encomenda(novo_pedido)
            messagebox.showinfo("Sucesso", f"Pedido de '{produto}' criado!")
        else:
            messagebox.showwarning("Aviso", "Preencha todos os campos.")

    def visualizar_usuarios(self):
        usuarios = admin.guardar_usuario()
        lista = "\n".join([u.nome for u in usuarios])
        messagebox.showinfo("Usuários Cadastrados", lista or "Nenhum usuário encontrado.")


    def logout(self):
        if self.usuario_logado:
            self.usuario_logado.logout()
        self.usuario_logado = None
        self.tela_login()

    def limpar_tela(self):
        for widget in self.root.winfo_children():
            widget.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
