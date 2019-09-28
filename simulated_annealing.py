# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence

"""

    def simulated_annealing(self):

        (given schedule is a mapping from time to T)

        while True:

            T = schedule[T]
            if T = 0:
                return current

            next = rand node from portfolio
            delta_E = next.change - current.change

            if delta_E > 0:
                next.investment += (current.investment * 0.1)
                current.investment -= (current.investment * 0.1)

"""