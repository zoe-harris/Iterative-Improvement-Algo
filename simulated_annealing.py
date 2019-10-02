# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence
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
            next = self.portfolio.investments[next_index]

            # Calculate the value of Delta E
            delta_E = next.percent_change - current.percent_change

            # If (Delta E > 0) or if [(e^(Delta E) / T) < 1], choose the next investment
            if (delta_E > 0) or (exp(delta_E / T) < 1):
                self.reinvest(next, current)