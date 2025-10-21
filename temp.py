def temperature_converter(temperature: float, unit: str) -> str:

    try:
        unit_lower = unit.lower()
        
        match unit_lower:
            case "celsius":
                result = (temperature * 9 / 5) + 32
                result = round(result, 2)
                return f"{result} Fahrenheit"
            case "fahrenheit":
                result = (temperature - 32) * 5 / 9
                result = round(result, 2)
                return f"{result} Celsius"
            
            case _:
                return "Error: Unsupported unit. Use 'Celsius' or 'Fahrenheit'."
    
    except (TypeError, ValueError):
        return "Error: Invalid input. Please provide a number for temp."



print(temperature_converter(25, "Celsius")) 
print(temperature_converter(77, "Fahrenheit"))  

