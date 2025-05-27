import datetime

def exibir_saudacao():
    print("--- Máquina de Saudações Colaborativa ---")
    print("Olá! Seja bem-vindo(a)!")
    print("---------------------------------------")

def saudacao_periodo():
    print("++++++++++++++")
    datetime.datetime.now().hour #pega o valor da hora atual
    a = 33
    b = 200
    c = 400
    if a >= b >= c:
        print("BOM DIA!!!")
    elif a == b:
        print("BOA TARDE!!!")
    else:
        print("BOA NOITE!!!")


def main():
    exibir_saudacao()
    # Adicione suas funções de saudação aqui!
    # Exemplo:
    saudacao_periodo()
    # saudacao_manha()
    # frase_inspiradora()

if __name__ == "__main__":
    main()