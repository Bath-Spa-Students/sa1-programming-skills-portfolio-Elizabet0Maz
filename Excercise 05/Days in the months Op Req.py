# Write a program that tells a user how many days there are in a specific month.
# Dictionary
Months = {1 : 31,
          2 : 28,
          3 : 31,
          4 : 30,
          5 : 31,
          6 : 30,
          7 : 31, 
          8 : 31,
          9 : 30,
          10 : 31,
          11 : 30,
          12 : 31}
# Variable input
Leap = input("Is it a Leap year? (yes/no): ")
# if function
if Leap == "yes" or Leap == "y":
# 2nd Month changes
    Months[2] = 29
# Variable, input with int data type
Answer = int(input("Choose The Month (1-12): "))
# if Keyword
if Answer in Months: 
# Print function
    print(Months[Answer])
# Else Function
else: 
# Print Function
<<<<<<< Updated upstream
    print("Month is not found")
=======
    print("Month is not found")
>>>>>>> Stashed changes
