from valid import validar_se_zero, valiacao_se_dois_inteiros

def soma(a: int, b: int) -> int:
    """
    Parâmetros: a e b, ambos do tipo inteiro
    Retorno: resultado da operação, se possível, ou zero
    Validações:
        Verifica se ambos os parametros recebidos são do tipo inteiro.
        Caso a validação realizada falhe, o retorno será zero.
    """
    if valiacao_se_dois_inteiros(a, b):
        return a + b
    else:
        return 0

def subtracao(a: int, b: int) -> int:
    """
    Parâmetros: a e b, ambos do tipo inteiro
    Retorno: resultado da operação, se possível, ou zero
    Validações:
        Verifica se ambos os parametros recebidos são do tipo inteiro.
        Caso a validação realizada falhe, o retorno será zero.
    """
    if valiacao_se_dois_inteiros(a, b):
        return a - b
    else:
        return 0

def multiplicacao(a: int, b: int) -> int:
    """
    Parâmetros: a e b, ambos do tipo inteiro
    Retorno: resultado da operação, se possível, ou zero
    Validações:
        Verifica se ambos os parametros recebidos são do tipo inteiro.
        Caso a validação realizada falhe, o retorno será zero.
    """
    if valiacao_se_dois_inteiros(a, b):
        return a * b
    else:
        return 0

def divisao(a: int, b: int) -> int:
    """
    Parâmetros: a e b, ambos do tipo inteiro
    Retorno: resultado da operação, se possível, ou zero
    Validações:
        Verifica se ambos os parametros recebidos são do tipo inteiro.
        Verifica se o segundo parâmetro é zero.
        Caso alguma das validações realizadas falhe, o retorno será zero.
    """
    if valiacao_se_dois_inteiros(a, b):
        if validar_se_zero(b):
            return 0
        else:
            return a / b
    else:
        return 0
