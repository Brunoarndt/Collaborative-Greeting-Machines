def exibir_saudacao():
    print("--- Máquina de Saudações Colaborativa ---")
    print("Olá! Seja bem-vindo(a)!")
    print("---------------------------------------")

def saudacao_personalizada():
    print("Enter your language (english or portuguese):")
    language=input()
    if language=="english":
        print("Enter your name:")
        name = input()
        print(f"Hello {name}")
    if language=="portuguese":
        print("Digite seu nome:")
        name = input()
        print(f"Olá {name}")

def main():
    exibir_saudacao()
    saudacao_personalizada()
    frase_inspiradora()
    # Adicione suas funções de saudação aqui!
    # Exemplo:
    # saudacao_manha()
    # frase_inspiradora()

if __name__ == "__main__":
    main()
    
