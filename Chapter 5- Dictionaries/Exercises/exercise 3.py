'''Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms
to your glossary.When you run your program again, these new words and meanings should automatically be included in the output.'''

#glossary with 10 programming words and their meanings.
glossary = {
    'string': 'A string is a series of characters.',
    'comment': 'Comment is a note in a program that helps the person and is ignored by the Python interpreter',
    'list': 'List is a collection of items in a particular order, enclosed in [].',
    'sort': 'Sort is used to arrange and reorder items based on certain criteria.',
    'variable': 'A variable is a memory location, used to store values',
    'loop': 'A control stream explanation for executing a block of code over and over until a specific condition is met.',
    'value': 'An item associated with a key in a dictionary.',
    'boolean expression': 'An expression that evaluates to True or False.',
    'float': 'A numerical value with a decimal component.',
    'function': 'A block of coordinated, reusable code that plays out a particular errand.',
    }
#calling each by loop

for word_meaning, definition in glossary.items():
    print("\n" + word_meaning.title() + ": " + definition)
