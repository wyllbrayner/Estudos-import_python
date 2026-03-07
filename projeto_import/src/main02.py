import calc

def main():
    a: int = 10
    b: int = 2
    zr:int = 0
    frase:str = "a"
    espaco:str = " "
    print(f'A soma          de {a} e "{espaco}" = {calc.soma(a, espaco)}')
    print(f'A soma          de {a} e "{frase}" = {calc.soma(a, frase)}')
    print(f'A soma          de {a} e {b}   = {calc.soma(a, b)}')
    print(f'A subtração     de {a} e {b}   = {calc.subtracao(a, b)}')
    print(f'A multiplicação de {a} e {b}   = {calc.multiplicacao(a, b)}')
    print(f'A divisão       de {a} e {b}   = {calc.divisao(a, b)}')
    print(f'A divisão       de {a} e {zr}   = {calc.divisao(a, zr)}')

if __name__ == '__main__':
    main()