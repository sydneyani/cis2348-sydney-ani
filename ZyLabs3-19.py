#Sydney Ani PID:1869076

import math

# Prompt the user to input the wall's height and width
height = float(input('Enter wall height (feet):\n'))
width = float(input('Enter wall width (feet):\n'))

# Calculate the area of the wall
area = height * width
# Calculate the paint needed
paint_needed = area / 350
# Using the ceil function round off the number of cans needed to a whole number
cans = int(math.ceil(paint_needed))

# Display the result
print('Wall area: ' + str(int(round(area))) + ' square feet')
print('Paint needed: %.2f gallons' % paint_needed)
print('Cans needed: ' + str(cans) + ' can(s)')

# Prompt the user to choose a color to paint the wall
print('\nChoose a color to paint the wall:')

color = input()

# Calculate and display the cost of the paint
if color == 'red':
    cost = 35 * cans
elif color == 'blue':
    cost = 25 * cans
elif color == 'green':
    cost = 23 * cans
else:
    cost = 0
print('Cost of purchasing ' + color + ' paint: $' + str(cost))
