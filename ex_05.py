'''
5 - Duas amigas estabeleceram o código abaixo para que suas mensagens não fossem lidas pelas demais pessoas.
0 12 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
' ' a b  c d e f g h  i j k l    m n o p q r    s t u v w x y   z
Observe que cada letra equivale a um número entre 1 e 26 e o espaço ao 0. Faça um método para "traduzir", que recebe uma lista com uma mensagem (secreta) e "traduz" a sequência armazenada em uma lista.
'''

import string

alfabeto = list(string.ascii_lowercase)

numeros = list(range(26))

letras = list(string.ascii_lowercase)
letras.insert(0, ' ')

numeros = list(range(0, 27))

frase = input("Digite uma frase: ").lower()

for i in frase:
    print(numeros[letras.index(i)], end='')