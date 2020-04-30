#2 - Crie um classe Funcionário com os atributos nome, idade e salário. Deve ter  um método aumenta_salario.
# Crie duas subclasses da classe funcionário, programador  e analista, implementando o método nas duas subclasses.
# Para o programador some ao atributo salário mais 20 e ao analista some ao salário mais 30,  mostrando na tela o valor.
# Depois disso, crie uma classe de testes instanciando os objetos programador e analista e
# chame o método aumenta_salario de cada um.(2,0)



class Funcionario:

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._idade = cpf
        self._salario = salario

    def aumentarSalario(self, aumento):

        self._salario += aumento
        return self._salario

class Programador(Funcionario):

    def aumentarSalario(self):
        return super().aumentarSalario(20)

class Analista(Funcionario):

    def aumentarSalario(self):
        return super().aumentarSalario(30)

class Teste:
    programador = Programador('Alexandre Marino Casagrande', 22, 500.00)
    print("Salário do programador aumentado: ", programador.aumentarSalario())

    analista = Analista('Fulano de Tal', 22, 250.00)
    print("Salário do analista aumentado: ", analista.aumentarSalario())

main = Teste()

print("Dados do programador - Nome: {0}, idade: {1} e salário com aumento: {2}.".format(main.programador._nome, main.programador._idade, main.programador._salario))
print("Dados do analista - Nome: {0}, idade: {1} e salário com aumento: {2}.".format(main.analista._nome, main.analista._idade, main.analista._salario))


