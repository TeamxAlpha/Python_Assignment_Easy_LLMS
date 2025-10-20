def calculator():
    x = float(input("Enter Firist Number:"))
    y = float(input("Enter Second Number: "))
    op = input("Enterr Operator (+, -, *, /): ")

    if op == '+':
        print(f"{x} + {y} = {x + y}")
    elif op == '-':
        print(f"{x} - {y} = {x - y}")
    elif op == '*':
        print(f"{x} * {y} = {x * y}")
    elif op == '/':
        if y == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print(f"{x} / {y} = {x / y}")
    
    else:
        print("Error: Unsupported operator.")   

if __name__ == "__main__":
    calculator()

