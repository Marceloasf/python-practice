def jogar():
    print("*" * 12)
    print("Bem vindo!!!")
    print("*" * 12)

    palavra_secreta = "banana"
    enforcou = False
    acertou = False
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = input("Digite uma letra: ")

        index = 0
        for letra in palavra_secreta:
            if chute.strip().upper() == letra.strip().upper():
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim de jogo")


if __name__ == "__main__":
    jogar()
