import random

class Locker:
    def __init__(self, id:int, tamanho:str) -> None:

        self.__id = id
        self.__tamanho = tamanho
        self.__disponivel = True
        self.__senha_random = None
        self.__apartamento = None
    
    @property 
    def id(self): 
        return self.__id

    def esta_disponivel(self):
        return self.__disponivel

    def tamanho_certo(self, tamanho:str) -> bool:
        return self.__tamanho == tamanho

    def indisponibilizar(self, apartamento:str) -> None:

        self.__disponivel = False
        self.__apartamento = apartamento
        self.__senha_random = str(random.randint(1000, 9999))
        print("\nEnviando mensagem...")
        print(f"Nova entrega disponível! Apt: {apartamento} - Senha: {self.__senha_random}")

    def disponibilizar(self):

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
