import math

def sum_num(a, b):
    return a + b

def sub_num(a, b):
    return a - b

def mul_num(a, b):
    return a * b

def div_num(a, b):
    if b != 0:
        return a / b
    else:
        return "Can't divide by zero"

def calc_triangle_area(base, hight):
    return 0.5 * base * hight

def calc_circle_area(radius):
    return math.pi * radius ** 2

def calc_rectangle_area(length, width):
    return length * width

def menu():
    while True:
        print("Main Menu:")
        print("1. Sum")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Division")
        print("5. Calculate triangle area")
        print("6. Calculate circle area")
        print("7. Calculate rectangle area")
        print("8. Exit")

        choice = int(input("Enter your choice (1-8): "))

        if choice == 1:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = sum_num(a, b)
            print("Result: ", result)
        elif choice == 2:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = sub_num(a, b)
            print("Result: ", result)
        elif choice == 3:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = mul_num(a, b)
            print("Result: ", result)
        elif choice == 4:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            result = div_num(a, b)
            print("Result: ", result)
        elif choice == 5:
            base = float(input("Enter the base of the triangle: "))
            hight = float(input("Enter the height of the triangle: "))
            result = calc_triangle_area(base, hight)
            print("Result: ", result,"cm2")
        elif choice == 6:
            radius = float(input("Enter the radius of the circle: "))
            result = calc_circle_area(radius)
            print("Result: ", result,"cm2")
        elif choice == 7:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            result = calc_rectangle_area(length, width)
            print("Result:", result,"cm2")
        elif choice == 8:
            print("Exiting from program")
            break
        else:
            print("Invalid choice, Please try again")
 menu()