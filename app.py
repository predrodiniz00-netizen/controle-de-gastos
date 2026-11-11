import tkinter as tk

janela = tk.Tk()

janela.title("meu controle de gastos")

janela.geometry("600x400")

titulo = tk.Label(
    janela,
    text="Meu Controle de Gastos!",
)
titulo.pack()

texto = tk.Label(
    janela,
    text="Nome do gasto:"
)
texto.pack()

entrada = tk.Entry(janela)
entrada.pack()

gastos = []
def cadastrar_gasto():
    gastos.append(entrada.get())
    lista_gastos.insert(tk.END, entrada.get())
    entrada.delete(0, tk.END)

valor_de_gasto = tk.Label(
    janela,
    text="Valor do gasto (R$):"
)
valor_de_gasto.pack()

entrada_valor = tk.Entry(janela)
entrada_valor.pack()

valor = float()
def calcular_total():
    total = 0
    for gasto in gastos:
        total += float(gasto)
    return total

lista_gastos = tk.Listbox(janela)
lista_gastos.pack()

botao = tk.Button(
    janela,
    text="Cadastrar gasto",
    command=cadastrar_gasto
)
botao.pack()

janela.mainloop()
print(gastos)