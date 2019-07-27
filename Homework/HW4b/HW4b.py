# P3.37

# initialize variables
option = 1

# get checking and savings balances
checkBalance = float(input("Please enter the initial checking account balance: $"))
savBalance = float(input("Please enter the initial savings account balance: $"))

# loops until the above two values are not negative
while(checkBalance < 0 or savBalance < 0):
   print("\nPlease enter non-negative values!")
   
   # get checking and savings balances
   checkBalance = float(input("Please enter the initial checking account balance: $"))
   savBalance = float(input("Please enter the initial savings account balance: $"))

# loops while option is not = to any value other than 1 - 3
while(option != 0 and 0 < option <= 3):  
   # print menu and checking/savings balances
   print("\n############################# MENU #############################")
   print("Checking Amount: $" + str(checkBalance) + "\nSavings Amount: $" + str(savBalance))
   print("1 = deposit, 2 = withdrawal, 3 = transfer, 0 = quit")
   option = int(input("Please enter your transaction option: "))
   
   # validate that option is a value between 1 - 3
   if(option != 0 and 0 < option <= 3):
      choice = int(input("Please enter 1 for checking or 2 for savings: "))
   
   # deposit implementation
   if(option == 1):
      # validate that choice is either 1 or 2
      if(choice == 1 or choice == 2):
         deposit = float(input("Please enter the amount to deposit: $"))
      
      # catches negative or 0 value for deposit amount
      while(deposit <= 0):
         deposit = float(input("No negative amounts! Please enter the amount to deposit: $"))
      
      # deposit in checking
      if(choice == 1):
         checkBalance += deposit
         print("$" + str(round(deposit, 2)) + " was successfully deposited in your checking account!")
      # deposit in savings
      elif(choice == 2):
         savBalance += deposit
         print("$" + str(round(deposit, 2)) + " was successfully deposited in your savings account!")
      # choice is not 1 or 2
      else:
         print("Please enter 1 or 2!")
   
   # withdrawal implementation
   elif(option == 2):
      # validate that choice is either 1 or 2
      if(choice == 1 or choice == 2):
         withdrawal = float(input("Please enter the amount to withdraw: $"))
      
      # catches negative or 0 value for withdrawal amount
      while(withdrawal <= 0):
         withdrawal = float(input("No negative amounts! Please enter the amount to withdraw: $"))
         
      # verify that withdrawal amt is not greater than amount in desired account
      if((choice == 1 and withdrawal > checkBalance) or (choice == 2 and withdrawal > savBalance)):
         print("Insufficient funds!")
      # withdraw from checking
      elif(choice == 1):
         checkBalance -= withdrawal
         print("$" + str(round(withdrawal, 2)) + " was successfully withdrawn from your checking account!")
      # withdraw from savings
      elif(choice == 2):
         savBalance -= withdrawal
         print("$" + str(round(withdrawal, 2)) + " was successfully withdrawn from your savings account!")
      # choice is not 1 or 2
      else:
         print("Please enter 1 or 2!")
      
   # transfer implementation
   elif(option == 3):
      # validate that choice is either 1 or 2
      if(choice == 1 or choice == 2):
         transfer = float(input("Please enter the amount to transfer: $"))
      
      # catches negative or 0 value for transfer amount
      while(transfer <= 0):
         transfer = float(input("No negative amounts! Please enter the amount to transfer: $"))
      
      # verify that transfer amt is not greater than amount in desired account
      if((choice == 1 and transfer > checkBalance) or (choice == 2 and transfer > savBalance)):
         print("Insufficient funds!")
      # transfer from checking to savings
      elif(choice == 1):
         checkBalance -= transfer
         savBalance += transfer
         print("$" + str(round(transfer, 2)) + " was transferred from checking to savings!")         
      # transfer from savings to checking
      elif(choice == 2):
         savBalance -= transfer
         checkBalance += transfer
         print("$" + str(round(transfer, 2)) + " was transferred from savings to checking!")
      # choice is not 1 or 2
      else:
         print("Please enter 1 or 2!")
      
   # 0 or other number was entered   
   else:
      print("\n\nTerminating application...")

