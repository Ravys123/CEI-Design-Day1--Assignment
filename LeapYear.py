# Taking year input from the user
year = int(input("Enter a year to check whether leap year or not : "))

# Checks whether entered year is a leap year or not 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")