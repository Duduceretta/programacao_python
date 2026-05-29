class CidadeClima:
    """
    Classe que representa as condições climáticas de uma cidade específica.
    """

    def __init__(self, nome: str, temperatura: float, umidade: int, condicao: str):
        self._nome = nome
        self._temperatura = temperatura
        self._umidade = umidade
        self._condicao = condicao

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def temperatura(self) -> float:
        return self._temperatura

    @property
    def umidade(self) -> int:
        return self._umidade

    @property
    def condicao(self) -> str:
        return self._condicao

    def __str__(self) -> str:
        """
        Sobrescreve o método __str__ para retornar os dados formatados.
        """
        largura_bloco = 35
        linha_divisoria = "=" * largura_bloco
        
        return (
            f"\n{linha_divisoria}\n"
            f" 🌍 CIDADE: {self._nome.upper()}\n"
            f"{linha_divisoria}\n"
            f" 🌡️ Temperatura: {self._temperatura:.1f}°C\n"
            f" 💧 Umidade:     {self._umidade}%\n"
            f" ☁️ Condição:    {self._condicao.capitalize()}\n"
            f"{linha_divisoria}"
        )