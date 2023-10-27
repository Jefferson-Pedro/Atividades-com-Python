import tkinter as tk
from tkinter import ttk
from bancoDeDados import BancoDeDados

class Gerenciar:
    def __init__(self, win):
        self.objBD = BancoDeDados()

        # Componentes Labels
        self.lblNome = tk.Label(win, text='Nome:')
        self.lblEmail = tk.Label(win, text='Email:')
        self.lblTelefone = tk.Label(win, text='Telefone:')
        self.lblUsername = tk.Label(win, text='Username:')
        self.lblSenha = tk.Label(win, text='Senha:')

        # Componentes Inputs
        self.txtNome = tk.Entry(win, width=40)
        self.txtEmail = tk.Entry(win, width=40)
        self.txtTelefone = tk.Entry(win, width=40)
        self.txtUsername = tk.Entry(win, width=40)
        self.txtSenha = tk.Entry(win, width=40)

        # Chamada para os metodos do BD
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizar(), width=15, bg='green',
                                      fg="white")
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela(), width=15, bg='red', fg="white")

        # Posicionamento dos componentes
        self.lblNome.place(x=30, y=270)
        self.txtNome.place(x=100, y=270)
        self.lblEmail.place(x=30, y=300)
        self.txtEmail.place(x=100, y=300)
        self.lblTelefone.place(x=30, y=330)
        self.txtTelefone.place(x=100, y=330)
        self.lblUsername.place(x=30, y=360)
        self.txtUsername.place(x=100, y=360)
        self.lblSenha.place(x=30, y=390)
        self.txtSenha.place(x=100, y=390)

        self.btnAtualizar.place(x=80, y=430)
        self.btnLimpar.place(x=220, y=430)

    def fAtualizar(self):
        # Obtenha os dados dos campos de entrada
        nome = self.txtNome.get()
        email = self.txtEmail.get()
        telefone = self.txtTelefone.get()
        username = self.txtUsername.get()
        senha = self.txtSenha.get()

        try:
            self.objBD.inserirDados(nome, email, telefone, username, senha)
            print('Dados inseridos com sucesso!')  # lembrar de inserir a tela de sucesso!
            self.fLimparTela()
        except:
            print('Não foi possível fazer a atualização.')
            # lembrar de inserir a tela de erro!

    def fLimparTela(self):
        try:
            self.txtNome.delete(0, tk.END)
            self.txtEmail.delete(0, tk.END)
            self.txtTelefone.delete(0, tk.END)
            self.txtUsername.delete(0, tk.END)
            self.txtSenha.delete(0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')


# Programa principal
janela = tk.Tk()
principal = Gerenciar(janela)
janela.title('Gerenciamento de Usuários')

#Imagem
imagem = tk.PhotoImage(file="./resources/editar_usuario.png")
imagem_label = tk.Label(janela, image=imagem)
imagem_label.pack()

#Colunas da Tabela
tree = ttk.Treeview(janela, columns=('coluna1', 'coluna2'), show='headings', selectmode='browse')

tree.column('coluna1', width=100)
tree.heading('#1', text='Nome')

tree.column('coluna2', width=100)
tree.heading('#2', text='Email')


janela.geometry("400x600")
janela.resizable(False, False)
janela.mainloop()
