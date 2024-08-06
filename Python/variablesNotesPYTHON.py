#namesakes have to be kept the same for each iteration of every variable.
#Variable names can have capital A-Z, lowercase a-z, 0-9, and _. Nothing else, not even spaces.
#Variables can be assigned to a new string after created.
    #Example: 
number = 10
print(number)
number = 50
print(number)

#You can also type "multiple words" long variable names.
    #Examples:
what_goes_up_when_rain_comes_down = "Umbrellas"
what_is_full_of_holes_but_holds_water = "Sponge"
what_can_you_not_keep_until_you_give_it = "Friendship"

print(what_goes_up_when_rain_comes_down)
print(what_is_full_of_holes_but_holds_water)
print(what_can_you_not_keep_until_you_give_it)

    #Examples of variable types:
    #String
name1 = "Kai"
print(name1)
    #Integer
num1 = 23
print(num1)
    #Boolean
bool1 = True
print(bool1)

    #Updating Variables using For Loops (See data-sequencesNotesPYTHON.py first for explanation of what For Loops are.) 
#You can use For Loops to update a variable with each iteration of the loop.
    #Example:
my_list = [2, 5, 8, 10]
total = 0
for x in my_list:
    total = total + x
print(total)
