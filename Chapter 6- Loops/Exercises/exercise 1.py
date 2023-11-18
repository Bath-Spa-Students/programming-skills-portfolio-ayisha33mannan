'''Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.'''

#making an empty list
pizza_topping = []
#loop
while True:
    pizza_topping = input("Enter a pizza topping you like (Write 'quit' when you are finished): ") #user will enter topping or quit
    if pizza_topping != "quit":
        print ( "just as you wish" , pizza_topping , "will be added to your pizza!")
    else:
        break
