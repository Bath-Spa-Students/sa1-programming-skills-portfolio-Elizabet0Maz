for loop in range(3):
    print("bye bye")
for numbers in range(3):
    print(numbers)

    password = "SecretWord"
guess = input("Input your password please: ")
while guess != password:  
  guess = input("Wrong password please try to input it again: ") 
print("Access Granted")
