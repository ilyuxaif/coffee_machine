import sys
sys.path.append('../')
from implementation.coffee import Coffee


class CoffeeMachine:
	model: str = 'none'
	coffeeTypes: list = []
	sizes: list = []

	def cookCoffee(self, props):
		return Coffee(props.coffee, props.size, props.sugar)
