# Você deverá criar um sistema de locker de entrega de produtos.
# Lógica: O entregador realiza a entrega de um produto escolhendo a opção ENTREGA.
#               Informa o tamanho do pacote, o apartamento e finaliza a entrega. O sistema envia uma mensagem ao nome do apartamento cadastrado com uma senha gerada aleatóriamente.
#
#.             O morador, ao retirar o produto, informa o apartamento e a senha, o locker "Abre". O morador Finaliza a retirada e o locker é liberado.
#
#.             Em configurações deve existir uma opção de cadastro, onde o usuário irá cadastrar o apartamento e uma senha para utilizar o locker.

# objetos
#   Morador
#   def Nome
# predio
#   def numeracao_casa

class predio:

  def __init__(self, numeracao_casa: int) -> None:
    self.numeracao_casa = numeracao_casa
    pass
  
class Locker:
    def __init__(self, tamanho: str) -> None:
        self.tamanho = tamanho  # 'P', 'M' ou 'G'
        self.disponivel = True
        self.apartamento = None
        self.senha = None

    def entregar(self, apartamento: int):
        import random
        self.disponivel = False
        self.apartamento = apartamento
        self.senha = str(random.randint(1000, 9999))
        print(f"Entrega registrada! Senha enviada para o apartamento {apartamento}: {self.senha}")

    def retirar(self, senha: str):
        if self.senha == senha:
            print("Locker aberto! Retire seu produto.")
            self.disponivel = True
            self.apartamento = None
            self.senha = None
        else:
            print("Senha incorreta.")

class Morador:
    
    def __init__(self, nome: str):
        self.nome = nome





#tamanhos dos lockers


def cadastrar_morador():
    nome = input("Nome do morador: ")
    numero_apartamento = input("Número do apartamento: ")
    if numero_apartamento in apartamentos:
        print("Este apartamento já possui um locker cadastrado!")
        return
    tamanho_locker = input("Tamanho do locker (P/M/G): ").upper()

    # Cria o morador
    novo_morador = Morador(nome)
    moradores.append(novo_morador)

    # Cria o apartamento (e adiciona à lista de apartamentos)
    novo_apartamento = predio(numero_apartamento)
    apartamentos.append(numero_apartamento)

    # Cria o locker vinculado ao apartamento
    novo_locker = Locker(tamanho_locker)
    novo_locker.apartamento = numero_apartamento
    lockers.append(novo_locker)

    print(f"Morador {nome} cadastrado no apartamento {numero_apartamento} com locker tamanho {tamanho_locker}.")

    
#listagens (armazenamento de informações)

moradores = []
apartamentos = []
lockers = [Locker('P'), Locker('M'), Locker('G')]  # Exemplo de 3 lockers, um de cada tamanho
SENHA_SINDICO = "1234" #senha mestra usada na retirar_produtos

# Funções  
def realizar_entrega():
    tamanho = input("Tamanho do pacote (P/M/G): ").upper()
    apartamento = input("Número do apartamento: ")
    if apartamento not in apartamentos:
        print("Apartamento não cadastrado no prédio!")
        return
    for locker in lockers:
        if locker.tamanho == tamanho and locker.disponivel:
            locker.entregar(apartamento)
            return
    print("Não há lockers disponíveis desse tamanho.")

def retirar_produto():
    apartamento = input("Número do apartamento: ")
    senha = input("Senha recebida: ")
    for locker in lockers:
        if locker.apartamento == apartamento and not locker.disponivel:
            if senha == SENHA_SINDICO:
                print("Acesso de síndico autorizado.")
                locker.disponivel = True
                locker.apartamento = None
                locker.senha = None
                print("Locker aberto! Retire seu produto.")
                return
            locker.retirar(senha)
            return
    print("Nenhum locker encontrado para esse apartamento.")


# status locker do 3 
def status_locker():
    print("\nStatus dos Lockers:")
    for i, locker in enumerate(lockers, 1):
        status = "Disponível" if locker.disponivel else f"Ocupado (Apto: {locker.apartamento})"
        print(f"{i} - Locker {locker.tamanho}: {status}")


def status_apartamento():
    print("\nStatus dos Apartamentos com entregas:")
    encontrou = False
    for locker in lockers:
        if not locker.disponivel:
            print(f"Apartamento {locker.apartamento} possui entrega no locker {locker.tamanho}.")
            encontrou = True
    if not encontrou:
        print("Nenhum apartamento possui entregas no momento.")