import testes10.eu_sou

def main():
    print(f"estou na main e me chamo: {__name__}")
    testes10.eu_sou.eu_sou_teste01()
    testes10.eu_sou.eu_sou_teste02()
    print(testes10.__file__)


if __name__ == "__main__":
    main()