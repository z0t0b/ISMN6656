# R4.1a
# get input number and set new values to placeholder values
n = int(input("a. Please enter the desired number: "))
i = 0
square = 0

# tell user that all squares less than entered number will be displayed
print("All squares less than your entered number are:")

# loops until squared number would be >= n
while (square < n):
   square = i**2
   if(square < n):
      print(str(square))
   i += 1

#######################################################################

# R4.1b
# get input number and set new values to placeholder values
n = int(input("\nb. Please enter the desired number: "))
i = 10

# tell user that all positive numbers divisible by 10 and less than the
# entered number will be displayed
print("All positive numbers that are divisible by 10 and less than your entered number are:")

# loops until number is greater than given number
while (i < n):
   print(i)
   i += 10
   
#######################################################################

# R4.1c
# get input number and set new values to placeholder values
n = int(input("\nc. Please enter the desired number: "))
i = 1
powers = 1

# tell user that all powers of two less than entered number will be displayed
print("All powers of 2 that are less than your entered number are:")

# loops until number is greater than given number
while (i < n):
   print(i)
   i = 2**powers
   powers += 1