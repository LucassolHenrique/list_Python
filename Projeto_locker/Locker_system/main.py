
from Aula08_25.class_SystemaLocker import *
from Aula08_25.class_retornar import *

menu = """
    +----+-----------------------------------+
    |----+   Sistema de Lockers do Tio Ivo   |
    +----+-----------------------------------+
    |  1 | Entrega                           |
    |  2 | Retirada                          |
    |  3 | Configuração                      |
    |  S | Saída                             |
    +----+-----------------------------------+
    Escolha: """

menu_configuracao = """
    +----+-----------------------------------+
    |----+   Configuração                    |
    +----+-----------------------------------+
    |  1 | Cadastrar Novo Morador            |
    |  2 | Alterar Dados Morador             |
    |  3 | Excluir Morador                   |
    |  R | Retornar                          |
    +----+-----------------------------------+
    Escolha: """


#
# submenu configuração
def novo_morador() -> None:
    # sistema.cadastrar_morador(1, Morador("Ana", "101", "1111"))
    # sistema.cadastrar_morador(2, Morador("Clara", "201", "2222"))
    # sistema.cadastrar_morador(3, Morador("Pedro", "301", "3333"))
    pass

def alterar_morador() -> None:
    pass

def excluir_morador() -> None:
    pass

def retornar_menu_geral() -> None:
    raise RetornarMenu

dict_configuracao: dict[str, callable] = {
        "1": novo_morador,
        "2": alterar_morador,
        "3": excluir_morador,
        "R": retornar_menu_geral}

def submenu_configuracao() -> None:
    while True:
        try:
            opcao = input(menu_configuracao).upper()
            dict_configuracao[opcao]()
        except KeyError:
            print("Ops! Escolha incorreta! Tente novamente.")
        except RetornarMenu:
            break

# submenu configuração
###


#
# menugeral
def entrega() -> None:
    def ler_dados_pacote() -> str | None:
        while True:
            print("Escolha o tamanho do Pacote:")
            print("P - Pequeno")
            print("M - Médio")
            print("G - Grande")
            tam_pacote = input("Qual o tamanho do Pacote? (C-Cancela): ").upper()
            if tam_pacote in ['P', 'M', 'G']:
                return tam_pacote
            if tam_pacote == "C":
                return None

            input("OPS. Escolha uma das opções. ")

    def ler_dados_apartamento() -> str | None:
        while True:
            print("="*40)
            num_apartamento = input("Informe o Apartamento? (C-Cancela)").upper()
            if num_apartamento == "C":
                return None
            if sistema.apartamento_valido(num_apartamento):
                return num_apartamento
            input("OPS. Apartamento não encontrado. Enter")

    def ler_dados_entrega() -> tuple[str | None, str | None]:
        num_apartamento = ler_dados_apartamento()
        if num_apartamento is None:
            return None, None
        tam_pacote = ler_dados_pacote()
        return tam_pacote, num_apartamento

    def confirmar_entrega() -> bool:
        while True:
            confirmar = input("Finalizar Entrega? s/n: ").upper()
            if confirmar in ['S', 'N']:
                input("Feche a porta do Locker.")
                if confirmar == 'S':
                    return True
                return False

    # se existe algum locker disponível
    if sistema.existe_algum_locker_disponivel():
        # então mostra os lockers disponíveis
        sistema.todos_lockers_disponiveis()
    else:
        # Caso não exista lockers disponíveis, retorne
        return

    tamanho_pacote, numero_apartamento = ler_dados_entrega()
    # caso de desistência no caminhho
    if tamanho_pacote is None or numero_apartamento is None:
        return

    # locker disponível para o tamnho da entrega
    locker_disponivel = sistema.locker_disponivel(tamanho_pacote)

    # se há um locker disponível
    if locker_disponivel:
        if confirmar_entrega():
            locker_disponivel.indisponibilizar(numero_apartamento)

def retirada() -> None:
    senha_recebida = input("Qual a senha enviada? ").upper()
    sistema.retirar_pacote(senha_recebida)

def configuracao() -> None:
    submenu_configuracao()

def finaliza() -> None:
    print("Sistema Encerrado!")
    exit(0)

dict_escolha: dict[str, callable] = {
        "1": entrega,
        "2": retirada,
        "3": configuracao,
        "S": finaliza}

def menu_geral():
    while True:
        try:
            opcao: str = input(menu).upper()
            dict_escolha[opcao]()
        except KeyError:
            print("Ops! Escolha incorreta! Tente novamente.")
# menugeral
###

def gerar_dados_para_teste() -> None:
    """Popula o dicionario com dados para teste"""
    sistema.gerar_lockers()
    sistema.gerar_moradores()

if __name__ == "__main__":
    sistema: SistemaLocker = SistemaLocker()
    # Gera dados para teste
    gerar_dados_para_teste()
    menu_geral()
