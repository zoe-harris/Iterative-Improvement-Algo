# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence
# Rachel Note: MAYBE copy nodes
from math import *
import random
from portfolio import Portfolio
from node import Node

class SimulatedAnnealing:

    def __init__(self, portfolio):
        self.portfolio = portfolio

    def reinvest(self, next, current):
        next.value += (current.value * 0.1)
        current.value -= (current.value * 0.1)

    def simulated_annealing(self):

        # schedule maps t to temperature
        temperature_decrease = 0.1
        schedule = lambda t: 1 - (t * temperature_decrease)

        # start with first company in portfolio
        current = self.portfolio.investments[0]

        # Run simulated annealing until temperature reaches 0
        for t in range(1, int(inf)):

            # Use schedule function to get value of T
            T = schedule(t)

            # When T reaches zero, break from loop
            if T == 0:
                return current

            # next = random node from portfolio
            next_index = random.randrange(0, 10)
            # Next node = random from all neighbors
            # Make all 90 neighbors, put it in a list, randomly select. OR randomly index x & y -- faster
            next = self.portfolio.investments[next_index]

            # Calculate the value of Delta E
            # Rachel Note: delta_E should compare the fitnesses. Randomly selected neighbor fitness - current fitness
            delta_E = next.percent_change - current.percent_change

            # If (Delta E > 0) or if [(e^(Delta E) / T) < 1], choose the next investment
            if (delta_E > 0) or random.random() < (exp(delta_E / T)):
                self.reinvest(next, current)
