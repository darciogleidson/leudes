#Aplicação para ler um arquivo excel e gerar um arquivo txt com os dados do excel
#No arquivo excel temos as seguintes colunas: Matricula, Valor
#Queria a aplicação com uma tela para selecionar o arquivo excel e gerar o arquivo txt
#O arquivo txt deve ter o nome do arquivo excel + .txt

#Importando as bibliotecas
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import pandas as pd

#Criando a tela
tela = Tk()
tela.title("Gerador de Arquivo TXT")
tela.geometry("500x300")
tela.configure(background="white")
tela.resizable(width=False, height=False)

#Criando a função para selecionar o arquivo excel
def selecionar_arquivo():
    global arquivo
    arquivo = filedialog.askopenfilename(initialdir="/", title="Selecione o Arquivo", filetypes=(("Arquivos Excel", "*.xlsx"), ("Todos os Arquivos", "*.*")))
    lbl_arquivo["text"] = arquivo

#Criando a função para gerar o arquivo txt
def gerar_arquivo():
    try:
        df = pd.read_excel(arquivo)
        df.to_csv(arquivo + ".txt", sep="\t", index=False)
        messagebox.showinfo(title="Sucesso", message="Arquivo gerado com sucesso!")
    except:
        messagebox.showinfo(title="Erro", message="Erro ao gerar o arquivo!")

#Criando os componentes
lbl_titulo = Label(tela, text="Gerador de Arquivo TXT", background="white", foreground="black", font=("Arial", 20, "bold"))
lbl_titulo.place(x=80, y=10)

lbl_arquivo = Label(tela, text="Selecione o arquivo", background="white", foreground="black", font=("Arial", 12, "bold"))
lbl_arquivo.place(x=150, y=80)

btn_selecionar = Button(tela, text="Selecionar", background="white", foreground="black", font=("Arial", 12, "bold"), command=selecionar_arquivo)
btn_selecionar.place(x=200, y=120)

btn_gerar = Button(tela, text="Gerar Arquivo", background="white", foreground="black", font=("Arial", 12, "bold"), command=gerar_arquivo)
btn_gerar.place(x=190, y=160)

#Iniciando a tela
tela.mainloop()
