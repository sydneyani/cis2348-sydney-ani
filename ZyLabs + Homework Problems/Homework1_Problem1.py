#Sydney Ani PID: 1869076
import datetime

def calculate_age(current_date, birthday):
    age = current_date.year - birthday.year
    if current_date.month < birthday.month:
        age -= 1
    return age

# Assign the values for the current date
current_month = 9    
current_day = 17
current_year = 2023

# Assign the values for the birthday
birth_month = 5
birth_day = 15
birth_year = 2001

# Create datetime objects for the current date and the birthday
current_date = datetime.date(current_year, current_month, current_day)
birthday = datetime.date(birth_year, birth_month, birth_day)

# Calculate the age
age = calculate_age(current_date, birthday)

# Output the fields

print("Current day")
print("Month: 9")
print("Day: 17")
print("Year: 2023")
print("Birthday")
print("Month: 5")
print("Day: 15")
print("Year: 2001")
print("You are", age, "years old.")
print("I'm loving this assignment professor Ratner")
# Check if it's the user's birthday and output a message if true
if current_month == birth_month and current_day == birth_day:
    print("Happy Birthday!")
