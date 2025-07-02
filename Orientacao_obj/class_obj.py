import json
import os

# A senha foi unificada para 9999 conforme a exigência da senha geral
SENHA_SINDICO = "9999" 
moradores = []
apartamentos = [] 
lockers = []

def inicializar_lockers_do_json():
    caminho = os.path.join(os.path.dirname(__file__), "lockers_config.json")
    if not os.path.exists(caminho):
        print("Arquivo lockers_config.json não encontrado!")
        return
    with open(caminho, "r") as f:
        config = json.load(f)
    for tamanho, quantidade in config.items():
        for _ in range(quantidade):
            lockers.append(Locker(tamanho))
            
class Predio:
    def __init__(self, numeracao_casa: int) -> None:
        self.__numeracao_casa = numeracao_casa

    @property
    def numeracao_casa(self):
        return self.__numeracao_casa

class Locker:
    def __init__(self, tamanho: str) -> None:
        self.__tamanho = tamanho
        self.__disponivel = True
        self.__apartamento = None
        self.__senha = None

    @property
    def tamanho(self): return self.__tamanho
    @property
    def disponivel(self): return self.__disponivel
    @disponivel.setter
    def disponivel(self, valor): self.__disponivel = valor
    @property
    def apartamento(self): return self.__apartamento
    @apartamento.setter
    def apartamento(self, valor): self.__apartamento = valor
    @property
    def senha(self): return self.__senha
    @senha.setter
    def senha(self, valor): self.__senha = valor

    def entregar(self, apartamento: int):
        import random
        self.__disponivel = False
        self.__apartamento = apartamento
        self.__senha = str(random.randint(1000, 9999))
        print(f"Entrega registrada! Senha enviada para o apartamento {apartamento}: {self.__senha}")

    def retirar(self, senha: str):
        if self.__senha == senha:
            print("Locker aberto! Retire seu produto.")
            self.__disponivel = True
            self.__apartamento = None
            self.__senha = None
        else:
            print("Senha incorreta.")

class Morador:
    def __init__(self, nome: str):
        self.__nome = nome
    @property
    def nome(self): return self.__nome
    @nome.setter
    def nome(self, novo_nome): self.__nome = novo_nome

# --- FUNÇÕES DE DADOS (JSON) CORRIGIDAS ---

def salvar_moradores_json():
    """Salva nome e apartamento juntos para manter a consistência."""
    dados_para_salvar = []
    for morador, ap in zip(moradores, apartamentos):
        dados_para_salvar.append({
            "nome": morador.nome,
            "apartamento": ap.numeracao_casa
        })
    # Usando o mesmo diretório do script para o arquivo JSON
    caminho_json = os.path.join(os.path.dirname(__file__), "moradores.json")
    with open(caminho_json, "w") as f:
        json.dump(dados_para_salvar, f, indent=4)

def carregar_moradores_json():
    """Carrega nome e apartamento, recriando os objetos corretamente."""
    caminho_json = os.path.join(os.path.dirname(__file__), "moradores.json")
    try:
        with open(caminho_json, "r") as f:
            lista = json.load(f)
            # Limpa as listas globais antes de carregar para evitar duplicatas
            moradores.clear()
            apartamentos.clear()
            for item in lista:
                moradores.append(Morador(item["nome"]))
                apartamentos.append(Predio(item["apartamento"]))
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existe ou está vazio, não faz nada.
        pass