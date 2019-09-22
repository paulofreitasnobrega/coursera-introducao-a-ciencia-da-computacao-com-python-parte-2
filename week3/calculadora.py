# Week 3 - Exercícios em Vídeo
# Exercício - Primeira Classes

# Criar sua primeira classe python

#Aluno: Paulo Freitas Nobrega

# Recebe dois números de entrada e executa as operações matemáticas (básicas).
# Soma, Multiplicação, Divisão e Subtração
class Calculadora:
	# Método construtor
	def __init__(self, valor1, valor2):
		self.a = valor1
		self.b = valor2

	# Método soma
	def soma(self):
		return self.a + self.b

	# Método subtração
	def subtrai(self):
		return self.a - self.b

	# Método multiplicação
	def multiplica(self):
		return self.a * self.b

	# Método divisão
	def divide(self) :
		return self.a / self.b

# Função de entrada do programa
def main():
	calc = Calculadora(9, 3)
	print("Soma: {}".format(calc.soma()))
	print("Subtrai: {}".format(calc.subtrai()))
	print("Multiplica: {}".format(calc.multiplica()))
	print("Divide: {}".format(calc.divide()))

main()
