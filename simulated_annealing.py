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

            # If e^delta_E / T is less than 1, we choose the next investment & deal with T
            if (delta_E > 0) or (exp(delta_E / T) < 1):
                next.investment += (current.investment * 0.1)
                current.investment -= (current.investment * 0.1)



"""