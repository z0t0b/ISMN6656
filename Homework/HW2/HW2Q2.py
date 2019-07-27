# Question 3, HW2
# The item prices are extreme for the given items, but it is assumed they are bought in bulk

# item definitions
item1 = "Noodles"
item2 = "Juice"
item3 = "Soda"
item4 = "Chocolate"
item5 = "Chips"

# item prices (in the same order as the above definitions)
price1 = float(300)
price2 = float(500)
price3 = float(600)
price4 = float(400)
price5 = float(200)

# assign value to subtotal variable
subtotal = float(price1 + price2 + price3 + price4 + price5)

# assign value to salesTax variable
salesTax = 0.07 * subtotal

# assign value to total variable
total = subtotal + salesTax

# dummy value for amount customer pays
customerPaid = 0

# executes until customer pays amount >= total
while (customerPaid < total):
   print("The total is: $" + str(total))
   customerPaid = float(input("Please input the amount to pay: $"))
   if (customerPaid < total):
      print("Please input a number larger than the total price!\n")
      
# assign change value
change = customerPaid - total

# print receipt header
print("\n\nSAMPLE RECEIPT\n5 ITEMS PURCHASED\n")

# print items and prices
print("%-10s %50s" % (item1, "$" + str(price1)))
print("%-10s %50s" % (item2, "$" + str(price2)))
print("%-10s %50s" % (item3, "$" + str(price3)))
print("%-10s %50s" % (item4, "$" + str(price4)))
print("%-10s %50s\n" % (item5, "$" + str(price5)))

# print subtotal, tax, and total
print("%-10s %50s" % ("Subtotal", "$" + str(subtotal)))
print("%-10s %50s" % ("Tax - 7%", "$" + str(salesTax)))
print("%-10s %50s\n" % ("Total", "$" + str(total)))

# print amount customer paid and change to customer, if any
print("%61s" % ("Customer Paid       $" + str(customerPaid)))
print("%61s\n\n\n" % ("Change to customer, if any         $" + str(change)))