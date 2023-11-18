'''Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
•If the person is less than 2 years old, print a message that the person is a baby.
•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
•If the person is at least 4 years old but less than 13, print a message that the person is a kid.
•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
•If the person is at least 20 years old but less than 65, print a message that the person is an adult.
•If the person is age 65 or older, print a message that the person is an elder.'''

#set variable (age)
age = 45 #the age of person is 15
if age < 2:     #age less than 2 years old,
    print ("Awww! you are just a baby") #print, person is a baby
elif age >=2 and age < 4 :    #age 2 years old but less than 4
    print ("Guchi guchi goo! you are a toddler")  #print, person is a toddler.
elif age >4 and age < 13:    #age 4 years old but less than 13
    print ("Wow! you are a big kid")    #print, person is a kid.
elif age >= 13 and age < 20 :   #age 13 years old but less than 20
    print ("Not a kid anymore, you're a teenager")   #print, person is a teenager
elif age >= 20 and age < 65 :   #age 20 years old but less than 65
    print ("You're an adult") #print, person is an adult
else:    #age 65 or older
    print ("Ahem Ahem! you are more than 65, you're an elder") #print, person is an elder
