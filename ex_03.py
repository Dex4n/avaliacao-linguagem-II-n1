#3 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido
# e continue pedindo até que o usuário informe um valor válido.(2,0)

while True:
    auxColetaNota = int(input("Digite uma nota de 0 até 10: "))
    if (auxColetaNota < 0 or auxColetaNota > 10):
        print("Você digitou um valor inválido!")

    else:
        print("Você digitou um valor válido!")
        break