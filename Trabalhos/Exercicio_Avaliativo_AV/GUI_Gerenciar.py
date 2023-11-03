import tkinter as tk
from tkinter import ttk, END

import bancoDeDados
from bancoDeDados import BancoDeDados

class Gerenciar:
    #objBD = BancoDeDados()
    def __init__(self, win, frame1, frame2):
        self.txtId = None
        self.objBD = BancoDeDados()

        # Componentes Labels
        self.lblNome = tk.Label(win, text='Nome:')
        self.lblEmail = tk.Label(win, text='Email:')
        self.lblTelefone = tk.Label(win, text='Telefone:')
        self.lblUsername = tk.Label(win, text='Username:')
        self.lblSenha = tk.Label(win, text='Senha:')

        # Componentes Inputs
        self.txtId = tk.Entry(win)
        self.txtNome = tk.Entry(win, width=60)
        self.txtEmail = tk.Entry(win, width=60)
        self.txtTelefone = tk.Entry(win, width=60)
        self.txtUsername = tk.Entry(win, width=60)
        self.txtSenha = tk.Entry(win, width=60)

        # Chamada para os métodos do BD
        self.btnAtualizar = tk.Button(frame2, text='Atualizar', command=self.fAtualizar, width=15, bg='green',
                                      fg="white", font= ('verdana', 8, 'bold'))
        self.btnLimpar = tk.Button(frame2, text='Limpar', command=self.fLimparTela, width=15, bg='blue',
                                   fg="white", font= ('verdana', 8, 'bold'))
        self.btnExcluir = tk.Button(frame2, text='Excluir', command=self.fExcluiUsuario, width=15, bg='red',
                                   fg="white", font=('verdana', 8, 'bold'))

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

        self.btnAtualizar.place(relx=0.6, rely=0.8, relwidth=0.1, relheight=0.15)
        self.btnExcluir.place(relx=0.4, rely=0.8, relwidth=0.1, relheight=0.15)
        self.btnLimpar.place(relx=0.2, rely=0.8, relwidth=0.1, relheight=0.15)


    def fListaUsuarios(self):
        children = listaUsuários.get_children()
        if children:  # Verifica se há itens na árvore para evitar o erro "Cannot delete root item"
            for child in children:
                listaUsuários.delete(child)
        lista = self.objBD.lerDados()
        for i in lista:
            listaUsuários.insert("", END, values=i)

    def fExcluiUsuario(self):
        # Obtem o ID do usuário do campo de entrada
        id = self.txtId.get()

        # Verifica se o ID não está vazio antes de excluir
        if id:
            nome = self.txtNome.get()
            email = self.txtEmail.get()
            telefone = self.txtTelefone.get()
            username = self.txtUsername.get()
            senha = self.txtSenha.get()

            self.objBD.deletarDados(id)

            self.fLimparTela()

            self.fListaUsuarios()
        else:
            print("Nenhum usuário selecionado para exclusão.")

    def fAtualizar(self):
        # Obtenha os dados dos campos de entrada
        nome = self.txtNome.get()
        email = self.txtEmail.get()
        telefone = self.txtTelefone.get()
        username = self.txtUsername.get()
        senha = self.txtSenha.get()

        try:
            self.objBD.atualizarDados(nome, email, telefone, username,senha)
            print('Dados atualizados com sucesso!')  # lembrar de inserir a tela de sucesso!
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

    def fSelecionaUsuario(self, event=None):
        listaUsuários.selection()
        for n in listaUsuários.selection():
            col1, col2,col3,col4, col5 = listaUsuários.item(n, 'values')
            self.txtId.insert(END, col1)
            self.txtNome.insert(END, col2)
            self.txtEmail.insert(END, col3)
            self.txtUsername.insert(END, col4)
            self.txtTelefone.insert(END, col5)
           # self.txtSenha.insert(END, col6)
        print('Usuário selecionado: ',self.txtId, self.txtNome,  self.txtEmail, self.txtUsername, self.txtTelefone)

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

# Colunas da Tabela
listaUsuários = ttk.Treeview(frame1, height=3, columns=('col1', 'col2', 'col3', 'col4'))
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

listaUsuários.place(relx=0.02, rely=0.05, relwidth=0.95, relheight=0.85)

scroolLista = tk.Scrollbar(frame1, orient='vertical')
listaUsuários.configure(yscrollcommand=scroolLista.set)
scroolLista.place(relx=0.97, rely=0.07, relwidth=0.03, relheight=0.8)
listaUsuários.bind("<Double-1>", lambda event: principal.fSelecionaUsuario(event))


principal = Gerenciar(janela, frame1, frame2)
principal.fListaUsuarios()  # Chamando a função para preencher a tabela
janela.mainloop()
