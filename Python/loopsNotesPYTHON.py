    #If Statements
#If statements are used to tell the program "if x occurs, do y"
#If statements start with the keyword "if", followed by a condition, and ending with a colon.
#After the colon, the next line is indented. This indicates to the program that if the conditions are met, the indented code is to be executed.
    #Example: (commented out to prevent errors if this program is run)
#if [condition]:
    #[other code to be run]
#Indenting is very important in Python. If your code is not properly indented, it will not run correctly and may even give you an error.
    #Comparison Operators
#A condition compares values using a comparison operator. Comparison operators are:
    #Greater than: >
    #Greater than or equal to: >=
    #Less than: <
    #Less than or equal to: <=
    #Equal to: ==
    #Not equal to: !=
#The greater than and less than operators are used for numbers only, but the equal to and not equal to operators can be used for numbers and strings.
    #Example:
Frank_age = 23
Bob_age = 40
if Bob_age > Frank_age:
    print("Bob is older than Frank")

    #Else statements
#an else statement will catch everything that is not included in the If statement.
    #Example:
Janet_age = 16
Eva_age = 5
if Eva_age > Janet_age:
    print("Eva is older than Janet.")
else:
    print("Eva is younger than Janet.")

    #'=' Sign Usage
#A single '=' sign is used to declare a variable. A double '=' sign is used to check if a variable is the same as something.
    #Example:
Name = input("What is your name? ")
change = input("Would you like to change your name? ")
if change == "Yes":
    Name = input("What is your new name? ")
    print("Your name is now " + Name + "!")
else:
    print("Your name is " + Name + "!")
#See how '==' can be used to test user input? This is very useful in heavily user-input based programs.
#You can also use '==' to check if two variables are the same.
    #Example:
friend_pet = "poodle"
your_pet = "fish"
if friend_pet == your_pet:
    print("You and your friend have the same pet!")
else:
    print("You and your friend have different pets.")
#You can also check if two values are not equal using '!='.
    #Example:
friend_pet = "poodle"
your_pet = "fish"

if friend_pet != your_pet:
    print("You and your friends have different pets!")
else:
    print("You and your friend have the same pet!")

    #And Condition
#If you want to check if two different conditions are BOTH true, you can combine two condition statements by using 'and'. 
    #Example:
your_pet = "gerbil"
your_need = "exercise"
if your_pet == "dog" and your_need == "animal companion":
    print("You are allowed to bring your pet inside the store.")
else:
    print("You cannot bring your pet inside the store.")

    #Or Condition
#If you want to check if one of multiple conditions are true, then you can do so by using 'or'.
    #Example:
your_pet = "gerbil"
if your_pet == "fish" or your_pet == "reptile":
    print("You are allowed to bring your pet inside the classroom.")
else:
    print("You cannot bring your pet inside the classroom.")

    #Else If statements
#Else If statements are used to combine multiple if statements. When you do this, you can add an Else if statement. Else if is shortened to elif.
    #Example:
price = 10
your_cash = 8

if your_cash > price:
    print("You have MORE than enough money to buy it.")
elif your_cash == price:
    print("You have exactly enough money to buy it.")
else:
    print("You do not have enough money to buy it.")
#You can also use multiple elif statements.
vacation = "mountains"
if vacation == "beach":
    print("You love the ocean")
elif vacation == "amusement park":
    print("You love to ride roller coasters")
elif vacation == "mountains":
    print("You love to get up and get away")
else:
    print("You like unique vacation destinations")

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
