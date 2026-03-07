from typing import Any

def validar_se_inteiro(a: Any) -> bool:
    """
    Parâmetros: a, de qualquer tipo.
    Retorno: bool com o resultado da validação.
    Validações:
        Não aplicado.
    """
    return isinstance(a, int)

def validar_se_string(a: Any) -> bool:
    """
    Parâmetros: a, de qualquer tipo.
    Retorno: bool com o resultado da validação.
    Validações:
        Não aplicado.
    """
    return isinstance(a, str)

def validar_se_zero(a: Any) -> bool:
    """
    Parâmetros: a, de qualquer tipo.
    Retorno: bool com o resultado da validação.
    Validações:
        Não aplicado.
    """
    if validar_se_inteiro(a):
        if a == 0:
            return True
        else:
            return False
    else:
        False
