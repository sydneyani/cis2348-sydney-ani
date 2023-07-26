#Sydney Ani PID:1869076

# Prompt the user to input name and age separated by spaces
parts = input().split()

# Extract the name from the input and assign it to the 'name' variable
name = parts[0]

# Enter a loop to process names and ages until the user enters '-1'
while name != '-1':

    try:
        # Try to convert the second element of the input to an integer and add 1 to it
        age = int(parts[1]) + 1

    except ValueError:
        # If the conversion to an integer fails, set 'age' to 0
        age = 0

    # Print the name along with the calculated (or defaulted) age
    print(f'{name} {age}')

    # Prompt the user to input the next name and age
    parts = input().split()

    # Extract the name from the input and update the 'name' variable for the next iteration
    name = parts[0]
