# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence
import copy
import random

ITERATION_COUNT = 4
CHECK_COUNT = 3


class HillClimbing:
    def __init__(self, portfolio):
        # These variables save the final, or best, results of hill climbing
        self.best_portfolio = portfolio
        self.maximum_fitness = self.best_portfolio.fitness()

        # This variable keeps track of that iteration's portfolio & maximum
        self.portfolio = portfolio
        self.fitness = self.portfolio.fitness()

        self.same_max_reached = 0  # This determines if we've peaked at the same point
        self.max_unchanged = 0  # This determines if we have yet to beat the current maximum

    def reinvest(self, next, current):
        next.value += (current.value * 0.1)
        current.value -= (current.value * 0.1)

    def random_restart(self):
        money = 100000
        # The for-loop ensures each value of the portfolio is changed. A random number is rolled for each investment to
        # determine how much money it receives. At the end, the left over money is divided evenly and split amongst
        # the investments
        for x in range(len(self.portfolio.investments)):
            if x == 9:
                self.portfolio.investments[x].value = money
            else:
                value = random.randrange(7500, 15000)
                while value > money and (money != 0):
                    num = 10 - x - 1
                    value = random.uniform(0, (money / num))
                self.portfolio.investments[x].value = value
                money -= value

        if money != 0:
            if money < 1000:
                val = random.randint(0, 9)
                self.portfolio.investments[val].value += money
            else:
                val = money / 10
                for x in range(len(self.portfolio.investments)):
                    self.portfolio.investments[x].value += val
        self.fitness = self.portfolio.fitness()

    def hill_climbing(self):
        # The following variables keep track of the max & portfolio of the current iteration while we are looping
        curr_fitness = self.portfolio.fitness()
        curr_portfolio = copy.deepcopy(self.portfolio)

        # These variables help ensure us if we have found a peak in the hill
        same_max_reached = 0  # This determines if we've peaked at the same point
        max_unchanged = 0  # This determines if we have yet to beat the current maximum

        counter = 0

        # We will run Hill Climbing w/ Random Restart until we cannot beat the global maximum
        while self.max_unchanged <= CHECK_COUNT and self.same_max_reached <= CHECK_COUNT:
            if counter > 0:
                curr_fitness = self.fitness

            # This loop runs the current iteration of hill climbing
            while (max_unchanged <= CHECK_COUNT) and (same_max_reached <= CHECK_COUNT):

                # Outer loop keeps track of the 'current' node, inner loop compares our current node to each neighbor
                for x in range(len(self.portfolio.investments)):
                    for y in range(len(self.portfolio.investments)):
                        if x != y:

                            # If x != create a copy of the current portfolio, select 2 nodes, reinvest, check
                            # if better than what we have, increment as needed, continue
                            neighbor_portfolio = copy.deepcopy(self.portfolio)
                            curr_node = neighbor_portfolio.investments[x]
                            next_node = neighbor_portfolio.investments[y]
                            self.reinvest(next_node, curr_node)
                            neighbor_fitness = neighbor_portfolio.fitness()

                            # If our current maximum value < new fitness, change the fitness & reset values to 0
                            if curr_fitness < neighbor_fitness:
                                curr_fitness = neighbor_fitness
                                curr_portfolio = neighbor_portfolio

                # The following if statements determine if the best move beats our CURRENT maximum
                # If we have yet to find a new peak in this run, increment
                if round(curr_fitness, 2) < round(self.fitness, 2):
                    max_unchanged += 1

                # If we have found the same maximum, increment
                if round(curr_fitness, 2) == round(self.fitness, 2):
                    same_max_reached += 1

                if round(curr_fitness, 2) > round(self.fitness, 2):
                    self.fitness = curr_fitness
                    self.portfolio = curr_portfolio

            # The following if statements determine if the CURRENT maximum beats the GLOBAL maximum
            # If we have yet to find a new peak in this run, increment
            if round(self.fitness, 2) < round(self.maximum_fitness, 2):
                self.max_unchanged += 1

            # If we have found the same maximum, increment
            if round(self.maximum_fitness, 2) == round(self.fitness, 2):
                self.same_max_reached += 1

            # If our current maximum is greater than the best maximum we've found, save it
            if round(self.fitness, 2) > round(self.maximum_fitness, 2):
                self.maximum_fitness = self.fitness
                self.best_portfolio = copy.deepcopy(self.portfolio)
                self.same_max_reached = 0
                self.max_unchanged = 0

            max_unchanged = 0
            same_max_reached = 0