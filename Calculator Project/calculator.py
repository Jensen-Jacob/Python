from art import logo
print(logo)

# Add function
def add(a, b):
  return a + b

# Subtract function
def subtract(a, b):
  return a - b

# Multiply function
def multiply(a, b):
  return a * b

# Divide function
def divide(a, b):
  return a / b

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

continue_calculation = False

print("Welcome to the calculator!")

first_number = 0
second_number = 0

def calculator():
    global continue_calculation
    global first_number
    global second_number
    while True:
        try:
            if not continue_calculation:
                first_number = float(input("What's the first number? "))
            second_number = float(input("What's the second number? "))
            break
        except:
            print("Invalid input! Try again")
    print("What operation do you want to perform?")
    while True:
        try:
            for key in operations:
                print(key)
            choice = input("Enter operation: ")
            if choice in operations:
                result = operations[choice](first_number, second_number)
                print(f"{first_number} {choice} {second_number} = {result}")
            else:
                raise Exception()
            break
        except:
            print(f"'{choice}' is not a valid operation! Please try again")
    while True:
        try:
            continue_calculation_choice = input(f"Type 'y' to continue calculation with {result} or 'n' to start a new calculation: ")
            if continue_calculation_choice == "y":
                continue_calculation = True
                first_number = result
                break
            else:
                first_number = 0
                second_number = 0
        except:
            print("Invalid input! Try again.")
    calculator()
    
calculator()