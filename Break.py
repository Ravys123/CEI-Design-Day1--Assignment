#  Create a program that stops printing numbers when it encounters a number greater than 5 using the break statement. 

for i in range(1,10):
    # Checks if the number is greater than 5 and stop printing the numbers after 5 
    if i > 5:
        break
    print(i)