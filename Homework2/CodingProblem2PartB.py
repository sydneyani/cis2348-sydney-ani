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
 # Open the file "inputDates.txt" to read the dates
        with open('inputDates.txt', 'r') as file:

            # Process each date in the file
            for date in file:

                # Remove any extra spaces or newlines
                date = date.strip()

                # If the date is -1, stop processing
                if date == '-1':
                    break

                    # Find the index of the space after the month name
                monthIndex = date.find(" ")

                # Find the index of the comma followed by a space after the month name
                dayIndex = date[monthIndex + 1:].find(", ")

                # If both indices are valid
                if monthIndex != -1 and dayIndex != -1:
                    # Extract the month name from the date
                    month = date[:monthIndex]

                    # Extract the day from the date
                    day = date[monthIndex + 1:][:dayIndex]

                    # Extract the year from the date
                    year = date[monthIndex + 1:][dayIndex + 2:]

                    # Find the corresponding month number from the month dictionary
                    monthNum = month_dict[month]
