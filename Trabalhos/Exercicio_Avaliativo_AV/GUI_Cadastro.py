import tkinter as tk
from bancoDeDados import BancoDeDados

class GUI:
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

        #Chamada para os metodos do BD
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto, width=15, bg='green', fg="white")
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

    def fCadastrarProduto(self):
        print('Chegou no cadastro!')
        pass

    def fLimparTela(self):
        print('Chegou no limpa tela!')
        pass


# Programa principal
janela = tk.Tk()
principal = GUI(janela)
janela.title('Bem Vindo a Tela de Cadastro')
imagem = tk.PhotoImage(file="./resources/cadastro_usuario.png")
imagem_label = tk.Label(janela, image=imagem)
imagem_label.pack()
janela.geometry("400x500")
janela.resizable(False, False)
janela.mainloop()
