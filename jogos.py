import forca
import adivinhacao


def escolhe_jogo():
    print("*" * 12)
    print("Escolha o seu jogo!")
    print("*" * 12)

    print("(1) Forca - (2) Adivinhação")

    jogo_escolhido = int(input("Qual jogo? "))

    if jogo_escolhido == 1:
        print("**** Jogo da forca ****")
        forca.jogar()
    elif jogo_escolhido == 2:
        print("**** Jogo de adivinhação ****")
        adivinhacao.jogar()


if __name__ == "__main__":
    escolhe_jogo()
