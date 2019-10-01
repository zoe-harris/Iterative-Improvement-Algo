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
            fitness += (node.num_invested - 10000)

        return fitness

    def print_contents(self):

        for s in self.investments:
            print(s.company + ": $" + s.num_invested)
