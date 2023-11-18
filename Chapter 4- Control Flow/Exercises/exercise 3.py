'''Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
•    If the alien is green, print a message that the player earned 5 points.
•    If the alien is yellow, print a message that the player earned 10 points.
•    If the alien is red, print a message that the player earned 15 points.
•    Write three versions of this program, making sure each message is printed for the appropriate color alien.'''

#PROGRAM THAT PASSES
#colour of alien killed will be Green
killed_alien = 'yellow'
#using if-elif-else statement
if killed_alien == 'green':
    print ("Yaay! You earned 5 points")  #if the color of alien killed is green player wins 5 points
elif killed_alien == 'yellow':
    print ("Bravo! You earned 10 points") #if the color of alien killed is yellow player wins 10 pounts
else:
    print ("Excellent! You earned 15 points" )  #if the color of alien killed is red player wins 15 points
