'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
For this exercise, we will keep track of when our friend’s birthdays are, and be able to find that information based on their name.
Create a dictionary (in your file) of names and birthdays.
When you run your program it should ask the user to enter a name, and return the birthday of that person back to them.
The interaction should look something like this: >>> Welcome to the birthday dictionary.
We know the birthdays of: Albert Einstein Benjamin Franklin Ada Lovelace >>>
Who's birthday do you want to look up? Benjamin Franklin >>> Benjamin Franklin's birthday is 01/17/170
'''


def friend():
    print(
        " Welcome to the birthday dictionary. We know the birthdays of: \n Albert Einstein \n Benjamin Franklin\n  Ada Lovelace\n")
    print()
    name = input("Who's birthday do you want to look up?")
    # name.capitalize()
    brth = {"Albert Einstein": "12/03/2012", "Benjamin Franklin": "30/04/2008", "Ada Lovelace": "05/06/2015"}
    a = brth[name]
    print(f"{name}'s birthday is on {a}")


friend()

