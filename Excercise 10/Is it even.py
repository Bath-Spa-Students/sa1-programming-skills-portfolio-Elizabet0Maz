#Write a program that tests if a value is even or odd.
#Function Header
def h(Number): #Parameter
# If keyword
    if Number == 0:
# Print keyword
        print("it's 0\ntry again")
# Calls Main to start the input
        main()
# Checks if Number is odd or even 
    Number = Number % 2
# If number 
    if Number == 0:
# Returns Number from function
        return("Your number is even")
# Keywords Else and Return
    else: return("Your number is odd")
# Funtion Header
def main(): #Void Function
# Input Keyword
    Number = int(input("Please input the number: "))
# Print h funtion
    print(h(Number)) #Parameter
# Starts the Code by Running Main
main()
