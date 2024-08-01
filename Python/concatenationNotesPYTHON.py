#Concatenation does not add spaces! Make sure to add spaces in your strings, or add a space to be concatenated if you are concatenating multiple variables and/or strings.

#Incorrect example:
string1 = "Paragliding is"
string2 = "daring"
string3 = string1 + string2
print(string3) #outputs "Paragliding isdaring".

#Correct examples:
#1
string1 = "Paragliding is"
string2 = "daring"
string3 = string1 + " " + string2 #this line of code combines two string variables and an unassigned string.
print(string3) #outputs "Paragliding is daring".
#2
string1 = "Paragliding is "
string2 = "daring"
string3 = string1 + string2 
print(string3) #outputs "Paragliding is daring"
#Example 2 also works the other way around, as in placing the space in string2 before daring (" daring") insteadd of placing it in string1 after Paragliding is ("Paragliding is ").

#Concatenating integers.
#Concatenation can only be performed with strings. If you have an integer, it must first be converted to a string to be concatenated with anything.

#Incorrect example:
age = 12
#print("You are " + age + " years old.")
#this will return the error: TypeError: can only concatenate str (not "int") to str.

#Correct example:
age = 12
print("You are " + str(age) + " years old.")
