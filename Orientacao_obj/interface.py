import tkinter as tk
from tkinter import simpledialog, messagebox
from class_obj import *

# Carrega moradores do JSON ao iniciar a interface
carregar_moradores_json()

def atualizar_lista_moradores(lista):
    lista.delete(0, tk.END)
    for morador, ap in zip(moradores, apartamentos):
        lista.insert(tk.END, f"{morador.nome} - Casa {ap.numeracao_casa}")

def alterar_nome_morador():
    selecionado = lista_moradores.curselection()
    if not selecionado:
        messagebox.showinfo("Aviso", "Selecione um morador.")
        return
    idx = selecionado[0]
    novo_nome = simpledialog.askstring("Alterar nome", "Novo nome:")
    if novo_nome:
        moradores[idx]._Morador__nome = novo_nome
        salvar_moradores_json()
        atualizar_lista_moradores(lista_moradores)
        messagebox.showinfo("Sucesso", "Nome alterado!")

def abrir_locker_sindico():
    senha = simpledialog.askstring("Síndico", "Digite a senha do síndico:", show="*")
    if senha != SENHA_SINDICO:
        messagebox.showerror("Erro", "Senha incorreta!")
        return
    apto = simpledialog.askinteger("Abrir Locker", "Número do apartamento:")
    for locker in lockers:
        if locker.apartamento == apto and not locker.disponivel:
            locker.disponivel = True
            locker.apartamento = None
            locker.senha = None
            messagebox.showinfo("Sucesso", "Locker aberto pelo síndico!")
            return
    messagebox.showinfo("Aviso", "Nenhum locker ocupado para esse apartamento.")

def criar_locker_sindico():
    senha = simpledialog.askstring("Síndico", "Digite a senha do síndico:", show="*")
    if senha != SENHA_SINDICO:
        messagebox.showerror("Erro", "Senha incorreta!")
        return
    tamanho = simpledialog.askstring("Locker", "Tamanho do locker (P/M/G):").upper()
    quantidade = simpledialog.askinteger("Locker", "Quantidade de lockers:")
    for _ in range(quantidade):
        lockers.append(Locker(tamanho))
    messagebox.showinfo("Sucesso", f"{quantidade} locker(s) do tamanho {tamanho} criado(s)!")

def ao_fechar():
    salvar_moradores_json()
    root.destroy()

# Janela principal
root = tk.Tk()
root.title("Sistema de Lockers")

lista_moradores = tk.Listbox(root, width=40)
lista_moradores.pack(pady=10)
atualizar_lista_moradores(lista_moradores)

btn_alterar = tk.Button(root, text="Alterar nome do morador", command=alterar_nome_morador)
btn_alterar.pack(pady=5)

btn_abrir = tk.Button(root, text="Síndico: Abrir qualquer locker", command=abrir_locker_sindico)
btn_abrir.pack(pady=5)

btn_criar = tk.Button(root, text="Síndico: Criar novo locker", command=criar_locker_sindico)
btn_criar.pack(pady=5)

btn_atualizar = tk.Button(root, text="Atualizar lista", command=lambda: atualizar_lista_moradores(lista_moradores))
btn_atualizar.pack(pady=5)

root.protocol("WM_DELETE_WINDOW", ao_fechar)
root.mainloop()