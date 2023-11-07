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

        # Componentes Inputs
        self.entry_peso = tk.Entry(root, width=30)
        self.entry_altura = tk.Entry(root, width=30)

        # Posicionamento
        self.label_peso.place(x=30, y=210)
        self.entry_peso.place(x=85, y=210)
        self.label_altura.place(x=25, y=240)
        self.entry_altura.place(x=85, y=240)

        # Botão para calcular IMC
        botao_calcular_imc = tk.Button(root, text="Calcular IMC", command=self.calcular_imc, width=15, bg='blue', fg="white")
        botao_calcular_imc.place(x=120, y=270)

    def calcular_imc(self):
        peso = self.entry_peso.get()
        altura = self.entry_altura.get()
        try:
            peso = float(peso)
            altura = float(altura)
            imc = peso / (altura ** 2)
            messagebox.showinfo("IMC", f"Seu IMC é: {imc:.2f}")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos para peso e altura.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cálculo de IMC")
    imagem = tk.PhotoImage(file="./resources/imc.png")
    imagem_label = tk.Label(root, image=imagem)
    imagem_label.pack()
    root.geometry("330x330")
    root.resizable(False, False)

    imc_calculator = IMC(root)

    root.mainloop()
