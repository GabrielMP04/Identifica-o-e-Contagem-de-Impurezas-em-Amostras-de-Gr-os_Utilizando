import customtkinter as ctk

from tkinter import filedialog
from PIL import Image

from predict import analisar
from utils import contar_graos

ctk.set_appearance_mode("dark")

janela = ctk.CTk()

janela.title(
    "Identificação de Impurezas em Grãos"
)

janela.geometry("1000x700")

imagem_label = ctk.CTkLabel(
    janela,
    text="Nenhuma imagem"
)

imagem_label.pack(pady=20)

resultado_label = ctk.CTkLabel(
    janela,
    text=""
)

resultado_label.pack()


def selecionar():

    arquivo = filedialog.askopenfilename()

    if not arquivo:
        return

    resultado = analisar(arquivo)

    sadios, impurezas = contar_graos(resultado)

    resultado_label.configure(
        text=
        f"Sadios: {sadios}\n"
        f"Impurezas: {impurezas}"
    )


botao = ctk.CTkButton(
    janela,
    text="Selecionar Imagem",
    command=selecionar
)

botao.pack(pady=20)

janela.mainloop()