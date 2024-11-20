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
# Variable input with int data type
Answer = int(input("Choose The Month (1-12): "))
# if Keyword
if Answer in Months: 
# print Function
    print(Months[Answer])
# Else Keyword
else: 
# Print Function
    print("Month is not found")
    
