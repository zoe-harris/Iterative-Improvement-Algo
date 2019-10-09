# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence
# Rachel Note: MAYBE copy nodes
from math import *
from copy import *
import random
from portfolio import Portfolio


class SimulatedAnnealing:

    def __init__(self, portfolio):
        self.portfolio = portfolio

    # method invests 10% of 'current' stock into 'next' stock
    def reinvest(self, p, next_index, curr_index):
        p.investments[next_index].value += (p.investments[curr_index].value * 0.1)
        p.investments[curr_index].value -= (p.investments[curr_index].value * 0.1)

    # method gets the fitness of a hypothetical portfolio in which
    # 10% of 'current' stock has been invested in the 'next' stock
    def next_fitness(self, next_index, curr_index):
        temp = Portfolio()
        temp.investments = deepcopy(self.portfolio.investments)
        self.reinvest(temp, next_index, curr_index)
        return temp.fitness()

    # method optimizes an investment portfolio using simulated annealing
    def simulated_annealing(self):

        # schedule maps t to temperature
        temperature_decrease = -0.0001
        schedule = lambda t: 1 + (t * temperature_decrease)

        # choose random company to start with
        curr_index = random.randrange(0, 10)
        current = self.portfolio.investments[curr_index]

        # Initialize counting variable t
        t = 0

        # Run simulated annealing until temperature reaches 0
        while True:

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

            curr_fitness = self.portfolio.fitness()
            new_fitness = self.next_fitness(next_index, curr_index)
            delta_E = new_fitness - curr_fitness

            # Reinvest if delta E > 0, or with probability of e^(delta E / T)
            if delta_E > 0 or random.random() < exp(delta_E / T):
                self.reinvest(self.portfolio, next_index, curr_index)
                current = next

            t += 1
