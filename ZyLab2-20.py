#Sydney Ani PID:1869076

# Prompt the user for the amounts of lemon juice, water, and agave nectar
lemon_juice_cups = float(input("Enter amount of lemon juice (in cups):\n"))
water_cups = float(input("Enter amount of water (in cups):\n"))
agave_nectar_cups = float(input("Enter amount of agave nectar (in cups):\n"))

# Prompt the user for the number of servings
servings = float(input("How many servings does this make?\n"))

# Output the ingredients and serving size with two digits after the decimal point
print("\nLemonade ingredients - yields {:.2f} servings".format(servings))
print("{:.2f} cup(s) lemon juice".format(lemon_juice_cups))
print("{:.2f} cup(s) water".format(water_cups))
print("{:.2f} cup(s) agave nectar".format(agave_nectar_cups))

# Prompt the user for the desired number of servings
desired_servings = float(input("\nHow many servings would you like to make?\n"))

# Adjust the amounts of ingredients based on desired servings
lemon_juice_cups *= desired_servings / servings
water_cups *= desired_servings / servings
agave_nectar_cups *= desired_servings / servings

# Output the adjusted ingredients and serving size with two digits after the decimal point
print("\nLemonade ingredients - yields {:.2f} servings".format(desired_servings))
print("{:.2f} cup(s) lemon juice".format(lemon_juice_cups))
print("{:.2f} cup(s) water".format(water_cups))
print("{:.2f} cup(s) agave nectar".format(agave_nectar_cups))

# Convert ingredient measurements to gallons
lemon_juice_gallons = lemon_juice_cups / 16
water_gallons = water_cups / 16
agave_nectar_gallons = agave_nectar_cups / 16

# Output the ingredients and serving size in gallons with two digits after the decimal point
print("\nLemonade ingredients - yields {:.2f} servings".format(desired_servings))
print("{:.2f} gallon(s) lemon juice".format(lemon_juice_gallons))
print("{:.2f} gallon(s) water".format(water_gallons))
print("{:.2f} gallon(s) agave nectar".format(agave_nectar_gallons))
