'''
1 - Darth Vader achou que seu exército de stormtrooper estava prendendo poucos rebeldes,
# então lhe contratou para desenvolver um programa que leia um conjunto indeterminado de
# número de refém presos por mês. Ao final da listagem informe o menor e o maior número
# de capturados, a média e o valor mais próximo a média. (2,0)
'''

class Numero:
    def ler_numeros(self):

        contador = 1
        lista = []
        opcao = 1

        while True:

            lista.append(int(input("Digite o %d° conjunto de presos " % contador)))
            opcao = int(input("Deseja continuar? 1 = Sim ou 0 = Não"))
            contador += 1

            if(opcao == 0 or opcao != 1):
                break

        return lista

    def encontrar_maior(self, lista):

        maior = lista[0]

        for encontrar_maior in lista:
            if encontrar_maior > maior:
                maior = encontrar_maior
        return maior

    def encontrar_menor(self, lista):

        menor = lista[0]

        for encontrar_menor in lista:
            if encontrar_menor < menor:
                menor = encontrar_menor
        return menor

    def somar_valores(self, lista):

        soma_total = 0.0

        for valor in lista:
            soma_total += valor
        return soma_total

    def calcular_media(self, soma, lista):

        media_numeros = soma / len(lista)
        return media_numeros

    def encontrar_aproximado(self, media, lista):

        aproximado = {value: abs(value - media) for value in lista}

        return min(aproximado, key=aproximado.get)

numero = Numero()

numeros_lista = numero.ler_numeros()

maior = numero.encontrar_maior(numeros_lista)
print("Maior conjunto de pressos: %d" %maior)

menor = numero.encontrar_menor(numeros_lista)
print("Menor  conjunto de pressos: %d" %menor)

soma = numero.somar_valores(numeros_lista)
print("Soma do conjunto de pressos: %.2f" %soma)

media = numero.calcular_media(soma, numeros_lista)
print("Média do conjunto de pressos: %.2f" %media)

aproximado = numero.encontrar_aproximado(media, numeros_lista)
print("Valor do conjunto de pressos aproximado da média : %.2f" %aproximado)