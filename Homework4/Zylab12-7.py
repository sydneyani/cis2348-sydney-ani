#Sydney Ani PID: 1869076

# Function to get the user's age from input
def get_age():
    age = int(input())  # Read the age as an integer from the user
    if age < 18 or age > 75:  # Check if the age is outside the valid range
        raise ValueError("Invalid age.")  # Raise an error if the age is not valid
    return age  # Return the valid age

# Function to calculate fat-burning heart rate based on age
def fat_burning_heart_rate(age):
    heart_rate = 0.7 * (220 - age)  # Calculate the fat-burning heart rate using the formula
    return heart_rate  # Return the calculated heart rate

if __name__ == "__main__":
    try:
        print("Please enter your age:")  # Prompt the user to enter their age
        age = get_age()  # Call the get_age() function to get the user's age
        rate = fat_burning_heart_rate(age)  # Call the fat_burning_heart_rate() function with the obtained age
        print(f"Fat burning heart rate for a {age} year-old: {rate} bpm")  # Display the calculated heart rate
    except ValueError as e:  # Handle the ValueError if an invalid age is entered
        print(e)  # Print the error message for an invalid age
        print("Could not calculate heart rate info.")  # Display a message indicating heart rate calculation failure

