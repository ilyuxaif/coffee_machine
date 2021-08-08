class CoffeeMachine:
	americano: bool

	def __init__(self, model):
		self.americano = True


class Posuda:
	def svaritPelmeni(self):
		print('varim pelmeni')


class Kastryyla(Posuda):
	def svaritMyaso(self):
		print('varim myaso')


class Chainik(Posuda):
	def svaritChai(self):
		print('varim chai')


chainik = Chainik()

chainik.svaritPelmeni()