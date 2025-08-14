import datetime as dt
from decimal import Decimal
from random import choice, randint
import custom_module

now = dt.datetime.now()
print(f"Today's date is {now.date()} and the time is {now.strftime('%H:%M:%S')}")

# Base cost for travel using decimal module
base_cost = Decimal('1000.00')

# Function to calculate cost of time travel
def calculate_time_travel_cost(year):
  current_year = dt.date.today().year
  year_difference = abs(current_year - year)
  cost_multiplier = Decimal(year_difference * 100)
  final_cost = base_cost + cost_multiplier
  return final_cost

year = randint(1900,2200)
possible_destinations = ["Ibiza", "Miami", "Santorini", "Mykonos"]
travel_destination = choice(possible_destinations)

cost = calculate_time_travel_cost(year)

try:
  message = custom_module.generate_time_travel_message(year, travel_destination, cost)
  print(message)
except Exception as e:
  print(f"An error occured: {e}")
