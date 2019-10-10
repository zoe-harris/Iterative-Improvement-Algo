# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence

from node import Node


class Portfolio:

    def __init__(self):
        self.investments = []

    def add_stock(self, new_investment):
        self.investments.append(new_investment)

    def fitness(self):
        fitness = 0

        for node in self.investments:
            fitness += (node.value * (node.percent_change * .01))

        return fitness

    def print_contents(self):

        print("| ", end='')
        for i in range(0, 5):
            s = self.investments[i]
            print(f'{s.company}: ${s.value:.2f} | ', end='')

        print("\n| ", end='')
        for i in range(5, 10):
            s = self.investments[i]
            print(f'{s.company}: ${s.value:.2f} | ', end='')

        print()
        print(f'The fitness of this portfolio is ${self.fitness():0.2f}')
