# Sistema de locker de entrega de produtos

# Sistema de locker de entrega de produtos


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
    def tamanho(self):
        return self.__tamanho

    @property
    def disponivel(self):
        return self.__disponivel

    @disponivel.setter
    def disponivel(self, valor):
        self.__disponivel = valor

    @property
    def apartamento(self):
        return self.__apartamento

    @apartamento.setter
    def apartamento(self, valor):
        self.__apartamento = valor

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, valor):
        self.__senha = valor

    def entregar(self, apartamento: int):
        import random
        self.__disponivel = False
        self.__apartamento = apartamento
        self.__senha = str(random.randint(1000, 9999))
        print(
            f"Entrega registrada! Senha enviada para o apartamento {apartamento}: {self.__senha}"
        )

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
    def nome(self):
        return self.__nome


# Listas globais protegidas (por convenção, mas não há encapsulamento real em listas globais)
moradores = []
apartamentos = []  # Agora armazena objetos Predio
lockers = []
SENHA_SINDICO = "1234"  # senha mestra usada na retirar_produtos


# Cadastro de morador, apartamento e locker
def cadastrar_morador():
    nome = input("Nome do morador: ")
    numero_apartamento = input("Número do apartamento: ")
    # Verifica se já existe um apartamento com essa numeração
    if any(ap.numeracao_casa == int(numero_apartamento)
           for ap in apartamentos):
        print("Este apartamento já possui um locker cadastrado!")
        return
    tamanho_locker = input("Tamanho do locker (P/M/G): ").upper()

    novo_morador = Morador(nome)
    moradores.append(novo_morador)

    novo_apartamento = Predio(int(numero_apartamento))
    apartamentos.append(novo_apartamento)

    novo_locker = Locker(tamanho_locker)
    novo_locker.apartamento = int(numero_apartamento)
    lockers.append(novo_locker)

    print(
        f"Morador {nome} cadastrado no apartamento {numero_apartamento} com locker tamanho {tamanho_locker}."
    )


# Função para realizar entrega
def realizar_entrega():
    tamanho = input("Tamanho do pacote (P/M/G): ").upper()
    apartamento = input("Número do apartamento: ")
    if not any(ap.numeracao_casa == int(apartamento) for ap in apartamentos):
        print("Apartamento não cadastrado no prédio!")
        return
    for locker in lockers:
        if locker.tamanho == tamanho and locker.disponivel:
            locker.entregar(int(apartamento))
            return
    print("Não há lockers disponíveis desse tamanho.")


# Função para retirada de produto
def retirar_produto():
    apartamento = input("Número do apartamento: ")
    senha = input("Senha recebida: ")
    for locker in lockers:
        if locker.apartamento == int(apartamento) and not locker.disponivel:
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


# Status dos lockers
def status_locker():
    print("\nStatus dos Lockers:")
    for i, locker in enumerate(lockers, 1):
        status = "Disponível" if locker.disponivel else f"Ocupado (Apto: {locker.apartamento})"
        print(f"{i} - Locker {locker.tamanho}: {status}")


# Status dos apartamentos com entregas
def status_apartamento():
    print("\nStatus dos Apartamentos com entregas:")
    encontrou = False
    for locker in lockers:
        if not locker.disponivel:
            # Busca o objeto Predio correspondente ao apartamento
            predio_obj = next((ap for ap in apartamentos
                               if ap.numeracao_casa == locker.apartamento),
                              None)
            if predio_obj:
                print(
                    f"Apartamento {locker.apartamento} (Casa: {predio_obj.numeracao_casa}) possui entrega no locker {locker.tamanho}."
                )
            else:
                print(
                    f"Apartamento {locker.apartamento} possui entrega no locker {locker.tamanho}."
                )
            encontrou = True
    if not encontrou:
        print("Nenhum apartamento possui entregas no momento.")
