# P3.40

# get cost input
cost = int(input("Please enter the cost of your groceries: $"))

if(10 <= cost <= 60):
   coupon = 8
elif(60 < cost <= 150):
   coupon = 10
elif(150 < cost <= 210):
   coupon = 12
elif(210 < cost):
   coupon = 14
else:
   coupon = 0

if(coupon == 0):
   print("You do not win a coupon.")
else:
   discount = str(round(cost * (coupon * 0.01), 2))
   print("You win a discount coupon of $" + discount + " (" + str(coupon) + "% of your purchase)")