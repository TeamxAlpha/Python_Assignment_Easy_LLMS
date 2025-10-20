def temperature_converter(temperature, unit):
    if unit.lower() == "celsius":
        fahrenheit = (temperature * 9/5) + 32
        return f"{fahrenheit} Fahrenheit"
    elif unit.lower() == "fahrenheit":
        celsius = (temperature - 32) * 5/9
        return f"{celsius} Celsius"
    else:
        return "Error: Unsupported unit."

# Example
print(temperature_converter(25, "Celsius"))  # Output: 77.0 Fahrenheit
