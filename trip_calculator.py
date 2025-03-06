def calculate_fuel_needed(distance_km, consumption_rate=5):  
    if distance_km < 0 or consumption_rate <= 0:
        raise ValueError("Distance and consumption rate must be positive.")
    return (distance_km * consumption_rate) / 100

def calculate_trip_cost(distance_km, fuel_price_per_liter):
    if fuel_price_per_liter < 0:
        raise ValueError("Fuel price must be positive.")
    fuel_needed = calculate_fuel_needed(distance_km)
    return fuel_needed * fuel_price_per_liter

if __name__ == "__main__":
    try:
        distance = float(input("Enter distance to travel (in km): "))
        fuel_price = float(input("Enter fuel price per liter: "))
        total_cost = calculate_trip_cost(distance, fuel_price)
        print(f"The total cost of the trip is: ${total_cost:.2f}")
    except ValueError as e:
        print(f"Invalid input: {e}")