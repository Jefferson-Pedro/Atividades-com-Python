import tkinter as tk
from tkinter import messagebox

from bancoDeDados import BancoDeDados

class IMC:
    def __init__(self, root):
        self.root = root
        self.objBD = BancoDeDados()

        # Componentes Labels
        self.label_peso = tk.Label(root, text="Peso (kg):")
        self.label_altura = tk.Label(root, text="Altura (m):")
        #self.label_genero = tk.Label(root, text="Gênero:")
        self.label_idade = tk.Label(root, text="Idade:")

        # Radio Buttons para gênero
        self.var_genero = tk.StringVar(value="Feminino")  # Inicializa com "Feminino"
        self.radio_feminino = tk.Radiobutton(root, text="Feminino", variable=self.var_genero, value="Feminino")
        self.radio_masculino = tk.Radiobutton(root, text="Masculino", variable=self.var_genero, value="Masculino")

        # Componentes Inputs
        self.entry_peso = tk.Entry(root, width=30)
        self.entry_altura = tk.Entry(root, width=30)
        #self.entry_genero = tk.Entry(root, width=30)
        self.entry_idade = tk.Entry(root, width=30)

        # Posicionamento
        self.label_peso.place(x=30, y=210)
        self.entry_peso.place(x=85, y=210)
        self.label_altura.place(x=25, y=240)
        self.entry_altura.place(x=85, y=240)
        #self.label_genero.place(x=40, y=270)
        #self.entry_genero.place(x=85, y=270)
        self.label_idade.place(x=45, y=300)
        self.entry_idade.place(x=85, y=300)
        self.radio_feminino.place(x=180, y=270)
        self.radio_masculino.place(x=80, y=270)

        # Botão para calcular IMC
        botao_calcular_imc = tk.Button(root, text="Calcular IMC", command=self.calcular_imc, width=15, bg='blue', fg="white")
        botao_calcular_imc.place(x=120, y=350)

    def calcular_imc(self):
        peso = self.entry_peso.get()
        altura = self.entry_altura.get()
        genero = self.var_genero.get()
        idade = self.entry_idade.get()

        peso = peso.replace(",", ".")
        altura = altura.replace(",", ".")

        try:
            peso = float(peso)
            altura = float(altura)
            idade = int(idade)
            imc = peso / (altura ** 2)

            classificacao = self.classificar_imc(imc)

            mensagem = f"Seu IMC é: {imc:.2f}\nClassificação: {classificacao}\nGênero: {genero}\nIdade: {idade}"
            messagebox.showinfo("IMC", mensagem)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso, altura e idade.")

    def classificar_imc(self, imc):
        if imc < 18.5:
            return "Baixo peso"
        elif 18.5 <= imc < 25:
            return "Peso normal"
        elif 25 <= imc < 30:
            return "Sobrepeso"
        elif 30 <= imc < 35:
            return "Obesidade grau I"
        elif 35 <= imc < 40:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III"

root = tk.Tk()
root.title("Cálculo de IMC")
imagem = tk.PhotoImage(file="./resources/imc.png")
imagem_label = tk.Label(root, image=imagem)
imagem_label.pack()
root.geometry("330x400")
root.resizable(False, False)

imc_calculator = IMC(root)

root.mainloop()
