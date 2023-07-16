#Sydney Ani PID: 1869076

# Get the input list of integers
input_list = input().split()

# Convert the input values to integers
input_list = [int(x) for x in input_list]

# Filter out the non-negative integers
non_negative_integers = [x for x in input_list if x >= 0]

# Sort the non-negative integers in ascending order
non_negative_integers.sort()

# Print the sorted non-negative integers
for num in non_negative_integers:
    print(num, end=' ')
