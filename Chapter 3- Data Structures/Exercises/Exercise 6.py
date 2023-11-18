"""You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
•Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
•Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
•Print a message to each of the two people still on your list, letting them know they’re still invited.
•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program."""

#CREATING LIST OF FRIENDS TO INVITE THEM TO DINNER
people_guest =  ["Zara", "Afia", "Lola"]
#inviting them to dinner
name = people_guest[0].title()
print(name + ", I would like to invite you to for dinner at my place" + ".")

name = people_guest[1].title()
print(name + ", I would like to invite you to for dinner at my place" + ".")

name = people_guest[2].title()
print(name + ", I would like to invite you to for dinner at my place" + ".")

#Lola can't make it to dinner
name = people_guest[2].title()
print("\nSorry, " + name + " is busy, she can't make it to dinner" + "." + "\n")

# invite someone else instead
del(people_guest[2])
people_guest.insert(2, 'Lilly')

# inviting people to dinner,
#NEW LIST:
name = people_guest[0].title()
print(name + ", I would like to invite you to for dinner at my place" + ".")

name = people_guest[1].title()
print(name + ", I would like to invite you to for dinner at my place" + ".")

name = people_guest[2].title()
print(name + ", I would like to invite you to for dinner at my place" + ".")

#now conducting a festival
print("\nWe are conducting a festival!! Yaay!!")
#inviting more people
people_guest.insert(0, 'Alia')
people_guest.insert(2, 'Ali')
people_guest.append('Rohan')

# message to all the people that are invited to the festival
name = people_guest[0].title()
print(name + ", I would like to invite you to a festival that we are conducting at our place" + ".")
name = people_guest[1].title()
print(name + ", I would like to invite you to a festival that we are conducting at our place" + ".")
name = people_guest[2].title()
print(name + ", I would like to invite you to a festival that we are conducting at our place" + ".")
name = people_guest[3].title()
print(name + ", I would like to invite you to a festival that we are conducting at our place" + ".")
name = people_guest[4].title()
print(name + ", I would like to invite you to a festival that we are conducting at our place" + ".")
name = people_guest[5].title()
print(name + ", I would like to invite you to a festival that we are conducting at our place" + ".")

# the festival is canceled
# it is raining
#inviting only two people
print("\nSorry, we can not conduct festival at our place" + ". ")

name = people_guest.pop()
print("Sorry, " + name.title() + " " + "The festival is canceled.")

name = people_guest.pop()
print("Sorry, " + name.title() + " " + "The festival is canceled.")

name = people_guest.pop()
print("Sorry, " + name.title() + " " + "The festival is canceled.")

name = people_guest.pop()
print("Sorry, " + name.title() + " " + "The festival is canceled.\n" )

#inviting only two people
name = people_guest[0].title()
print(name + ", I would like to invite you to for dinner at my place" + ".")

name = people_guest[1].title()
print(name + ", I would like to invite you to for dinner at my place" + ".")

# deleting the name
del(people_guest[0])
del(people_guest[0])

# Prove the list is empty.
print ("\nhere is the proof that the list is empty: ")
print(people_guest)
