'''A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their
age, and then tell them the cost of their movie ticket'''

#user visible
basic = "Please enter your age: "
basic += "\nWrite 'quit' when you are done: "
#loop
while True:
    price_age = input(basic)  #user will write their age
    if price_age == 'quit': #or else quit
        break
    price_age = int( price_age)

    if price_age < 3: #age range 0-2
        print("  You can enjoy without any charges!")
    elif price_age  >= 3 and price_age <= 12:  #age range 3-12
        print("  Your ticket price will be $10.")
    else:    #age range 13 or more
        print("  Your ticket price will be $15.")
