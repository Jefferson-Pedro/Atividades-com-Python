import tkinter as tk
from tkinter import messagebox
from bancoDeDados import BancoDeDados
from PIL import Image, ImageTk

class Cadastro:

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

        #Chamada para os métodos do BD
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrar, width=15, bg='green', fg="white")
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela, width=15, bg='red', fg="white")

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

        self.btnCadastrar.place(x=80, y=430)
        self.btnLimpar.place(x=220, y=430)

    def fCadastrar(self):
        # Obtenha os dados dos campos de entrada
        nome = self.txtNome.get()
        email = self.txtEmail.get()
        telefone = self.txtTelefone.get()
        username = self.txtUsername.get()
        senha = self.txtSenha.get()

        try:
            self.objBD.inserirDados(nome, email, telefone, username, senha)
            print('Dados inseridos com sucesso!')
            messagebox.showinfo("Sucesso", "Cadastro realizado com sucesso!")
            self.fLimparTela()
        except:
            print('Ocorreu um erro, verifique os dados e tente novamente!')
            messagebox.showerror("Erro", "Ocorreu um erro ao salvar as informações.")

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
janela.title('Bem Vindo a Tela de Cadastro')

# Carregamento da imagem de fundo com Pillow
background_image = Image.open("./resources/cadastro_usuario.png")
photo = ImageTk.PhotoImage(background_image)

# Exibição da imagem em um Label
background_label = tk.Label(janela, image=photo)
background_label.place(x=0, y=-140, relwidth=1, relheight=1)

cadastro = Cadastro(janela)  # Crie a instância de Cadastro
janela.geometry("400x500")
janela.resizable(False, False)
janela.mainloop()
