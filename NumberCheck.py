#  Write a Python program that takes an integer input from the user and prints 
# #whether the number is positive, negative, or zero

number = int(input("Enter an number to check whether the number is positive, negative or zero : "))

if number > 0 :
    print(f"The number you enter {number} is a Positive Number")
elif number < 0:
    print(f"The number you enter {number} is a Negative Number")
else:
    print(f"The number you enter {number} is Zero")