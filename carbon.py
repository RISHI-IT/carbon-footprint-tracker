
import datetime
carbon_factors = {
    "car": 0.271,          
    "bus": 0.103,          
    "train": 0.041,       
    "flight": 0.115,      
    "beef": 27.0,          
    "chicken": 6.9,        
    "vegetables": 2.0,     
    "electricity": 0.45,   
}

def travel_footprint(mode, distance):
    if mode in carbon_factors:
        return distance * carbon_factors[mode]
    else:
        print("Invalid travel mode!")
        return 0

def food_footprint(food_type, quantity):
    if food_type in carbon_factors:
        return quantity * carbon_factors[food_type]
    else:
        print("Invalid food type!")
        return 0

def energy_footprint(electricity_usage):
    return electricity_usage * carbon_factors["electricity"]
def calculate_carbon_footprint():
    print("Welcome to EcoSave: Carbon Footprint Tracker!")
    date = datetime.date.today()
    print(f"Date: {date}")

    print("\n--- Travel Footprint ---")
    mode = input("Enter travel mode (car/bus/train/flight): ").lower()
    distance = float(input(f"Enter distance traveled by {mode} (in km): "))
    travel_emissions = travel_footprint(mode, distance)

    print("\n--- Food Footprint ---")
    food_type = input("Enter food type (beef/chicken/vegetables): ").lower()
    quantity = float(input(f"Enter quantity of {food_type} consumed (in kg): "))
    food_emissions = food_footprint(food_type, quantity)
    
    print("\n--- Energy Footprint ---")
    electricity_usage = float(input("Enter electricity used (in kWh): "))
    energy_emissions = energy_footprint(electricity_usage)
    
    total_emissions = travel_emissions + food_emissions + energy_emissions
    print("\n--- Carbon Footprint Summary ---")
    print(f"Travel Emissions: {travel_emissions:.2f} kg CO2")
    print(f"Food Emissions: {food_emissions:.2f} kg CO2")
    print(f"Energy Emissions: {energy_emissions:.2f} kg CO2")
    print(f"Total Carbon Footprint for {date}: {total_emissions:.2f} kg CO2")
    
    print("\n--- Insights ---")
    if total_emissions > 50:
        print("⚠️ Your carbon footprint is higher than average. Consider reducing travel or using sustainable energy!")
    else:
        print("✅ Great job! Your carbon footprint is within an environmentally-friendly range.")
if __name__ == "__main__":
    calculate_carbon_footprint()