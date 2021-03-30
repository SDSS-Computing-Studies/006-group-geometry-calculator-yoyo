#!python3
# Volume Calculator
# Feel free to rename your variables

import math

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    print("=============Title Screen============")

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    print("Calculate Area of Rectangle --- 1")
    print("Calculate Area of Circle --- 2")
    print("Calculate Perimeter of Triangle --- 3")
    print("Calculate Perimeter of Regular Polygon --- 4")
    print("Calculate Surface Area of Cube --- 5")
    print("Calculate Surface Area of Cylinder --- 6")
    print("Calculate Volume of Sphere --- 7")
    print("Calculate Volume of Cone --- 8")
    print("Exit --- 9")
    print("=================================")


def getParams(shape):
    # Will create a list of questions to be asked depending on the shape.
    # These will be asked so that the user can enter in appropriate values
    # input parameter: string 
    # output parameter: return a list containing the prompts for each shape:
    # example: ["Enter the radius:","Enter the slant height:","Enter the height:"]
    prompts = []
    if shape == "Rectangle":
        prompts.append(("Enter the Width of Rectangle, must be an integer:"))
        prompts.append(("Enter the Height of Rectangle, must be an integer:"))
    elif shape == "Circle":
        prompts.append(("Enter the radius of Circle, must be an integer:"))
    elif shape == "Triangle":
        prompts.append(("Enter the First Side Length of Triangle, must be an integer:"))
        prompts.append(("Enter the Second Side Length of Triangle, must be an integer:"))
        prompts.append(("Enter the Third Side Length of Triangle, must be an integer:"))
    elif shape == "Regular Polygon":
        prompts.append(("Enter the Number of Sides of Regular Polygon, must be an integer:"))
        prompts.append(("Enter the Sides Length of Regular Polygon, must be an integer"))
    elif shape == "Cube":
        prompts.append(("Enter the Side Length of Cube, must be an integer:"))
    elif shape == "Cylinder":
        prompts.append(("Enter the Height of Cylinder, must be an integer:"))
        prompts.append(("Enter the Radius of Cylinder, must be an integer:"))
    elif shape == "Sphere":
        prompts.append(("Enter the Radius of Sphere, must be an integer:"))
    elif shape == "Cone":
        prompts.append(("Enter the Radius of Cone, must be an integer:"))
        prompts.append(("Enter the Height of Cone, must be an integer:"))
    

    return prompts

def getInputs(questions):
    # Will prompt the user for inputs for the shape they.
    # These will be asked so that the user can enter in appropriate values
    # It will turn all the input data into a list
    # input parameter: list containing the prompts/questions
    # output parameter: return a list containing all the measurements of the shape
    measurements = []
    for q in questions:
        measurements.append(int(input(q)))
    
    return measurements

def rectangle_area(l):
    print("Area of Rectangle is :" , end = "")
    return l[0] * l[1]

def circle_area(l):
    print("Area of Circle is :" , end = "")
    return math.pi * math.pow(l[0], 2)

def triangle_perimeter(l):
    print("Perimeter of Triangle is :" , end = "")
    return l[0] + l[1] + l[2]

def regular_polygon_perimeter(l):
    print("Perimeter of Regular Polygon is :" , end = "")
    return l[0] * l[1]

def cube_surface_area(l):
    print("Surface Area of Cube is :" , end = "")
    return l[0]^2 * 6

def cylinder_surface_area(l):
    print("Surface Area  of Cylinder is :" , end = "")
    return circle_area([l[1]]) * 2 + l[0] * l[1] * 2 * math.pi

def sphere_volume(l):
    print("Volume of Sphere is :" , end = "")
    return 3/4 * math.pi * math.pow(l[0], 3)

def cone_volume(l):
    print("Volume of Cone is :" , end = "")
    return circle_area([l[0]]) * l[1] * 1/3

def main():
    # main block of code that will run your program and control program flow
    # You will need to include a while loop to keep repeating the commands until
    # the user chooses to exit
    shape_list = ["Rectangle", "Circle", "Triangle", "Regular Polygon", "Cube", "Cylinder", "Sphere", "Cone"]
    title()
    instructions()
    option = int(input())
    while option != 9:
        shape = shape_list[option - 1]
        input_list = getInputs(getParams(shape))
        if option == 1:
            print(rectangle_area(input_list))
        elif option == 2:
            print(circle_area(input_list))
        elif option == 3:
            print(triangle_perimeter(input_list))
        elif option == 4:
            print(regular_polygon_perimeter(input_list))
        elif option == 5:
            print(cube_surface_area(input_list))
        elif option == 6:
            print(cylinder_surface_area(input_list))
        elif option == 7:
            print(sphere_volume(input_list))
        elif option == 8:
            print(cone_volume(input_list))
        title()
        instructions()
        option = int(input())
main()
