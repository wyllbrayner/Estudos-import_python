from calc import soma, subtracao, multiplicacao, divisao

def main():
    a: int = 10
    b: int = 2
    zr:int = 0
    frase:str = "a"
    espaco:str = " "
    print(f'A soma          de {a} e "{espaco}" = {soma(a, espaco)}')
    print(f'A soma          de {a} e "{frase}" = {soma(a, frase)}')
    print(f'A soma          de {a} e {b}   = {soma(a, b)}')
    print(f'A subtração     de {a} e {b}   = {subtracao(a, b)}')
    print(f'A multiplicação de {a} e {b}   = {multiplicacao(a, b)}')
    print(f'A divisão      de {a} e {b}    = {divisao(a, b)}')
    print(f'A divisão      de {a} e {zr}    = {divisao(a, zr)}')

if __name__ == '__main__':
    main()