'''Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different message.'''

#defining function
def make_shirt(size='large', text='I love Python!'): #values set by default
    """The shirt that is going to be made will have"""
    print("\nThe size of my t-shirt will be" , size )
    print('I will print text on it that says, "' , text + '"')

#calling function
make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')
