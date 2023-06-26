# Sydney Ani PID: 1869076
# Create a dictionary to store month names and their corresponding numbers
month_dict = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
    'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10,
    'November': 11, 'December': 12
}

try:
    # Open a new file called "parsedDates.txt" to store the parsed dates
    with open('parsedDates.txt', 'w') as outFile:

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

                    # Write the parsed date in the output file
                    outFile.write(str(monthNum) + '/' + day + '/' + year + '\n')

except FileNotFoundError:
    # Print an error message if the input file is not found
    print('Error: Unable to find the input file')
