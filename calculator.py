def calculator(x: int, y: int, operator: str ) -> str:
    try: 
        match operator:
            case '+':
                result = x + y
            case '-':
                result = x - y
            case '*':
                result = x * y
            case '/': 
                result = x / y
            case _:
                return "Error: Unsupported operator. "
            
        return f"{x} {operator} {y} = {result}"
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed. "


print(calculator(5 , 3, "+"))
print(calculator(5 , 3, "-"))
print(calculator(5 , 3, "*"))
print(calculator(5 , 5, "/"))
