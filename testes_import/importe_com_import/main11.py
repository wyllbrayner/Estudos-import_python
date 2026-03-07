import testes11

def main():
    print(f"estou na main e me chamo: {__name__}")
    testes11.eu_sou.eu_sou_teste01()
    testes11.eu_sou.eu_sou_teste02()
    print(testes11.__file__)


if __name__ == "__main__":
    main()