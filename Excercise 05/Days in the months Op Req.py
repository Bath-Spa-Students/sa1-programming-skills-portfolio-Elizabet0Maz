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
Leap = input("Is it a Leap year? (yes/no): ")
if Leap == "yes" or Leap == "y":
    Months[2] = 29
Answer = int(input("Choose The Month (1-12): "))
if Answer in Months: 
    print(Months[Answer])
else: 
    print("Month is not found")