# R4.2a
# default values
x = 2
sumEven = 0

# stores each even number in x and total sum in SumEven; includes 2 & 100
while (x <= 100):
   sumEven += x
   x += 2

# print sum
print("a. The sum of all even numbers between 2 and 100 (inclusive) is: " + str(sumEven))

#######################################################################

# R4.2b
# default values
i = 1
sumSquares = 0
square = 0

# stores each square in square variable, and total in sumSquares; includes 1 & 100
while (square < 100):
   sumSquares += square
   square = i**2
   i += 1

# print sum
print("b. The sum of all squares between 1 and 100 (inclusive) is: " + str(sumSquares))

#######################################################################

# R4.2c
# default values
sum = 0
odd = 1

# gets user input for a and b
a = int(input("Please enter a value for a: "))
b = int(input("Please enter a value for b: "))

# if a is even, odd is the next number above it; if not, odd is a
if (a % 2 == 0):
   odd = a + 1
else:
   odd = a

# adds each odd number between a and b (including a and b) to a sum
while (odd <= b):
   sum += odd
   odd += 2

# print sum
print("c. The sum of all odd numbers between " + str(a) + " and " + str(b) + " (inclusive) is: " + str(sum))

#######################################################################

# R4.2d
# default values
sum = 0
val = 0

# gets user input for n
n = int(input("Please enter a value for n: "))

# gets each individual number in given number and adds each odd number to a sum
for d in str(n):
   val = int(d)
   if (val % 2 != 0):
      sum += val
      
# print sum
print("d. The sum of all odd digits of " + str(n) + " is: " + str(sum))