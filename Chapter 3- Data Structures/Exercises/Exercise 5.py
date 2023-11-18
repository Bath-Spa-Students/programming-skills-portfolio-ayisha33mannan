"""You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations.
You’ll have to think of someone else to invite.
•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of
the guest who can’t make it.
•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
•Print a second set of invitation messages, one for each person who is still in your list."""

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
