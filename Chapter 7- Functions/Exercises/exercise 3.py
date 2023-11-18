'''Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function
should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional
arguments to make a shirt. Call the function a second time using keyword arguments.'''

#defining function
def make_shirt(size, text):
    """The shirt that is going to be made will have"""
    print("\nThe size of my t-shirt will be" , size )
    print('I will print text on it that says, "' , text + '"')

make_shirt('small', 'Everyday is MANGO-nificent') #calling function once using positional arguments (size, text)
make_shirt(text="Dream Don't Work Unless You Do", size='large')  #calling function once using keyword arguments
