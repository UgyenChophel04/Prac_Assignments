# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Main function
def main():
    # Example usage
    celsius_temperature = 25
    fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
    print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")

    fahrenheit_temperature = 77
    celsius_temperature = fahrenheit_to_celsius(fahrenheit_temperature)
    print(f"{fahrenheit_temperature} degrees Fahrenheit is equal to {celsius_temperature} degrees Celsius.")


# Execute the main function
if __name__ == "__main__":
    main()
