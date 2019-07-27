# P2.11
def main():
	# typecast number of gallons input as int, since the input should be an integer
	input1 = int(input("Please input the number of gallons of gas in the tank: "))
	# typecast fuel efficiency input as int, since the input should be an integer
	input2 = int(input("Please input the fuel efficiency in miles per gallon: "))
	# typecast price as float, since the input should be a monetary value
	input3 = float(input("Please input the price of gas per gallon: "))

	# calculations for cost per 100 miles and the distance left in the trip
	cost_per_100_miles = float((100 / input2) * input3)
	distance_left = str(input1 * input2)

	# round so the number looks like a cash value
	cost_per_100_miles = str(round(cost_per_100_miles, 2))

	# print the values to the screen
	print("\nThe number of gallons of gas in the tank is " + str(input1) + ".")
	print("The fuel efficiency of the vehicle (in miles per gallon) is " + str(input2) + ".")
	print("The price of gas per gallon is $" + str(input3) + ".\n")
	print("Therefore, the cost per 100 miles is $" + cost_per_100_miles + " and the distance left in the trip is " + distance_left + " miles.\n")


# main declaration, so the program runs
main()