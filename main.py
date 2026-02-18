import tkinter as tk

# 🧠 Lógica da Calculadora
def clique(valor):
    if valor == "=":
        try:
            # Resolve a conta e mostra o resultado
            resultado = eval(tela.get())
            tela.delete(0, tk.END)
            tela.insert(0, str(resultado))
        except:
            tela.delete(0, tk.END)
            tela.insert(0, "Erro")
    elif valor == "C":
        tela.delete(0, tk.END)
    else:
        tela.insert(tk.END, valor)

# 🪟 Configuração da Janela Principal
janela = tk.Tk()
janela.title("Calculadora Pro")
janela.configure(bg="#242424")  # Cor de fundo da janela

# 🖥️ Tela de Exibição (Display)
tela = tk.Entry(janela, font=("Arial", 28, "bold"), borderwidth=0, 
                relief="flat", justify="right", bg="#242424", fg="white", 
                insertbackground="white")
tela.grid(row=0, column=0, columnspan=4, padx=20, pady=30, sticky="nsew")

# 🟥 Lista de Botões
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# 🔄 Criando os botões com design moderno
linha = 1
coluna = 0

for b in botoes:
    # Definindo cores diferentes para tipos de botões
    if b in "0123456789":
        cor_fundo = "#333333"  # Cinza escuro para números
    elif b == "=":
        cor_fundo = "#FF9500"  # Laranja para o resultado
    else:
        cor_fundo = "#4B4B4B"  # Cinza médio para operadores e 'C'

    comando = lambda x=b: clique(x)
    
    tk.Button(janela, text=b, width=5, height=2, font=("Arial", 16, "bold"),
              bg=cor_fundo, fg="white", borderwidth=0, relief="flat",
              activebackground="#555555", activeforeground="white",
              command=comando).grid(row=linha, column=coluna, padx=2, pady=2, sticky="nsew")
    
    coluna += 1
    if coluna > 3:
        coluna = 0
        linha += 1

# Ajusta o redimensionamento das colunas
for i in range(4):
    janela.grid_columnconfigure(i, weight=1)

janela.mainloop()