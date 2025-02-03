"""
------------------------------------------------------------------------
Lab 5, Task 3
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-12"
------------------------------------------------------------------------
"""

# Imports

from functions import gym_cost

# Constants

cost = float(input("Enter membership cost: "))

friends = int(input("Enter number of friends: "))

final_cost = gym_cost(cost, friends)

print(f"Your membership cost is: {final_cost:.2f}")

