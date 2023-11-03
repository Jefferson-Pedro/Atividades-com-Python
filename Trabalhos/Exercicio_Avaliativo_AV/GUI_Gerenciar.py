import tkinter as tk
from tkinter import ttk, END

import bancoDeDados
from bancoDeDados import BancoDeDados

class Gerenciar:
    def __init__(self, win, frame1, frame2):
        self.objBD = BancoDeDados()

        # Componentes Labels
        self.lblNome = tk.Label(win, text='Nome:')
        self.lblEmail = tk.Label(win, text='Email:')
        self.lblTelefone = tk.Label(win, text='Telefone:')
        self.lblUsername = tk.Label(win, text='Username:')
        self.lblSenha = tk.Label(win, text='Senha:')

        # Componentes Inputs
        self.txtNome = tk.Entry(win, width=60)
        self.txtEmail = tk.Entry(win, width=60)
        self.txtTelefone = tk.Entry(win, width=60)
        self.txtUsername = tk.Entry(win, width=60)
        self.txtSenha = tk.Entry(win, width=60)

        # Chamada para os métodos do BD
        self.btnAtualizar = tk.Button(frame2, text='Atualizar', command=self.fAtualizar, width=15, bg='green',
                                      fg="white", font= ('verdana', 8, 'bold'))
        self.btnLimpar = tk.Button(frame2, text='Limpar', command=self.fLimparTela, width=15, bg='red',
                                   fg="white", font= ('verdana', 8, 'bold'))

        # Posicionamento dos componentes (relativo ao frame2)
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

        self.btnAtualizar.place(relx=0.5, rely=0.8, relwidth=0.1, relheight=0.15)
        self.btnLimpar.place(relx=0.3, rely=0.8, relwidth=0.1, relheight=0.15)


    def fListaUsuarios(self):
        listaUsuários.delete(listaUsuários.get_children())
        lista = bancoDeDados.lerDados()

        for i in lista:
          listaUsuários.insert("", END, values=i)

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
            self.fListaUsuarios()
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
janela.title('Gerenciamento de Usuários')

#Configuração de Janela
janela.configure(background='#a9a9a9')
janela.geometry("700x500")
janela.resizable(False, False)

#Frame
frame1 = tk.Frame(janela, bd=4)
frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

#Frame
frame2 = tk.Frame(janela, bd=4)
frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

#Imagem
#imagem = tk.PhotoImage(file="./resources/editar_usuario.png")
#imagem_label = tk.Label(janela, image=imagem)
#imagem_label.pack()

#Colunas da Tabela
listaUsuários = ttk.Treeview(frame1, height= 3, columns=('col1', 'col2', 'col3', 'col4'))
listaUsuários.heading("#0", text="")
listaUsuários.heading("#1", text="Id")
listaUsuários.heading("#2", text="Nome")
listaUsuários.heading("#3", text="Email")
listaUsuários.heading("#4", text="Username")

listaUsuários.column("#0", width=0)
listaUsuários.column("#1", width=50)
listaUsuários.column("#2", width=200)
listaUsuários.column("#3", width=200)
listaUsuários.column("#4", width=150)

listaUsuários.place(relx=0.02, rely=0.05, relwidth=0.95, relheight= 0.85)

scroolLista = tk.Scrollbar(frame1, orient='vertical')
listaUsuários.configure(scroolLista.set(0.1, 0.1))
scroolLista.place(relx=0.97, rely=0.07, relwidth=0.03, relheight=0.8)

principal = Gerenciar(janela, frame1, frame2)
janela.mainloop()
