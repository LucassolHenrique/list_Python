import tkinter as tk
from tkinter import simpledialog, messagebox
import sys
import io
from class_obj import * # Importa tudo de class_obj.py

def atualizar_lista_moradores(listbox):
    """Limpa e atualiza o Listbox com os moradores e seus apartamentos."""
    listbox.delete(0, tk.END)
    for morador, ap in zip(moradores, apartamentos):
        listbox.insert(tk.END, f"{morador.nome} - Apto: {ap.numeracao_casa}")

def cadastrar_morador_gui():
    """GUI para cadastrar morador, com verificação de senha do síndico."""
    senha = simpledialog.askstring("Área do Síndico", "Digite a senha do síndico para cadastrar:", show="*")
    if senha != SENHA_SINDICO:
        messagebox.showerror("Erro", "Senha incorreta!")
        return

    nome = simpledialog.askstring("Cadastrar Morador", "Nome do novo morador:")
    if not nome: return

    try:
        numero_apartamento = simpledialog.askinteger("Cadastrar Morador", "Número do apartamento:")
        if numero_apartamento is None: return

        if any(ap.numeracao_casa == int(numero_apartamento) for ap in apartamentos):
            messagebox.showerror("Erro", "Este apartamento já possui um morador cadastrado!")
            return

        moradores.append(Morador(nome))
        apartamentos.append(Predio(int(numero_apartamento)))
        salvar_moradores_json()
        atualizar_lista_moradores(lista_moradores_box)
        messagebox.showinfo("Sucesso", f"Morador {nome} cadastrado no apartamento {numero_apartamento}.")
    except (ValueError, TypeError):
        messagebox.showerror("Erro", "Número do apartamento inválido.")

def alterar_nome_morador_gui():
    """GUI para morador alterar o próprio nome."""
    selecionado = lista_moradores_box.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um morador na lista.")
        return
    idx = selecionado[0]
    novo_nome = simpledialog.askstring("Alterar Nome", f"Digite o novo nome para '{moradores[idx].nome}':")
    if novo_nome:
        moradores[idx].nome = novo_nome
        salvar_moradores_json()
        atualizar_lista_moradores(lista_moradores_box)
        messagebox.showinfo("Sucesso", "Nome alterado com sucesso!")

def excluir_morador_gui():
    """GUI para excluir um morador com senha do síndico."""
    selecionado = lista_moradores_box.curselection()
    if not selecionado:
        messagebox.showwarning("Aviso", "Selecione um morador para excluir.")
        return
    
    idx = selecionado[0]
    confirmar = messagebox.askyesno("Confirmar", f"Deseja excluir '{moradores[idx].nome}'? Esta ação não pode ser desfeita.")
    if not confirmar: return

    senha = simpledialog.askstring("Área do Síndico", "Digite a senha do síndico para confirmar a exclusão:", show="*")
    if senha != SENHA_SINDICO:
        messagebox.showerror("Erro", "Senha incorreta!")
        return
    
    moradores.pop(idx)
    apartamentos.pop(idx)
    salvar_moradores_json()
    atualizar_lista_moradores(lista_moradores_box)
    messagebox.showinfo("Sucesso", "Morador removido.")

def realizar_entrega_gui():
    """GUI para realizar uma entrega em um locker."""
    tamanho = simpledialog.askstring("Realizar Entrega", "Tamanho do pacote (P/M/G):")
    if not tamanho: return
    tamanho = tamanho.upper()
    if tamanho not in ['P', 'M', 'G']:
        messagebox.showerror("Erro", "Tamanho inválido. Use P, M ou G.")
        return
    try:
        apartamento = simpledialog.askinteger("Realizar Entrega", "Número do apartamento de destino:")
        if apartamento is None: return
        if not any(ap.numeracao_casa == int(apartamento) for ap in apartamentos):
            messagebox.showerror("Erro", "Apartamento não cadastrado!")
            return
        for locker in lockers:
            if locker.tamanho == tamanho and locker.disponivel:
                locker.entregar(int(apartamento))
                messagebox.showinfo("Sucesso", f"Entrega registrada no locker! A senha é: {locker.senha}")
                return
        messagebox.showwarning("Aviso", "Não há lockers disponíveis desse tamanho.")
    except (ValueError, TypeError):
        messagebox.showerror("Erro", "Número do apartamento inválido.")

def retirar_produto_gui():
    """GUI para o morador retirar um produto."""
    try:
        apartamento = simpledialog.askinteger("Retirar Produto", "Número do seu apartamento:")
        if apartamento is None: return
        senha = simpledialog.askstring("Retirar Produto", "Senha de retirada:", show="*")
        if not senha: return
        for locker in lockers:
            if locker.apartamento == int(apartamento) and locker.senha == senha:
                locker.retirar(senha)
                messagebox.showinfo("Sucesso", "Locker aberto! Retire seu produto.")
                return
        messagebox.showerror("Erro", "Dados incorretos ou nenhuma entrega encontrada para este apartamento.")
    except (ValueError, TypeError):
        messagebox.showerror("Erro", "Número do apartamento inválido.")

