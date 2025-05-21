import random

class Locker:
    """
    Classe que representa um locker para armazenar pacotes.

    Atributos:
        id (int): Identificador único do locker.
        tamanho (str): Tamanho do locker ('P' - Pequeno, 'M' - Médio, 'G' - Grande).
        disponivel (bool): Indica se o locker está disponível.
        senha_random (str): Senha gerada para retirada do pacote.
        apartamento (str): Número do apartamento associado à entrega.
    """

    def __init__(self, id:int, tamanho:str) -> None:
        """
        Inicializa um locker com seu identificador e tamanho.

        Args:
            id (int): Identificador único do locker.
            tamanho (str): Tamanho do locker ('P', 'M', 'G').
        """
        self.__id = id
        self.__tamanho = tamanho
        self.__disponivel = True
        self.__senha_random = None
        self.__apartamento = None

    @property
    def id(self):
        """Retorna o identificador do locker."""
        return self.__id

    def esta_disponivel(self):
        """Verifica se o locker está disponível."""
        return self.__disponivel

    def tamanho_certo(self, tamanho:str) -> bool:
        """
        Verifica se o locker é do tamanho desejado.

        Args:
            tamanho (str): Tamanho desejado ('P', 'M', 'G').

        Returns:
            bool: True se o tamanho corresponder, False caso contrário.
        """
        return self.__tamanho == tamanho

    def indisponibilizar(self, apartamento:str) -> None:
        """
        Torna o locker indisponível e associa a um apartamento.

        Args:
            apartamento (str): Número do apartamento.
        """
        self.__disponivel = False
        self.__apartamento = apartamento
        self.__senha_random = str(random.randint(1000, 9999))
        print("\nEnviando mensagem...")
        print(f"Nova entrega disponível! Apt: {apartamento} - Senha: {self.__senha_random}")

    def disponibilizar(self):
        """
        Torna o locker disponível novamente após a retirada do pacote.
        """
        self.__disponivel = True
        self.__apartamento = None
        self.__senha_random = None
        print("Locker Aberto. Retire sua encomenda.")
        input("Feche a porta e pressione Enter.")
        print("Locker liberado.")

    @property
    def senha_random(self):
        """Retorna a senha gerada para retirada do pacote."""
        return self.__senha_random

    @property
    def apartamento(self):
        """Retorna o número do apartamento associado ao locker."""
        return self.__apartamento

    @property
    def tamanho(self):
        """Retorna o tamanho do locker."""
        return self.__tamanho
