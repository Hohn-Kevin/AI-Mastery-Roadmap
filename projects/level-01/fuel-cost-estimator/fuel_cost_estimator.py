amount_kilometers = float(input("Enter the distance in kilometers: "))
fuel_efficiency = float(input("Enter the fuel efficiency in liters per 100 kilometers: "))
fuel_cost = float(input("Enter the cost of fuel per liter: "))

fuel_usage = amount_kilometers / 100 * fuel_efficiency
trip_cost = fuel_usage * fuel_cost

print(f"You used {fuel_usage:.2f} L fuel on your Trip.")
print(f"So in summary the trip cost you {trip_cost:.2f} €")