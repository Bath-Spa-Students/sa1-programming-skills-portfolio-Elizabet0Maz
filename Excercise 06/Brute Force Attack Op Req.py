# Write a program that simulates a password entry system.
# Variable 
password = "12345"
# Variable and Input
ans = input("Input your password please: ")
# Maximum attempts
attempts = 0
# Limit for attempts
limit = 5
# While loop
while ans != password:  
# Incriment Operator
      attempts = attempts + 1 
# Input for retrying
      ans = input("Wrong please try again! ")
# If Keyword
      if attempts == limit:
# Exit if limit reached.
        exit()
# If keyword 
if ans == password:
# print function
      print("Your password is correct!")
