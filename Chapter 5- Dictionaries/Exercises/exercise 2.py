'''A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
* Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store
their meanings as values.
* Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print
the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between '''

#glossary with 5 programming words and their meanings.
glossary = {
    'string': 'A string is a series of characters.',
    'comment': 'Comment is a note in a program that helps the person and is ignored by the Python interpreter',
    'list': 'List is a collection of items in a particular order, enclosed in [].',
    'sort': 'Sort is used to arrange and reorder items based on certain criteria.',
    'variable': 'A variable is a memory location, used to store values',
    }
#calling each of them by print

programming_words = 'string'
print("\n" + programming_words.title() + ": " + glossary[programming_words])
programming_words = 'comment'
print("\n" + programming_words.title() + ": " + glossary[programming_words])
programming_words = 'list'
print("\n" + programming_words.title() + ": " + glossary[programming_words])
programming_words = 'sort'
print("\n" + programming_words.title() + ": " + glossary[programming_words])
programming_words = 'variable'
print("\n" + programming_words.title() + ": " + glossary[programming_words])
