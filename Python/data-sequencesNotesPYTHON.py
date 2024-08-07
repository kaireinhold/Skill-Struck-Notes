
    #Lists:
#Lists are ordered and changeable. They allow duplicates.
#Ordered means that the order of the data in thr group matters. These go by index numbers, beginning counting at 0.
#Changeable means that you can switch out the data points in the middle of the list.
    #Example:
friends = ["Kevin", "Lily", "Ajash", "Camilla"]
print(friends)
#If you want to get an output of only one of the data points in the list, you can put brackets and the index number of the data point(s) that you want to print.
    #Example:
friends = ["Kevin", "Lily", "Ajash", "Camilla"]
print(friends[2])
#You can also use the 'slicing' method to output multiple data points in the list, though they work differently with lists than with regular strings.
    #Example:
friends = ["Kevin", "Lily", "Ajash", "Camilla"]
print(friends[1:3]) #This example outputs ['Lily', 'Ajash'], which shows that each data point is treated the same as a single character in a string is.
#Lists can also be used with data types other than strings, for example Integers.
    #Example:
distance = [5, 7, 20, 11, 18]
print(distance)
#It's also possible to mix different data types in the same list.
    #Example:
information = [5, 7, "Ahmed", 9, "Sequoia"]
print(information)
#You can also split up strings into a list of characters by using the list() function.
    #Example:
animal = "giraffe"
mylist = list(animal)
print(mylist)

    #Adding to Lists
#To add to a list in python, you can use many methods. append(), extend(), and insert() are two of these methods.
    
    #append():
#This method is used to add one piece of data to the end of a list.
    #Example:
goats = ["Billy", "Frannie", "Leslie", "Barbara", "Scott"]
goats.append("Molly")
print(goats)
    
    #extend():
#This method is used to combine two lists, adding multiple pieces of data to the end of an already existing list.
    #Example:
goats = ["Billy", "Frannie", "Leslie", "Barbara", "Scott"]
goats.extend(["Janie", "Boulder", "Penelope", "Frank"])
print(goats)
#If you use this method with just a string, it will add each character of the string as a different piece of data.
    #Example:
goats = ["Billy", "Frannie", "Leslie", "Barbara", "Scott"]
goats.extend("Curly")
print(goats)

    #insert():
#This is used to add an item to a list in a specific place.
    #Example:
goats = ["Billy", "Frannie", "Leslie", "Barbara", "Scott"]
goats.insert(2, "Curly")
print(goats)

    #Removing from Lists
#To remove data from a list in Python, you can use the remove() method.
    #Example:
goats = ["Billy", "Frannie", "Leslie", "Barbara", "Scott"]
goats.remove("Frannie")
print(goats)
#If there are multiple of the same element in a list, the remove() method will take out the first element that matches.
    #Example:
goats = ["Billy", "Frannie", "Bob", "Barbara", "Bob", "Scott"]
goats.remove("Bob")
print(goats)

    #Return a Value
#If you want to remove an item from a list, but still have it available to use, you can use the pop() method.
    #Example:
goats = ["Billy", "Frannie", "Braden", "Barbara", "Scott"]
favorite = goats.pop(3)
print(favorite + " is my favorite goat")
print(goats)

    #Ranges:
#Ranges are used to return a certain output from a sequence using index numbers. Ranges can also be used by themselves to return numbers. Unless you specify otherwise, ranges always start counting and returning outputs from 0.
    #Example:
smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies"]
print(smells[2:5])

    #Tuples:
#Tuples are unordered and unchangeable. They allow duplicates.

   #Dictionaries:
#Dictionaries are unordered, but changeable and indexed. They do not allow duplicates.

    #For Loops
#A for loop is used to address each piece of data in a sequence.
#It is a way to repeat a block of code multiple times, hence why it is called a 'loop'.
    #Example of Basic Structure: (commented out as to not give an error when the code is run)
sequence = ["a", "b", "c", "d"]
for item in sequence:
    #do something with your item
    #'item' is a variable that takes the value of each element in the sequence, one at a time. This can be called anything, but it is important that it makes sense for your loop and is not too long.
    #'sequence' is the collection of items that you want to iterate over. This would be the name of your variable.
    #List Example:
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number) #this will print '1 2 3 4 5' (each number on a separate line)
    #'numbers' is the list that we want to iterate over
    #'number' is the variable that takes each value from the list, one at a time.

    #String Example:
string = "hello world"
for char_ in string:
    print(char_) #this will print each character in the string that is assigned to the variable 'string' on a separate line, similarly to the list example.

    #Range Example:
for i in range(5):
    print(i) #This prints each integer in the range from 0 up until 5. So, it will print '0 1 2 3 4' on a separate line each.
#You can perform some actions for each element in that sequence, too. This can be used with if-elif-else loops inside of your for loop
    #Example:
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number == 0:
        print(f"{number} is zero")
    elif number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")
#You can also use this to handle different types of data in a list.
    #Example:
elements = [1, "hello", 3.5, True, None, [1, 2, 3], {"key": "value"}]
for element in elements:
    if isinstance(element, bool):
        print(f"{element} is a boolean")
    elif isinstance(element, int):
        print(f"{element} is an integer")
    elif isinstance(element, str):
        print(f"{element} is a string")
    elif isinstance(element, float):
        print(f"{element} is a float")
    elif element is None:
        print(f"{element} is a NoneType")
    elif isinstance(element, list):
        print(f"{element} is a list")
    elif isinstance(element, dict):
        print(f"{element} is a dictionary")
    else:
        print(f"{element} is of an unknown type")

    #Check IF something is IN or NOT IN a sequence
    #Example 1:
lucky_list = ["horseshoe", "clover", "rabbit foot", "socks"]
if "clover" in lucky_list:
    print("clover is in lucky_list")

    #Example 2:
lucky_list = ["horseshoe", "clover", "rabbit foot", "socks"]
if "hat" not in lucky_list:
    print("hat is not in lucky_list")
