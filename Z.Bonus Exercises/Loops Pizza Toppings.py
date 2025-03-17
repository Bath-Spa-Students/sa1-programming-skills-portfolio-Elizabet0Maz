# Variable
topings = []
# Variable, input
Toping = input("Enter your Topings for the Pizza ")
# While loop
while Toping != 'quit':
# Variable, input
    Toping = input("Enter your Topings for the Pizza ")
# Adds Toping to the list (Topings)
    topings.append(Toping)
# Else Keyword
else:
# Removes Item from the list
    topings.remove("quit")
# Print Function
    print(topings)
<<<<<<< Updated upstream
# Exit
=======
# Exit 
>>>>>>> Stashed changes
    exit()