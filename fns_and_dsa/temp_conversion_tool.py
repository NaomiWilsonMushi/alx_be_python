
# Conversion factors for Fahrenheit <-> Celsius
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Main interaction with the user
try:
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    
    # Decide which conversion to use
    if unit.upper() == "F":
        print(convert_to_celsius(temp))
    elif unit.upper() == "C":
        print(convert_to_fahrenheit(temp))
    else:
        raise ValueError
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")