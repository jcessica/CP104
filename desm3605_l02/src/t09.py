"""
------------------------------------------------------------------------
Lab 2, Task 9
------------------------------------------------------------------------
Author: Jessica Desmond
ID:     169033605
Email:  desm3605@mylaurier.ca
__updated__ = "2023-09-19"
------------------------------------------------------------------------
"""

# Imports

# Constants

PI = 3.14


diameter_base = float(input("Diameter of container base (cm): "))

height_cyl = float(input("Height of container (cm): "))

material_cost = float(input("Cost of material ($/cm^2): "))

container_prod = int(input("Number of containers: "))

radius = diameter_base/2

#Base calculation
circular_area = PI*(radius**2)

#Lateral area calculation
rectangular_area = 2*PI*radius*height_cyl

#Surface of the container
surface_cont = circular_area+rectangular_area

#Cost of one container
cost_cont_one = surface_cont*material_cost

#Cost of all containers
cost_cont_all = surface_cont*material_cost*container_prod

print("The total cost of one container is: $",cost_cont_one)
print("The total cost of all containers is: $",cost_cont_all)







