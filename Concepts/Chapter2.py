import math
# veriables and data types

# Python has type inference meaning the programmer dosent
# have to specify the veriable type
a = 30 # integer
b = "harry" # String
c = 88.44 # float

# This is how to see the type of a veriable
print(type(a))

# typecasting is converting one type to another
str(31)  # int to str conversion
int("32") # str to int conversion 
float(32) # int to float conversion

# input function is how you can get input from the keyboard as
# a string
A = input("enter name: ")

print(A)

## Practice Test

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))

total = num1 + num2
print("the sum of the two is", total)

remainder = num1 % num2
print("the remainder of the two is", remainder)

average = (num1 + num2) / 2
print("the average of the two is", average)

square = num1 ** num2
print("the square of num1 to num2 is", square)