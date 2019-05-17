# Assignment 1 problem 2
# Date: 5/17/2019

# Given a binary string as input, composed of 0’s and 1’s, give the decimal value for the input.
# Make sure to validate the input before doing any calculation.

print("Enter a Binary Number: ")

binary = input()

# converts each string input in integers and then converts into a list
arr = [int(x) for x in binary]

arr.reverse()

decimal = 0
for i in range(len(arr)):
    decimal = decimal + arr[i] * pow(2 , i)

print("Decimal number for Binary input is: " + str(decimal))
