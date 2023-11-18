'''Tidy up the code to make it easier to understand
Use a variable to represent a person’s name, and include some whitespace characters at the beginning 
and end of the name. Make sure you use each character combination, “\t” and “\n”, at least once.
Print the name once, so the whitespace around the name is displayed. 
Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip('''
 
 #step1: creat a variable and assign a string. print it
note ="\tAyisha\n"
print("Name with whitespace characters:", note)
#step2: print the variable using stripping functions, lstrip(), rstrip(), and strip(
# using lstrip() function (removes whitespace from left)
note = note.lstrip()
print("Name after lstrip() function:", note)
# using rstrip() function (removes whitespace from right)
note = note.rstrip()
print("Name after rstrip() function:", note)
# using strip() function (removes whitespace from both end)
note = note.strip()
print("Name after strip() function:", note)
