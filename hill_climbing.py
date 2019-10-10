# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence
import copy
import random

ITERATION_COUNT = 10
CHECK_COUNT = 5


class HillClimbing:
    def __init__(self, portfolio):
        # These variables save the final, or best, results of hill climbing
        self.best_portfolio = portfolio
        self.maximum_fitness = self.best_portfolio.fitness()

        # This variable keeps track of that iteration's portfolio & maximum
        self.portfolio = portfolio

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
                val = random.randint(0, 10)
                self.portfolio.investments[val].value += money
            else:
                val = money / 10
                for x in range(len(self.portfolio.investments)):
                    self.portfolio.investments[x].value += val
        #self.portfolio.print_contents()
        return self.portfolio.fitness()

    def hill_climbing(self):
        # The following variables keep track of the max & portfolio of the current iteration while we are looping
        curr_fitness = self.portfolio.fitness()
        curr_portfolio = copy.deepcopy(self.portfolio)

        # These variables help ensure us if we have found a peak in the hill
        same_max_reached = 0  # This determines if we've peaked at the same point
        max_unchanged = 0  # This determines if we have yet to beat the current maximum

        curr_node = 0
        next_node = 0
        counter = 0

        # We will run Hill Climbing w/ Random Restart 4 times
        while counter < ITERATION_COUNT:
            if counter > 0:
                curr_fitness = self.random_restart()

            # This loop runs the current iteration of hill climbing
            while (max_unchanged <= CHECK_COUNT) and (same_max_reached <= CHECK_COUNT):
                # print("Find new move.\nmax_unchanged = ", max_unchanged, "\nsame_max_reached = ", same_max_reached)
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
                                # same_max_reached = 0
                                # max_unchanged = 0

                # If we have yet to find a new peak in this run, increment
                if curr_fitness < self.maximum_fitness:
                    max_unchanged += 1

                # If we have found the same maximum, increment
                if curr_fitness == self.maximum_fitness:
                    same_max_reached += 1

            # If our current maximum is greater than the best maximum we've found, save it
                if curr_fitness > self.maximum_fitness:
                    print("\n\ncounter = ", counter, "\nmax_unchanged = ", max_unchanged, "\nsame_max_reached = ",
                          same_max_reached)
                    print("Current Portfolio:")
                    curr_portfolio.print_contents()
                    print("Best Portfolio:")
                    self.best_portfolio.print_contents()
                    print("\n\n")
                    self.maximum_fitness = curr_fitness
                    self.best_portfolio = curr_portfolio

                else:
                    print("\n\ncounter = ", counter, "\nmax_unchanged = ", max_unchanged, "\nsame_max_reached = ",
                          same_max_reached)
                    print("Current Portfolio:")
                    curr_portfolio.print_contents()
                    print("Best Portfolio:")
                    self.best_portfolio.print_contents()

            max_unchanged = 0
            same_max_reached = 0
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
