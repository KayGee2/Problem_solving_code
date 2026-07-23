print("Welcome to the South African Fuel Calculator⛽")
kilometers = float(input("Enter the number of kilometers: "))
petrol_price = float(input("Enter current petrol prices: "))

liters_per_kilometer = kilometers / 10 
total_petrol_cost = liters_per_kilometer * petrol_price

print(f"Total cost of petrol needed for {float(kilometers)}km: R{round(total_petrol_cost, 2)}")

print("Thank you for using the South African Fuel Calculator. Please drive safely !! 🚗💨")