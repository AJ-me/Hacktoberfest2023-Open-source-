import math

def basic_calculator(num1, num2, operator):
if operator == "+":
        return num1 + num2
elif operator == "-":
        return num1 - num2
elif operator == "*":
        return num1 * num2
elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"

def advanced_calculator():
    while True:
        print("Select operation:")
        print("1. Basic Calculator")
        print("2. Square root")
        print("3. Exponentiation")
        print("4. Trigonometric functions")
        print("5. Logarithm")
        print("6. Factorial")
        print("7. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

if choice == "7":
            print("Exiting the calculator.")
            break

if choice not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid choice. Please try again.")
            continue

if choice == "1":
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            result = basic_calculator(num1, num2, operator)
            print("Result: ", result)
        elif choice == "2":
            num = float(input("Enter a number: "))
            result = math.sqrt(num)
            print("Square root: ", result)
        elif choice == "3":
            num = float(input("Enter the base: "))
            exponent = float(input("Enter the exponent: "))
            result = math.pow(num, exponent)
            print("Result: ", result)
        elif choice == "4":
            angle = float(input("Enter an angle in degrees: "))
            print("Select trigonometric function:")
            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")
            trig_choice = input("Enter choice (1/2/3): ")
if trig_choice == "1":
                result = math.sin(math.radians(angle))
                print("Sine: ", result)
            elif trig_choice == "2":
                result = math.cos(math.radians(angle))
                print("Cosine: ", result)
            elif trig_choice == "3":
                result = math.tan(math.radians(angle))
                print("Tangent: ", result)
            else:
                print("Invalid choice")
        elif choice == "5":
            num = float(input("Enter a number: "))
            result = math.log(num)
            print("Natural logarithm: ", result)
        elif choice == "6":
            num = int(input("Enter an integer: "))
            result = math.factorial(num)
            print("Factorial: ", result)

if __name__ == "__main":
    advanced_calculator()
