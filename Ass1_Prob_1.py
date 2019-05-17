# Assignment 1 problem 1
# Date: 5/17/2019

# Getting two intergers from the user

input_1 = int(input("Enter number 1: "))
input_2 = int(input("Enter number 2: "))

# average = (number 1 + number 2)/2
average = (input_1 + input_2) / 2

print("Average for inputs is " + str(int(average))) #using str() for explicit conversion

if input_1 > input_2:
    print("number 1 is maximum")
    print("number 2 is minimum")
else:
    print("number 2 is maximum")
    print("number 1 is minimum")