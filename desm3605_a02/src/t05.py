"""
------------------------------------------------------------------------
Assignment 1, Task 5
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-10-05"
------------------------------------------------------------------------
"""
#User input
shed_length = float(input("Foundation length (m): "))

shed_width = float(input("Foundation width (m): "))

shed_height = float(input("Foundation height (m): "))

wall_height = float(input("Wall height (m): "))

cost_conc = float(input("Cost of concrete ($/m^3): "))

cost_brick = float(input("Cost of bricks ($/m^2): "))


#Calculations for printing
found_vol = shed_length * shed_height * shed_width

found_conc = found_vol * cost_conc

brick_count = 2*(wall_height * shed_width) + 2*(wall_height * shed_length)

brick_cost = brick_count * cost_brick

total_cost = brick_cost + found_conc


print()
print()

print(f"Concrete needed for foundation (m^3): {found_vol:.2f}")

print(f"Cost of concrete: ${found_conc:.2f}")

print(f"Bricks needed for walls (m^2): {brick_count:.2f}")

print(f"Cost of bricks: ${brick_cost:.2f}")

print(f"Total cost: ${total_cost:.2f}")