def status_locker_gui():
    """Exibe o status de todos os lockers em uma janela."""
    status_text = "Status de Todos os Lockers:\n\n"
    for i, locker in enumerate(lockers, 1):
        status = "Disponível" if locker.disponivel else f"Ocupado (Apto: {locker.apartamento})"
        status_text += f"{i} - Locker {locker.tamanho}: {status}\n"
    messagebox.showinfo("Status dos Lockers", status_text)

def criar_locker_sindico_gui():
    """GUI para o síndico criar novos lockers (temporários)."""
    senha = simpledialog.askstring("Área do Síndico", "Digite a senha do síndico:", show="*")
    if senha != SENHA_SINDICO:
        messagebox.showerror("Erro", "Senha incorreta!")
        return
    tamanho = simpledialog.askstring("Criar Locker", "Tamanho do novo locker (P/M/G):").upper()
    if tamanho not in ['P', 'M', 'G']:
        messagebox.showerror("Erro", "Tamanho inválido. Use P, M ou G.")
        return
    quantidade = simpledialog.askinteger("Criar Locker", f"Quantidade de lockers de tamanho '{tamanho}':")
    if quantidade and quantidade > 0:
        for _ in range(quantidade):
            lockers.append(Locker(tamanho))
        messagebox.showinfo("Sucesso", f"{quantidade} locker(s) de tamanho {tamanho} criado(s)!")
        status_locker_gui()

def abrir_locker_sindico_gui():
    """GUI para o síndico abrir qualquer locker."""
    senha = simpledialog.askstring("Área do Síndico", "Digite a senha do síndico:", show="*")
    if senha != SENHA_SINDICO:
        messagebox.showerror("Erro", "Senha incorreta!")
        return
    apto = simpledialog.askinteger("Chave Mestra", "Número do apartamento para liberar o locker:")
    if apto is None: return
    for locker in lockers:
        if locker.apartamento == apto:
            locker.disponivel = True
            locker.apartamento = None
            locker.senha = None
            messagebox.showinfo("Sucesso", f"Locker do apartamento {apto} foi liberado pela chave mestra!")
            return
    messagebox.showinfo("Aviso", "Nenhum locker ocupado foi encontrado para este apartamento.")

def ao_fechar():
    """Salva os dados antes de fechar a janela."""
    salvar_moradores_json()
    root.destroy()

# --- Bloco Principal de Execução ---
if __name__ == "__main__":
    inicializar_lockers_do_json()
    carregar_moradores_json()

    root = tk.Tk()
    root.title("Sistema de Gestão de Lockers")
    root.geometry("450x550")

    frame_moradores = tk.LabelFrame(root, text="Gestão de Moradores", padx=10, pady=10)
    frame_moradores.pack(pady=10, padx=10, fill="x")
    
    lista_moradores_box = tk.Listbox(frame_moradores, width=50, height=6)
    lista_moradores_box.pack(pady=5)
    
    btn_alterar = tk.Button(frame_moradores, text="Alterar Nome do Morador Selecionado", command=alterar_nome_morador_gui)
    btn_alterar.pack(pady=2, fill="x")

    frame_op = tk.LabelFrame(root, text="Operações de Locker", padx=10, pady=10)
    frame_op.pack(pady=5, padx=10, fill="x")
    btn_entregar = tk.Button(frame_op, text="Realizar Entrega", command=realizar_entrega_gui)
    btn_entregar.pack(side="left", expand=True, padx=5)
    btn_retirar = tk.Button(frame_op, text="Retirar Produto", command=retirar_produto_gui)
    btn_retirar.pack(side="left", expand=True, padx=5)
    btn_status_locker = tk.Button(frame_op, text="Ver Status dos Lockers", command=status_locker_gui)
    btn_status_locker.pack(side="left", expand=True, padx=5)

    frame_sindico = tk.LabelFrame(root, text="Área do Síndico (Senha: 9999)", padx=10, pady=10)
    frame_sindico.pack(pady=10, padx=10, fill="x")
    
    btn_cadastrar = tk.Button(frame_sindico, text="Cadastrar Novo Morador", command=cadastrar_morador_gui)
    btn_cadastrar.pack(pady=2, fill="x")
    btn_excluir = tk.Button(frame_sindico, text="Excluir Morador Selecionado", command=excluir_morador_gui)
    btn_excluir.pack(pady=2, fill="x")
    btn_criar_sindico = tk.Button(frame_sindico, text="Criar Novos Lockers", command=criar_locker_sindico_gui)
    btn_criar_sindico.pack(pady=2, fill="x")
    btn_abrir_sindico = tk.Button(frame_sindico, text="Abrir Locker (Chave Mestra)", command=abrir_locker_sindico_gui)
    btn_abrir_sindico.pack(pady=2, fill="x")

    atualizar_lista_moradores(lista_moradores_box)
    root.protocol("WM_DELETE_WINDOW", ao_fechar)
    root.mainloop()