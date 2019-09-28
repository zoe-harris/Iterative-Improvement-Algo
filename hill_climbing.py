# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence

"""

    def __init__(portfolio):
        self.portfolio = portfolio
        self.optimized_list = None

    def total_gains(self, portfolio):
        ...return total gains of current portfolio

    portfolio = [i0, i1, i2, i3, i4, i5, i6, i7, i8, i9]
    maximum = 0  # fitness
    same_max_reached = 0
    max_unchanged = 0

    while same_max_reached < 3 and max_unchanged < 3:

        if curr_node.gain < neighbor.gain:
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
