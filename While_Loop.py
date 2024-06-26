# Taking number input from the user
number = int(input("Enter a number: "))

# Initializing the counter
i = 1

# While loop to print the multiplication table of entered number
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1