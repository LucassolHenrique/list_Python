
class Usuario_Master:
    def __init__(self, nome: str, apartamento: str, senha: str = "0000") -> None:
        self.__nome = nome
        self._apartamento = apartamento
        if isinstance(self, Sindico):
            self.__senha_universal = senha
        # if type(self) is Sindico:
        #     self.__senha_universal = senha


class Sindico(Usuario_Master): 
    def __init__(self, nome: str, apartamento: str, senha: str = "0000") -> None:
        super().__init__(nome, apartamento)


class Morador(Usuario_Master):

    def __init__(self, nome: str, apartamento: str, senha_geral: str) -> None:
        super().__init__(nome, apartamento)
        self.__senha_geral = senha_geral

    @property
    def apt(self) -> str:
        return self._apartamento

    @apt.setter
    def apt(self, apt: str) -> None:
        self._apartamento = apt
