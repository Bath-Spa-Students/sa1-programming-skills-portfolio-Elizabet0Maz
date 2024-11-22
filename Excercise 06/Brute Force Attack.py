# Write a program that simulates a password entry system.
# Variable 
password = "12345"
# Variable and Input
ans = input("Input your password please: ")
# While loop
while ans != password:
# Input for retrying
    ans = input("Wrong please try again! ")
# If keyword 
if ans == password:
# print function
    print("Your password is correct!")
