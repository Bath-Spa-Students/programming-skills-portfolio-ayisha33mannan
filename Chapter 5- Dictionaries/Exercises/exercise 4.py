'''Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.'''
#dictionary
#names of river and countries
river_country = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China',
    'Indus': 'Pakistan',
}
#making sentence using dictionary
for river, country in river_country.items():
    print("The river " + river.title() + " flows through " + country.title() + ".")
#names of the rivers only in the dictionary
print("\nThe rivers in this data set are:")
for river in river_country.keys():
    print("-> " + river.title())
#names of countries only in the dictionary
print("\nThe countries in this data set through which the river runs:")
for country in river_country.values():
    print("-> " + country.title())
