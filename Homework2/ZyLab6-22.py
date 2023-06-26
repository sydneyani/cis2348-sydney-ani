# Sydney Ani PID: 1869076
# Coefficients of the equations
a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())

# Brute force search
for x in range(-10, 11):
    for y in range(-10, 11):
        if a1 * x + b1 * y == c1 and a2 * x + b2 * y == c2:
            print(x, y)
            exit()

# If no solution is found
print("No solution")
