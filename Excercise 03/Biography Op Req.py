# Create a program that stores and prints your name, home-town, and age to the console using a Python dictionary.
# def Function
def main():
# Variable, and Input
    Name = input("Please input your name: ")
# Variavle, and Input
    Home = input("Please input your Home-Town: ")
# Try-Except function
    try: 
        Age = int(input("Please input your Age: "))
    except ValueError:
        print("Error")
        main()


    # Dictionary
    Dictionary = {"Name" : Name,
                "Home-Town" :  Home,
                "Age" : Age}
    # Print Function
    print("Name:", Dictionary["Name"], "\nHome-Town:", Dictionary["Home-Town"], "\nAge:", Dictionary["Age"])
# calling main
main()