#A string is a piece of information with quotation marks around it.
    #Examples:
pet = "dog"
pet = 'dog'
#Strings can be declared/created by using single or double quotes. They can be many words long, and can have numbers in them. They can even just be numbers.

#Strings can also go across multiple lines of code. These are called multiline strings. They must hace three sets of quotes surrounding them to work.
    #Examples:
string1 = """I am part of a long string.
This is the second line of code.
Look, I can keep going into the third line,
and I am still being assigned
to the same variable."""

string2 = '''I am part of a long string.
This is the second line of code.
Look, I can keep going into the third line,
and I am still being assigned
to the same variable.'''

#Strings can also be called string literals. It's just another way of saying strings, really.


    #String Methods
#Methods are keywords that a program can use to modify data within a variable. To use a method on a variable, you must type the name of the variable and then type a period and the name of the method you want to use. After the method, you must type opening and closing parentheses.
    #Example:
#string1.methodname() 
#This examlpe is commented out as to not cause an error in the program, as the method 'methodname' is not declared in this program.
#Programmers can write their own methods, but python also comes with many prewritten methods.

    #Lower and Upper
#Makes all characters in a string lowercase or uppercase. These functions have no effect on numbers or special characters.
    #Examples:
string1 = "I love Coding!"
print(string1.lower()) #Outputs i love coding!
print(string1.upper()) #Outputs I LOVE CODING!

    #Replace
#Replace changes a specific character, or characters, in the string to something else. You must put something inside the parentheses for this method. The characters in the replace method must be identical to the characters in the string for the method to work correctly.
    #Example:
string1 = "Coding is cool!"
print(string1.replace("cool", "fun"))


    #Strip
#Strip is used to remove excess white space at the beginning or end of a string. This is done by typing .strip() after the name of a string variable.
    #Example:
string1 = " I love Coding! "
print(string1.strip())

    #Indexing
#The index number is a number that says where a character is in a string. Indexing starts counting at zero.
    #Example:
string1 = "Coding is awesome!"
print(string1[5]) #outputs g, the 5th index in the example. C is at index 0.
#Spaces count as characters in indexing.
#You can also cound backwards in the string by using negative indexing.
string1 = "Coding is awesome!"
print(string1[-3]) #outputs m. When indexing from the end you start counting at onem not zero.

    #Slicing
#Slicing uses the indexes to print specific         "slices", or parts, of a string. The first number is the index to start at, and the second number is where to end.
    #Example:
string1 = "I love coding!"
print(string1[4:9]) #outputs ve co. It includes characters 4 UNTIL 9, not including index 9.
#One more thing that can be included in slicing. You can include a third number, which is how many numbers you will skip. The default is one, and that is what the computer will assume if nothing is there.
    #Example:
string1 = "I love coding!"
print(string1[2:9:2]) #outputs lv o. It starts at index 2, ends at index 9, and skips over 2 indexes each time.
#If the first or second section is left blank, it will either go to the beginning or the end of the string.
    #Example:
string1 = "I love coding!"
print(string1[:5]) #outputs I lov. It starts at the beginning of the string, and ends at index 5.

    #Reverse
#To reverse a string, you start slicing at the end and move backwards. This is done by starting at the last index of the string (found easily by typing len(<name of string>) in the first part of a slice), then moving backwards by typing -1 in the third part of a slice. This effectively reverses a string.
    #Example:
string1 = "yodel"
reverse = string1[len(string1)::-1]
print(reverse)

    #Split
#Splitting a string outputs each separate word in a string. This does not include spaces, but rather uses spaces to determine where to split the string.
    #Example:
string1 = "I love spaghetti!"
print(string1.split()) #outputs ['I', 'love', 'spaghetti!']

    #Length
#Finding how many characters are in a string. For this, we start counding at 1. Spaces are included in the total character count.
    #Example:
string1 = "I love spaghetti!"
print(len(string1)) #outputs 17, the length of all characters in the string.

    #Find
#Find returns the index value of a certain character. It goes from start to end to find the first instance of a character in the string.
    #Example:
string1 = "I love Mississippi!"
print(string1.find("s")) #outputs 9, the first instance of the character s in the string.
#You can also use this method to start from the end of a string and look for the first instance of a character from the end. It will still give the index number counting from left to right, beginning with 0, though.
    #Example:
string1 = "I love Mississippi!"
print(string1.rfind("s")) #outputs 13, the first instance of the character s when looking from the end of the string.

    #Checking strings
#Checking a string is simplem, and done using the keyword 'in'.
    #Example:
string1 = "I love Coding!"
check = "love" in string1
print(check) #outputs True, because the string 'love' is present in the larger string 'I love Coding!'
#You can also use the keywords 'not in' to check if something is not in the string.
    #Example:
string1 = "I love Coding!"
check = "love" not in string1
print(check) #outputs False, because the string 'love' is present in the larger string 'I love Coding!'
#Characters in this ARE case sensitive, so you must type exactly what you are looking for.

#This is useful if you want to check if a word or phrase is presend in a string that has hundreds of words, or if you want to check if the user inputs certain words.
