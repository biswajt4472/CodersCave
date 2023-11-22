def add(x, y):
    return x + y


def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def Power(x, y):
    return x**y


print("Select operation.")
print("1.Sum")
print("2.Substract")
print("3.Multiply")
print("4.Divide")
print("5.Power")

while True:
    choice = input("Enter choice (1/2/3/4/5): ")
    if choice in ("1", "2", "3", "4","5"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == "1":
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == "2":
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == "3":
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == "4":
            print(f"{num1} / {num2} = {divide(num1, num2)}")
        elif choice == "5":
            print(f"{num1} power {num2}  = {Power(num1,num2)}")
        next_calculation = input("Let's do next calculation? (Yes/No): ")
        if next_calculation == "No":
            break

    else:
        print("Invalid Input")
