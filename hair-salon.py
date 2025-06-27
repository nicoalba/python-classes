# Datat metrics for hair salon

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

## Find average price for a cut
total_price = [0]

for item in prices:
  total_price.append(item)

average_price = sum(total_price) / len(prices)
print("Average haircut price : " + str(average_price))

## Cut prices by 5
new_prices = [item - 5 for item in prices]
print(new_prices)

## Revenue
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total revenue: "+ str(total_revenue))

## Average daily revenue
average_daily_revenue = total_revenue / 7
print("Average daily revenue: " + str(average_daily_revenue))

## Advertise haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Cuts under $30: " + str(cuts_under_30))
