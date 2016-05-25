"""Area.py 

Simplistic menu driven area calculator.
Using just basic types, conditionals, while loop.

Author: Super Kid
Date: 2016-ish.
"""
print("Welcome to Area Calculator")
print("------- -- ---- ----------")
print("\n")
    
while True:
    menu_choice = 0
    answer = 0.0
    # User Input Stage
    while menu_choice<1 or menu_choice>4:
        print("Please select your shape:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Triangle")
        menu_choice = int(input("Enter choice 1-4 or press CTRL-C to quit: "))

    if menu_choice==1:
        print("You have selected: Square")
        length = float(input("Please enter the side length: "))
        answer = length**2
    elif menu_choice==2:
        print("You have selected: Rectangle")
        length = float(input("Please enter the length: "))
        breadth = float(input("Please enter the breadth: "))
        answer = length*breadth
    elif menu_choice==3:
        print("You have selected: Circle")
        radius = float(input("Please enter the radiua: "))
        answer = 3.14*radius**2
    else:
        print("You have selected: Triangle")
        base = float(input("Please enter the base length: "))
        height = float(input("Please enter the height: "))
        answer = 0.5*base*height

    print("\n")
    print("*"*50)
    print("Thank you. Your required area is", answer, "square units")
    print("*"*50)
    print("\n")


