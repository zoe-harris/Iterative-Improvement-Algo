# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence
import math

class SimulatedAnnealing:

    def __init__(self, portfolio):
        self.portfolio = portfolio

"""
    def simulated_annealing(self):

        # schedule maps t to temperature
        temperature_decrease = 0.1
        schedule = lambda t: 1 - (t * temperature_decrease)

        # start with first company in portfolio
        current = self.portfolio.investments[0]

        for t in range(int(math.inf)):

            T = schedule(t)

            if T == 0:
                return current

            # next = random node from portfolio
            delta_E = next.change - current.change

            # If e^delta_E / T is less than 1, we choose the next investment & deal with T

            if (delta_E > 0) or (exp(delta_E / T) < 1):
                next.investment += (current.investment * 0.1)
                current.investment -= (current.investment * 0.1)
"""
"""

    def simulated_annealing(self):

        (given schedule is a mapping from time to T)
        temperature_decrease = 0.1
        schedule = lambda t : 1 - (t * temperature_decrease)

        for t = 0 to infinity:

            T = schedule(t)

            if T = 0:
                return current

            next = rand node from portfolio
            delta_E = next.change - current.change

            # If e^delta_E / T is less than 1, we choose the next investment & deal with T

            if (delta_E > 0) or (exp(delta_E / T) < 1):
                next.investment += (current.investment * 0.1)
                current.investment -= (current.investment * 0.1)

"""
