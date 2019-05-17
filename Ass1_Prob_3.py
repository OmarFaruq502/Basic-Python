#Assignment 1 problem 3
#Date: 5/17/2019

# Write a program which will find all such numbers which are divisible by 5 but are not a multiple
# of 2 and lie between 1 and 100. The numbers obtained should be printed in a comma-separated
# sequence on a single line.

# Simple solution
print("Numbers are:", end =" ")

for i in range(0,101,5):
    if (i % 2) == 0:
        continue
    else:
        print(str(i) + ",", end= "")