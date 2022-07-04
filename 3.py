#3. Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

def hundredth_year():

    name=input("enter name")
    age = int(input("enter age"))


    a = 100 - age
    b = 2022 + a

    return (f'{name} will become 100 in the year {b}')

print(hundredth_year())
