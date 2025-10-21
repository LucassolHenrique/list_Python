import streamlit as st
import json
import os

# Nome do arquivo que funcionará como nosso "banco de dados"
NOME_ARQUIVO = 'jogo_da_vida.json'

# --- Funções para gerenciar os dados (as mesmas do exemplo anterior) ---

def carregar_dados():
    """Carrega os dados do arquivo JSON. Se o arquivo não existir, cria um com valores padrão."""
    if not os.path.exists(NOME_ARQUIVO):
        # Dados iniciais se o jogo estiver começando agora
        dados_padrao = {
            "pontos_totais": 0,
            "tarefas": {
                "Ler por 30 minutos": 15,
                "Estudar por 2 horas": 30,
                "Dormir no horário certo": 10,
                "Fazer 30 min de exercício": 20,
                "Beber 2 litros de água": 5
            },
            "recompensas": {
                "Dormir até mais tarde (1h)": 50,
                "Comprar uma porcaria (lanche)": 70,
                "1h de videogame/série sem culpa": 100,
                "Ir ao sushi": 350,
                "Comprar um livro novo": 200
            }
        }
        salvar_dados(dados_padrao)
        return dados_padrao
    
    with open(NOME_ARQUIVO, 'r', encoding='utf-8') as f:
        return json.load(f)

def salvar_dados(dados):
    """Salva o dicionário de dados no arquivo JSON."""
    with open(NOME_ARQUIVO, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# --- Lógica do Streamlit (aqui o "front" acontece!) ---

def main():
    st.set_page_config(layout="centered", page_title="Meu Jogo da Vida")
    
    dados = carregar_dados()

    # Título principal
    st.title("🎯 Meu Jogo da Vida Pessoal")
    st.markdown("### Gamifique seus hábitos e conquiste suas metas!")

    # Exibição de pontos
    st.metric(label="Seus Pontos Atuais", value=f"{dados['pontos_totais']} pts")

    st.markdown("---")

    # Colunas para organizar a interface
    col1, col2 = st.columns(2)

    with col1:
        st.header("✅ Registrar Atividade")
        st.markdown("Escolha uma tarefa que você concluiu:")

        tarefas = dados['tarefas']
        tarefas_lista = list(tarefas.keys())

        # Usar um selectbox para escolher a tarefa
        tarefa_selecionada = st.selectbox(
            "Qual tarefa você completou?", 
            options=tarefas_lista,
            format_func=lambda x: f"{x} (+{tarefas[x]} pts)"
        )

        if st.button("Concluir Tarefa e Ganhar Pontos", key="btn_tarefa"):
            if tarefa_selecionada:
                pontos_ganhos = tarefas[tarefa_selecionada]
                dados['pontos_totais'] += pontos_ganhos
                salvar_dados(dados)
                st.success(f"🎉 Você ganhou {pontos_ganhos} pontos por '{tarefa_selecionada}'!")
                st.experimental_rerun() # Recarrega a página para atualizar os pontos

    with col2:
        st.header("🎁 Gastar Pontos")
        st.markdown("Resgate suas recompensas com seus pontos:")

        recompensas = dados['recompensas']
        recompensas_lista = list(recompensas.keys())

        # Usar um selectbox para escolher a recompensa
        recompensa_selecionada = st.selectbox(
            "Qual recompensa você quer resgatar?", 
            options=recompensas_lista,
            format_func=lambda x: f"{x} ({recompensas[x]} pts)"
        )

        if st.button("Resgatar Recompensa", key="btn_recompensa"):
            if recompensa_selecionada:
                custo = recompensas[recompensa_selecionada]
                if dados['pontos_totais'] >= custo:
                    dados['pontos_totais'] -= custo
                    salvar_dados(dados)
                    st.balloons() # Efeito visual de balões!
                    st.success(f"✨ Parabéns! Você resgatou '{recompensa_selecionada}'. Aproveite!")
                    st.experimental_rerun() # Recarrega a página para atualizar os pontos
                else:
                    st.error(f"Você não tem pontos suficientes para '{recompensa_selecionada}'. Faltam {custo - dados['pontos_totais']} pontos.")
    
    st.markdown("---")

    st.header("📋 Suas Tarefas e Recompensas")
    
    tab1, tab2 = st.tabs(["Minhas Tarefas", "Minhas Recompensas"])

    with tab1:
        st.subheader("Tarefas Disponíveis:")
        for tarefa, pontos in dados['tarefas'].items():
            st.markdown(f"- **{tarefa}**: Ganha **{pontos}** pontos")
        
        # Opção para adicionar nova tarefa
        st.markdown("---")
        st.subheader("Adicionar Nova Tarefa")
        nova_tarefa = st.text_input("Nome da nova tarefa:")
        pontos_nova_tarefa = st.number_input("Pontos para esta tarefa:", min_value=1, value=10)
        if st.button("Adicionar Tarefa", key="add_tarefa"):
            if nova_tarefa and nova_tarefa not in dados['tarefas']:
                dados['tarefas'][nova_tarefa] = pontos_nova_tarefa
                salvar_dados(dados)
                st.success(f"Tarefa '{nova_tarefa}' adicionada!")
                st.experimental_rerun()
            elif nova_tarefa in dados['tarefas']:
                st.warning("Esta tarefa já existe!")
            else:
                st.warning("Por favor, insira o nome da tarefa.")

    with tab2:
        st.subheader("Recompensas Disponíveis:")
        for recompensa, custo in dados['recompensas'].items():
            st.markdown(f"- **{recompensa}**: Custa **{custo}** pontos")
        
        # Opção para adicionar nova recompensa
        st.markdown("---")
        st.subheader("Adicionar Nova Recompensa")
        nova_recompensa = st.text_input("Nome da nova recompensa:")
        custo_nova_recompensa = st.number_input("Custo da recompensa (pontos):", min_value=1, value=100)
        if st.button("Adicionar Recompensa", key="add_recompensa"):
            if nova_recompensa and nova_recompensa not in dados['recompensas']:
                dados['recompensas'][nova_recompensa] = custo_nova_recompensa
                salvar_dados(dados)
                st.success(f"Recompensa '{nova_recompensa}' adicionada!")
                st.experimental_rerun()
            elif nova_recompensa in dados['recompensas']:
                st.warning("Esta recompensa já existe!")
            else:
                st.warning("Por favor, insira o nome da recompensa.")

if __name__ == "__main__":
    main()