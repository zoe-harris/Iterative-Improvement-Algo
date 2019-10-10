# Zoe Harris & Rachel Lewis
# Programming Assignment 2
# CSCE405 Artificial Intelligence

from node import Node
from portfolio import Portfolio
from simulated_annealing import SimulatedAnnealing
from hill_climbing import HillClimbing

# Dictionary keys are DJIA companies, values are the change in value of
# the companies' respective stocks
dow_jones = {
                'MMM': 4.46, 'AXP': -0.36, 'AAPL': 6.47,
                'BA': 6.36, 'CAT': -1.23, 'CVX': 1.53,
                'CSCO': 4.25, 'KO': -1.43, 'DIS': -4.8,
                'DOW': 10.72, 'XOM': 5.64, 'GS': 4.28,
                'HD': 3.55, 'IBM': 7.97, 'INTC': 10.9,
                'JNJ': -0.06, 'JPM': 10.24, 'MCD': -2.23,
                'MRK': -4.13, 'MSFT': 1.62, 'NKE': 6.5,
                'PFE': 3.25, 'PG': 2.61, 'TRV': 1.16,
                'UTX': 7.54, 'UNH': -5.32, 'VZ': 4.07,
                'V': -0.03, 'WMT': 1.26, 'WBA': 8.97
            }

# Initialize input and error checking variables
valid_length = False
valid_companies = True
valid_input = False
user_input = ""
user_list = []

# Prompt for input until list contains 10 valid companies
while valid_input is False:

    user_input = input("Please enter 10 DJIA companies, separated by spaces: ")
    user_list = user_input.split()

    if len(user_list) is not 10:
        print("You entered an incorrect number of companies. ", end='')
    else:
        valid_length = True

    for i in user_list:
        valid_companies = dow_jones.keys()
        if i not in valid_companies:
            print(i + " is not a DJIA company. ", end='')
            valid_companies = False

    if valid_length and valid_companies:
        break

# Create a portfolio for each of the three investment strategies: hill climbing,
# simulated annealing, and user choice, with an initial investment of $10,000
# in each of the ten companies.
user_portfolio = Portfolio()
hc_portfolio = Portfolio()
sa_portfolio = Portfolio()
initial_investment = 10000

for i in user_list:
    new_node = Node(i, dow_jones.get(i), initial_investment)
    hc_portfolio.add_stock(new_node)
    sa_portfolio.add_stock(new_node)
    user_portfolio.add_stock(new_node)


print("Starting Porfolio:")
user_portfolio.print_contents()
print("\nHill Climbing Portfolio:")
hc_obj = HillClimbing(hc_portfolio)
hc_obj.hill_climbing()
hc_portfolio = hc_obj.best_portfolio
hc_portfolio.print_contents()
print("\nSimulated Annealing Portfolio:")
sa_obj = SimulatedAnnealing(sa_portfolio)
sa_obj.simulated_annealing()
sa_portfolio.print_contents()
