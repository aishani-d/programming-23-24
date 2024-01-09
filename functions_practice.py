# Functions Practice
# Author: Aishani
# 24 Nov 2023

def print_area_of_a_square(sidelength: float) -> None:
    """Calculates the area of a square.
    Results are in units squared.
    
    Params:
    sidelength - length of one side of the square"""
    
    area = sidelength**2
    
    print(
        f"The area of a square with side length = {sidelength} is: {area} square units"
    )
    

def area_of_a_square(sidelength: float) -> float:
    """Returns the area of a square with given
    sidelength
    
    Params:
    sidelength - length of one side of a square
    """
    
    area = sidelength**2
    return area

def stars(num_stars: int) -> str:
    """"""
    return
stars(2)  #   **
stars(10)  #   **********
print_area_of_a_square(12.2)
print_area_of_a_square(13)
# sum_areas = area_of_a_square(12.2) + area_of_a_square(13)
print(area_of_a_square(2))
print(print_area_of_a_square(2))

# Stars Function
def stars(num_stars: int) -> str:
    """"Returns a string of stars given length"""
    return "*" * num_stars

print(stars(5))
print(stars(100))

# Biggest Number Function
def biggest_number(number1: int, number2: int, number3: int) -> None:
    """Finds the biggest number out of the three
    Result is an integer.
    Params:
    number1 - the first number
    number2 - the second number
    number3 - the third number
    """
    if number1 > number2 and number1 > number3:
        maxnumber = number1
    elif number2 > number1 and number2 > number3:
        maxnumber = number2
    else:
        maxnumber = number3
    print(maxnumber)
biggest_number(3,77,17)

# Pyramid Function
def pyramid(num_layers: int) -> None:
    """Prints out a pyramid of given number of layers
    
    Params:
    num_layers - number of layers in the pyramid
    """
    for current_layer in range(1, num_layers + 1):
        print(stars(current_layer))

# Mirrored Pyramid  
def pyramid_mirror(num_layers: int) -> None:
    """"Print a pyramid mirrored of given number of layers.
    
    Params:
    num_layers - number of layers in the pyramid
    """
    
	for current_layer in range(1, num_layers+1):
        # Spaces is equal to total number of layers minus the stars in the current layer
		spaces = " " * (num_layers - current_layer)
        
		print(spaces + stars(current_layer))
              
pyramid_mirror(2)
pyramid_mirror(3)
pyramid_mirror(20)