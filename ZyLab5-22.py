#Sydney Ani PID:1869076

# Automotive services menu and corresponding costs (THIS IS CASE SENSITIVE)
services = {
    "Oil change": 35,
    "Tire rotation": 19,
    "Car wash": 7,
    "Car wax": 12,
}

# Display the menu of automotive services and costs
print("Davy's auto shop services")
for service, cost in services.items():
    print(service + " -- $" + str(cost))

# Prompt the user for two services
print("\nSelect first service:")
service1 = input()
print("Select second service:")
service2 = input()

# Output the invoice for the selected services
print("\nDavy's auto shop invoice\n")
if service1 == "-":
    print("Service 1: No service")
else:
    print("Service 1: " + service1 + ", $" + str(services.get(service1, 0)))

if service2 == "-":
    print("Service 2: No service")
else:
    print("Service 2: " + service2 + ", $" + str(services.get(service2, 0)))

# Calculate the total cost
total_cost = services.get(service1, 0) + services.get(service2, 0)
print("\nTotal: $" + str(total_cost))
