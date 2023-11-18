'''Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all
occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.'''

#list of different options for sandwiches
sandwich_orders = ['pastrami', 'Vegetable', 'grilled cheese', 'pastrami','chicken', 'egg', 'pastrami', 'spicy']
finished_sandwiches = [] #finshed order is empty for now

print("sorry, but pastrami is not available today.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami') #using remove to remove pastrami from list

print("\n")
while sandwich_orders:
    process_sandwich = sandwich_orders.pop()
    print("I'm making " + process_sandwich + " sandwich for you!!.")
    finished_sandwiches.append(process_sandwich) # now empty set is not empty

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich just for you!")
