#Integers: whole positive or negative numbers
characters = 10
#Booleans: positive or negative numbers with one or more decimal places.
time = 10.2

    #Concatenating Numbers
#When trying to concatenate numbers, you have to convert the variable to a string instead of an integer or a float, or use the format method. This is because the program does not know whether or not you want to use + as a concatenation symbol or as an addition symbol.
    #Incorrect Example: (commented out because it throws an error)
#string1 = "The number of miles we've hiked totals up to " #string variable
#miles = 21 #int variable
#string2 = string1 + miles
#print(string2) #this outputs an error, because of the above reasons.

    #Format
#The format method will change integer variables to be outputted as a string within string variables.
#Strings that you want to use with the format method must have curly brackets "{}" inside the string for format to work. Format will look for those curly brackets and replace them with the newly formatted variable.
    #Example:
string1 = "The number of miles we've hiked totals up to {}"
miles = 21
print(string1.format(miles))
#You can also used multiple integers inside the format method.
    #Example:
string1 = "The number of miles we've hiked totals up to {}, which is {} feet."
miles = 21
feet = 110880
print(string1.format(miles, feet))
#The variables will always replace the curly brackets in the same order they appear in the format method unless you specify otherwise.
    #Format by Index
#If you ever need to specify the order in which you want variables to fill in curly brackets in a string, you can do this by using index numbers inside of the curly brackets. Remember that indexes start counting from 0.
    #Example:
string1 = "The total number of miles we hiked is {1}. We saw {0} deer."
miles = 21
animals = 20
print(string1.format(animals, miles))
