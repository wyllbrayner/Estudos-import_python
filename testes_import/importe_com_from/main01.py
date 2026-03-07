from testes01 import eu_sou

def main():
    print(f"estou na main e me chamo: {__name__}")
    eu_sou.eu_sou_teste01()
    eu_sou.eu_sou_teste02()
    print(eu_sou.__file__)

if __name__ == "__main__":
    main()