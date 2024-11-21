Salary = int(input("Enter your salary per year : "))
WExperience = float (input("Enter your work Experience in years : "))
if Salary >= 40000:
    if WExperience >= 3:
        print("You are eligible for loan")
    else : 
        print("Unfortunately your work experience is lesser than 3 years therefore you may not get the loan")
else: 
    print("Sorry your Salary is lesser than 40 K")
