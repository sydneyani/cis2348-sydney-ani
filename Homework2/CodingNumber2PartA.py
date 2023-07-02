# Sydney Ani PID: 1869076
# Create a dictionary to store month names and their corresponding numbers
def convert_to_date_string(date_input):
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }
    year = date_input.split(",")[-1].strip()
    month = date_input.split(",")[0].split()[0]
    day = date_input.split(",")[0].split()[-1]
    month_number = months[month]
    return str(month_number) + "/" + day + "/" + year

while True:
    user_input = input()
    if user_input == "-1":
        break  # Exit the loop
    print(convert_to_date_string(user_input))
