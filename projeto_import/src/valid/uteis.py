from .validacao import validar_se_inteiro
from typing import Any

def valiacao_se_dois_inteiros(a: Any, b: Any) -> bool:
    """
    Parâmetros: a e b, de qualquer tipo.
    Retorno: bool com o resultado da validação.
    Validações:
        Não aplicado.
    """
    return validar_se_inteiro(a) and validar_se_inteiro(b)
