import random


def get_pontos_perdidos(p, ns, c):
    return p - abs(ns - c)


def jogar():
    print("*" * 12)
    print("Bem vindo!!!")
    print("*" * 12)

    numero_secreto = random.randrange(1, 101)
    mensagem_input = "Digite um número entre 1 e 100: "
    pontos_max = 1000
    pontos_usuario = pontos_max

    print("Qual nível de dificuldade?")
    print("(1) Fácil - (2) Médio - (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if nivel == 1:
        total_tentativas = 20
    elif nivel == 2:
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa atual é a {} de {}".format(rodada, total_tentativas))
        chute = int(input(mensagem_input))

        while chute < 1 or chute > 100:
            chute = int(input(f"Você deve digitar um número entre 1 e 100.\n{mensagem_input}"))

        acertou = numero_secreto == chute
        chute_maior = chute > numero_secreto

        if acertou:
            print(f"Você acertou! Seus pontos foram {pontos_usuario} de {pontos_max}.")
            break
        elif chute_maior:
            print("Você errou! Seu chute foi maior que o número secreto.")
            pontos_usuario = get_pontos_perdidos(pontos_usuario, numero_secreto, chute)
        else:
            print("Você errou! Seu chute foi menor que o número secreto.")
            pontos_usuario = get_pontos_perdidos(pontos_usuario, numero_secreto, chute)

    print("Fim de jogo")


if __name__ == "__main__":
    jogar()
