'''Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made,
move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.'''

#list of different options for sandwiches
sandwich_orders = ['Vegetable sandwich', 'grilled cheese sandwich', 'spicy sandwich', 'egg sandwich', 'chicken']
finished_sandwiches = [] #finshed order is empty for now

while sandwich_orders:
    process_sandwich = sandwich_orders.pop()
    print("I'm making "+ process_sandwich + " for you!")
    finished_sandwiches.append(process_sandwich)# now empty set is not empty

print("\n")
for sandwich in finished_sandwiches:
    print("I made a " + sandwich + " sandwich for you!")
