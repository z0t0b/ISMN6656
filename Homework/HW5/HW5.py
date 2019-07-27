# HW5

# initialize blank lists
items = []
prices = []

# get 5 items and prices with for loop
for index in range(5):
   item = input("Item: ")
   price = float(input("Item Price: $"))

   # put input in lists
   items.append(item)
   prices.append(price)

print("\n\n")

# displays all items and prices
for item in items:
   index = items.index(item)
   for _ in prices:
      print("Item: " + item + " Price: $" + str(prices[index]))
      break
