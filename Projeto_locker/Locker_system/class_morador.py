
class Usuario_Master:
    """
    Classe base para representar usuários do sistema.

    Atributos:
        nome (str): Nome do usuário.
        apartamento (str): Número do apartamento do usuário.
        senha_universal (str): Senha exclusiva do síndico.
    """

    def __init__(self, nome: str, apartamento: str, senha: str = "0000") -> None:
        """
        Inicializa um usuário mestre no sistema.

        Args:
            nome (str): Nome do usuário.
            apartamento (str): Número do apartamento do usuário.
            senha (str, opcional): Senha universal, usada apenas pelo síndico.
        """
        self.__nome = nome
        self._apartamento = apartamento
        if isinstance(self, Sindico):
            self.__senha_universal = senha
        # if type(self) is Sindico:
        #     self.__senha_universal = senha


class Sindico(Usuario_Master):
    """
    Classe que representa o síndico do condomínio, herdando de `Usuario_Master`.
    """

    def __init__(self, nome: str, apartamento: str, senha: str = "0000") -> None:
        """
        Inicializa um síndico do sistema.

        Args:
            nome (str): Nome do síndico.
            apartamento (str): Número do apartamento do síndico.
            senha (str, opcional): Senha universal do síndico.
        """
        super().__init__(nome, apartamento)


class Morador(Usuario_Master):
    """
    Classe que representa um morador do condomínio, herdando de `Usuario_Master`.

    Atributos:
        senha_geral (str): Senha exclusiva do morador.
    """

    def __init__(self, nome: str, apartamento: str, senha_geral: str) -> None:
        """
        Inicializa um morador do sistema.

        Args:
            nome (str): Nome do morador.
            apartamento (str): Número do apartamento do morador.
            senha_geral (str): Senha exclusiva do morador.
        """
        super().__init__(nome, apartamento)
        self.__senha_geral = senha_geral

    @property
    def apt(self) -> str:
        """Retorna o apartamento associado ao morador."""
        return self._apartamento

    @apt.setter
    def apt(self, apt: str) -> None:
        """Define o apartamento do morador."""
        self._apartamento = apt
