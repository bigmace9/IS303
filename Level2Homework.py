# Mason Chandler
# Road Trip Planner (Leve 2 Assignment)


# Input
user_name = input("What's your name? ")
user_destination = input("Where are you traveling to? ")
one_way_miles = float(input("How many miles is that from you, one way? "))
vehicle_miles = int(input("How many miles per gallon does your car get? "))
gas_price = float(input("What is current gas price per gallon? "))
travelers_number = int(input("How many people are coming with you? "))


# Calculations

total_miles = int((one_way_miles *2))
gas_needed = (total_miles/vehicle_miles)
gas_cost = (gas_needed * gas_price)
cost_per_traveler = (gas_cost/travelers_number)


# Output
print("------------------------------------------")
print("Road Trip Planner")
print("------------------------------------------")

print(f"Traveler: {user_name}")
print(f"Destination: {user_destination.upper()}")
print(f"Total Gas Cost: ${gas_cost:.2f}")
print(f"Total Cost per Traveler: ${cost_per_traveler:.2f}")
print("------------------------------------------")
print("Have a great trip!")



