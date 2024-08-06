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
