def celsius_to_fahrenheit(c):
    """Converts Celsius to Fahrenheit."""
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    """Converts Celsius to Kelvin."""
    return c + 273.15

def fahrenheit_to_celsius(f):
    """Converts Fahrenheit to Celsius."""
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    """Converts Fahrenheit to Kelvin."""
    # F -> C -> K
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    """Converts Kelvin to Celsius."""
    return k - 273.15

def kelvin_to_fahrenheit(k):
    """Converts Kelvin to Fahrenheit."""
    # K -> C -> F
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

def main():
    """Main function to run the temperature converter."""
    print("Welcome to the Temperature Converter!")
    print("Scales: C (Celsius), F (Fahrenheit), K (Kelvin)")

    while True:
        try:
            # Get the input value
            value_str = input("\nEnter the temperature value (e.g., 25): ")
            if value_str.lower() == 'quit':
                break
            value = float(value_str)

            # Get the source scale
            from_scale = input("Enter the source scale (C, F, or K): ").upper()

            # Perform the conversions
            if from_scale == 'C':
                f = celsius_to_fahrenheit(value)
                k = celsius_to_kelvin(value)
                print(f"\n{value}°C is equal to:")
                print(f"  {f:.2f}°F (Fahrenheit)")
                print(f"  {k:.2f} K (Kelvin)")
            
            elif from_scale == 'F':
                c = fahrenheit_to_celsius(value)
                k = fahrenheit_to_kelvin(value)
                print(f"\n{value}°F is equal to:")
                print(f"  {c:.2f}°C (Celsius)")
                print(f"  {k:.2f} K (Kelvin)")

            elif from_scale == 'K':
                c = kelvin_to_celsius(value)
                f = kelvin_to_fahrenheit(value)
                print(f"\n{value} K is equal to:")
                print(f"  {c:.2f}°C (Celsius)")
                print(f"  {f:.2f}°F (Fahrenheit)")

            else:
                print("Error: Invalid source scale. Please enter C, F, or K.")

        except ValueError:
            print("Error: Invalid temperature value. Please enter a number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    print("\nThank you for using the Temperature Converter!")

if __name__ == "__main__":
    main()