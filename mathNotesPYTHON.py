#addition: c = a + b
#subtraction: c = a - b
#multiplication: c = a * b
#division: c = a / b

#Examples:
#math operations with two variables
number_spiders = 10
number_legs = 8

total_legs = number_spiders * number_legs
print(total_legs) #output is 80'

#math operations inside print statement
number_butterflies = 25
print(number_butterflies + 15) #output is 40

#When dividing integers, you always get returned a float data type.
#Example:
bees = 16
flowers = 2
answer = bees / flowers
print(answer) #outputs 8.0, a float, even though the number is an even 8.

#You can print equations as well, but if something is being multiplied by parentheses make sure to put an asterik between the integer and the parentheses.
#Example:
print((3 * 5) * 4 + 9 - 5 * (4 - 3))

#Modulus
#The "percent sign" is called Modulus in python. It is used to return the remainder values between two numbers being divided.
#Examples:
fruits = 10 % 3
print(fruits)

number = 245
print(number % 2) #this returns a 1, which shows us that the variable number is assigned to an odd integer. If it were to return a 0, then we would know that the variable number is assigned to an even integer. This only works when using modulus with 2.
#Anything that returns a 0, we know that it is divided into a whole number by the input after the modulus.

#Modulus can also be used to find the last two numbers in a 3 digit number.
#Example:
number = 245
print(number % 100) #this prints the last two digits of 245.
