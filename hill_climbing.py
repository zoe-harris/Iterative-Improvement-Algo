# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence
import random

ITERATION_COUNT = 4
CHECK_COUNT = 3


class HillClimbing:
    def __init__(self, portfolio):
        self.portfolio = portfolio
        self.best_portfolio = 0
        self.maximum_fitness = 1
        self.same_max_reached = 0
        self.max_unchanged = 0
        self.curr_max_fitness = 1

    def reinvest(self, next, current):
        next.value += (current.value * 0.1)
        current.value -= (current.value * 0.1)

    def random_restart(self):
        money = 100000

        # The for-loop ensures each value of the portfolio is changed. A random number is rolled for each investment to
        # determine how much money it receives. At the end, the left over money is divided evenly and split amongst
        # the investments
        for x in range(len(self.portfolio.investments)):
            value = random.randrange(5000, 15000)
            while value > money:
                value = random.randrange(5000, 15000)
            self.portfolio.investments[x].value = value
            money -= value

        if money != 0:
            val = money / 10
            for x in range(len(self.portfolio.investments)):
                self.portfolio.investments[x].value += val

    def hill_climbing(self):
        curr_maximum = 0
        same_max_reached = 0  # This determines if we've peaked at the same point
        max_unchanged = 0  # This determines if we have yet to beat the current maximum

        curr_node, neighbor_node, counter = 0

        # We will run Hill Climbing w/ Random Restart 4 times
        while counter < ITERATION_COUNT:

            if counter > 0:
                self.random_restart()

            # This loop runs the current iteration of hill climbing
            while (max_unchanged <= CHECK_COUNT) or (same_max_reached <= CHECK_COUNT):

                # This double for-loop searches for the best move at our current position.
                # Outer loop keeps track of the 'current' node
                # Rachel Notes
                # Neighbor = The state that exists AFTER a move.
                # Neighbor = [c1 = 10k, c2 = 5k, c3 = 3k], [c1 = 9k, c2 = 6k, c3 = 3k]
                # Only save the best neighbor
                for x in range(len(self.portfolio.investments)):
                    curr_node = self.portfolio.investments[x]

                    # Inner loop compares our current node to each neighbor move & reinvests as needed
                    for y in range(len(self.portfolio.investments)):
                        next_node = self.portfolio.investments[y]

                        # If company 1 made less than company 2, reinvest
                        if curr_node.percent_change < neighbor_node.percent_change:
                            self.reinvest(neighbor_node, curr_node)

                new_fitness = self.portfolio.fitness()

                # If our current maximum value < new fitness, change the fitness & reset values to 0
                if curr_maximum < new_fitness:
                    curr_maximum = self.portfolio.fitness()
                    same_max_reached = 0
                    max_unchanged = 0

                # If we have yet to find a new peak in this run, increment
                if curr_maximum > new_fitness:
                    max_unchanged += 1

                # If we have found the same maximum, increment
                if curr_maximum == new_fitness:
                    same_max_reached += 1

            # If our current maximum is greater than the best maximum we've found, save it
            if curr_maximum > self.maximum_fitness:
                self.maximum_fitness = curr_maximum
                self.best_portfolio = self.portfolio

            curr_maximum, max_unchanged, same_max_reached = 0
            counter += 1

"""

    def hill_climbing(self):

        portfolio = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9]
        maximum = 0  # fitness
        same_max_reached = 0
        max_unchanged = 0

        while same_max_reached < 3 and max_unchanged < 3:

            if curr_node.change < neighbor.change:
                neighbor.investment += (curr_node.investment * 0.1)
                curr_node.investment -= (curr_node.investment * 0.1)

            new_gains = total_gains(portfolio)

            current_maximum is the maximum of the current iteration
            maximum is the highest reached fitness thus far

            if new_gains > current_maximum:
                current_maximum = new_gains

            if current_maximum == maximum:
                same_max_reached += 1

            if current_maximum < maximum
                max_unchanged += 1

            if current_maximum > maximum:
                maximum = current_maximum
                same_max_reached = 0
                max_unchanged = 0

            curr_node = neighbor

"""
