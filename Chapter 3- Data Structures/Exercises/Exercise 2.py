'''Start with the list you used in Exercise 1, but instead of just printing each person’s name, print a message to them.
The text of each message should be the same, but each message should be
personalized with the person’s name.'''

# creating a variable (name) and creating list of my friends
Names = ["Zainab", "Sundas" , "Aisha" , "Attia"]
# printing each persons name at a time
# with a personalised message
personalized_message = Names[1].title() + " you are my best friend" + "."
print (personalized_message)
personalized_message = Names[2].title() + " you are weird, but sweet" + "."
print (personalized_message)
personalized_message = Names[0].title() + "," + " i really like you" + "!"
print (personalized_message)
personalized_message = Names[3].title() + "," + " you are THE BEST" + "."
print (personalized_message)
