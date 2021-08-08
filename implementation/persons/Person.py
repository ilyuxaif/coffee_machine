from abc import ABC, abstractmethod
import sys
import random
sys.path.append('../')
from implementation.machines.CoffeeMachine import CoffeeMachine
from implementation.machines.CoffeeMachine import Coffee

class Person:
    coffee_wish: str = None
    sugar_wish: int = None
    name: str = None
    coffee: dict = None

    def chooseCoffee(self, machine: CoffeeMachine):
        coffee = ''
        size = ''

        if self.coffee_wish in machine.coffeeTypes:
            coffee = self.coffee_wish
        else:
            coffee = machine.coffeeTypes[random.randint(0, len(machine.coffeeTypes))]

        size = machine.sizes[random.randint(0, len(machine.sizes))]

        self.coffee = {
            'coffee': coffee,
            'size': size,
            'sugar': self.sugar_wish}

    def startCoffeeMachine(self, machine: CoffeeMachine):
        coffee_cup = machine.cookCoffee(self.coffee)
        self.takeAwayCoffee(coffee_cup)

    def takeAwayCoffee(self, coffee: Coffee):
        print(f'{self.name} is happy with {coffee.type}!')