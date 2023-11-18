'''A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants
 as many as she can get for £50. They are £6 each.
Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
You will to use the arithmetic operators to complete this exercise.'''
# variable to show the cost of USB
cost = 6
# variable to show the budget 
money = 50
#calcutaion for how many USB she can buy
USB = money / cost 
#calcilating the remaining money 
cash = money - (USB * cost)
#now print 
print( "The number of USB sticks she can buy is: " , str(USB) )
print(str(cash), "is the remaining amount left")
