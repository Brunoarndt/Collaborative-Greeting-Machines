import datetime
import random

def saudacao_periodo():
    datetime.datetime.now().hour #pega o valor da hora atual
    a = 33
    b = 200
    c = 400
    if a >= b >= c:
        print("a está entre b e c")
    elif a == b:
        print("a e b são iguais")
    else:
        print("c é maior do que todos")


def frase_inspiradora():
    array = [
        "string 1",
        "string 2"
    ]
    print(random.choice(array))


def saudacao_personalizada():
    print("Enter your name:")
    name = input()
    print(f"Hello {name}")

