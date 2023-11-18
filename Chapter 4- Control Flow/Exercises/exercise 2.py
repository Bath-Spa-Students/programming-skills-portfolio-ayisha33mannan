'''Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain.
•If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien.
•If the alien’s color isn’t green, print a statement that the player just earned 10 points.
•Write one version of this program that runs the if block and another that runs the else block.'''

#PROGRAM THAT PASSES
#colour of alien killed will be Green
alien_killed = 'green'
#using if-else statement
#if the alien color is green player wins 5 points
# else player will earn 10 points
if alien_killed == 'green' :
    print ("Yaay! You earned 5 points")
else:
    print ("Bravo! You earned 10 points")

#PROGRAM THAT FAILS
#now colour of alien killed will be yellow
alien_killed = 'yellow'
 #using if-else statement
#if the alien color is green player wins 5 points
# else player will earn 10 points
if alien_killed == 'green' :
    print ("Yaay! you earned 5 points")
else:
    print ("Bravo! you earned 10 points")
