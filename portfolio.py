# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence

from node import Node

class Portfolio:

    def __init__(self):
        self.stocks = []

    def add_stock(self, new_stock):
        self.stocks.append(new_stock)

    def fitness(self):
        fitness = 0

        for node in self.stocks:
            fitness += (node.invested - 10000)

        return fitness
