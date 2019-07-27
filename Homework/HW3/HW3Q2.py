# P3.29

# starting value so while loop executes
value = 0

while(value == 0):
   # get input for month
   month = int(input("Please enter the desired month (1 = January, 2 = February, etc): "))

   if(month in [1, 3, 5, 7, 8, 10, 12]):
      days = "31"
      value = 1 # terminate loop
   elif(month in [4, 6, 9, 11]):
      days = "30"
      value = 1 # terminate loop
   elif(month == 2):
      days = "28 or 29 days"
      value = 1 # terminate loop
   else:
      # error message, loop restarts
      print("Please enter a number from 1 to 12!\n")

# final print statement
print("The number of days in your chosen month is " + days)