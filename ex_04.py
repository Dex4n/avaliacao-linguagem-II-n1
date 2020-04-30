#4 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:(2,0)

while True:
    tabuada = int(input("Você deseja gerar tabuada de qual número? (De 1 até 10): "))

    if (tabuada < 1 or tabuada > 10):
        print("Você digitou um valor inválido!")

    else:
        contador = 0

        print("Tabuada de %d:" % (tabuada))

        while (contador < 11):

            print("%d X %d = %d" % (tabuada, contador, tabuada * contador))
            contador += 1
    break