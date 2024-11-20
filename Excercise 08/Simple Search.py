# Write a program that searches for a specific string within a list of strings. 
# The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

# List of the names. 
Names = ["Jake","Zac","Ian","Ron","Sam","Dave"]
# Print Function
print(Names)
# Answer Variable for the input, lower function.
Answer = "Sam"
# if keyword.
if Answer in Names:
# Print Function.
    print(f"Your name is {Answer}")
# Else, Print function.
else: print("Name is not in the List sorry.")
