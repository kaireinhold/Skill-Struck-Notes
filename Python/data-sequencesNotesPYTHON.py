
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
    #Step:
#A step is used in a range to skip over values. The assumed value of a step is 1, which will print every value. 2 skips over every other value, and so on.
    #Example:
smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies"]
print(smells[0:6:2])
    #Replacement:
#You can replace an item in a list with something new using the index value.
    #Example:
smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies"]
smells[3] = "perfume"
print(smells)
    #Length
#You can find out how many items are in a list using len(<listName>). Length starts counting from 1, differently to indexes and ranges.
    #Example:
smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies"]
print(len(smells))
    #Sorting:
#Sorting lists is very simple using the sort() method. You can sort alphabetically, numerically, and in reverse.
    #Alphabetically Example:
smells = ["skunk", "lilac", "rain", "ocean", "garbage", "cleaner", "cookies"]
smells.sort()
print(smells)
    #Numerically Example:
cookies = [3, 55, 9, 12, 13]
cookies.sort()
print(cookies)
    #Reverse Example:
#This reverses the order in which the lists are sorted.
cookies = [3, 55, 9, 12, 13]
cookies.sort(reverse=True)
print(cookies)

    #Tuples:
#Tuples are unordered and unchangeable. They allow duplicates.

   #Dictionaries:
#Dictionaries are unordered, but changeable and indexed. They do not allow duplicates.
