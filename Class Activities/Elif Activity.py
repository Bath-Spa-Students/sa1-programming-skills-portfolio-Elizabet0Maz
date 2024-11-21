# Elif Practice
# Variable 1
C = int(input("Please input your first number: "))
# Variable 2
B = int(input("Please input your second number: "))

# If two numbers equal to each other display both
if C == B:
    print(C, B)
# If Second Variable is greater than the first one subtract first from second
elif B > C:
    print(B - C)
# Else add Second variable with the first variable
else: 
    print(B + C)
