import datetime as dt
from decimal import Decimal
from random import choice, randint
import custom_module

print(f"Today's date is {dt.date.today()} and the time is {dt.datetime.now().time()}")

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
possible_destinations = ["ibiza", "miami", "santorini"]
travel_destination = choice(possible_destinations)

cost = calculate_time_travel_cost(year)

message = custom_module.generate_time_travel_message(year, travel_destination, cost)

print(message)