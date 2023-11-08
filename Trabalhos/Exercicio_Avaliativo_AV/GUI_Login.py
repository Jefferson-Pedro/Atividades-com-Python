import tkinter as tk
from tkinter import messagebox
from bancoDeDados import BancoDeDados


class Login:
    def __init__(self, root):
        self.root = root
        self.objBD = BancoDeDados()

        # Componentes Labels
        self.label_usuario = tk.Label(root, text="Usuário:")
        self.label_senha = tk.Label(root, text="Senha")

        # Componentes Inputs
        self.entry_usuario = tk.Entry(root, width=30)
        self.entry_senha = tk.Entry(root, show="*", width=30)

        # Botão de login
        self.botao_login = tk.Button(root, text="Login", command=self.fazer_login, width=15, bg='green', fg="white")
        self.botao_cadastro = tk.Button(root, text="Cadastre-se", command=self.abrir_cadastro, width=15, bg='blue', fg="white")

        # Posicionamento
        self.label_usuario.place(x=25, y=200)
        self.entry_usuario.place(x=80, y=200)
        self.label_senha.place(x=25, y=230)
        self.entry_senha.place(x=80, y=230)
        self.botao_login.place(x=120, y=260)
        self.botao_cadastro.place(x=120, y=290)

    def fazer_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if self.objBD.verificar_credenciais(usuario, senha):
            messagebox.showinfo("Login", "Login bem-sucedido")
            self.abrir_calculo_imc()
        else:
            messagebox.showerror("Login", "Usuário ou senha incorretos")

    def abrir_cadastro(self):
        from GUI_Cadastro import Cadastro
        cadastro = Cadastro()
        janela = tk.Toplevel(cadastro)
        janela.grab_set()


    def abrir_calculo_imc(self):
        # Coloque o código para abrir a tela de cálculo de IMC aqui
        pass

# Janela Principal
root = tk.Tk()
root.title("Tela de Login")
imagem = tk.PhotoImage(file="./resources/estacio-logo.png")
imagem_label = tk.Label(root, image=imagem)
imagem_label.pack()
root.geometry("330x330")
root.resizable(False, False)

# Inicializa a classe de login dentro da janela principal
login = Login(root)

# Inicia a aplicação
root.mainloop()