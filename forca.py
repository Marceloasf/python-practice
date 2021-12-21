def jogar():
    print("*" * 12)
    print("Bem vindo!!!")
    print("*" * 12)

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for _ in palavra_secreta]

    vidas = 5
    perdeu = False
    venceu = False

    print(letras_acertadas)

    while not perdeu and not venceu:
        chute = input("Digite uma letra: ").strip().upper()

        index = 0
        if chute in palavra_secreta:
            for letra in palavra_secreta:
                if chute == letra:
                    letras_acertadas[index] = letra
                index += 1
        else:
            vidas -= 1

        perdeu = vidas == 0
        venceu = "_" not in letras_acertadas
        print(f"Você tem {vidas} vidas!")
        print(letras_acertadas)

    if venceu:
        print("Você venceu :)")
    else:
        print("Você perdeu :(")
    print("Fim de jogo")


if __name__ == "__main__":
    jogar()
