# Package weight
weight = 41.5

# Ground shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3 + 20
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4 + 20
elif weight > 10:
  cost_ground = weight * 4.75 + 20

# Premium shipping
cost_premium = 125

# Drone shipping
if weight <= 2:
  cost_drone = weight * 4.50
elif weight > 2 and weight <= 6:
  cost_drone = weight * 9
elif weight > 6 and weight <= 10:
  cost_drone = weight * 12
elif weight > 10:
  cost_drone = weight * 14.25

print("Weight: " + str(weight))
print("Ground shipping: " + str(cost_ground))
print("Premium ground shipping: " + str(cost_premium))
print("Drone shipping: " + str(cost_drone))

# Determine cheapest shipping method

if cost_ground < cost_premium and cost_ground < cost_drone:
  print("Cheapest method: Ground shipping at $" + str(cost_ground))
if cost_premium < cost_ground and cost_premium < cost_drone:
  print("Cheapest method: Premium shipping at $" + str(cost_premium))
else:
  print("Cheapest method: Drone shipping at $" + str(cost_drone))
