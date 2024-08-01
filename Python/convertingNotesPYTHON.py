#converting string to integer
cheese = "3"
cheese = int("3")
print(cheese)

#converting float to integer
peppers = 2.8
peppers = int(2.8)
print(peppers)
#when converted to an integer, the decimal is dropped, not rounded.

#converting integer to string
fries = 30
fries = str(30)
print(fries)

#converting integer to float
pizza = 4
pizza = float(4)
print(pizza)

#converting inputs
family = int(input("How many family members do you have? "))
#eventually, create an if-other loop to check the input for an integer, that way your program does not get crashed by a non-integer input being cast as an integer.
baby = family + 1
print(baby)
