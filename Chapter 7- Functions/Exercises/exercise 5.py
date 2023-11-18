'''Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence,
such as Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the default country.'''

#defining function
def describe_city(city, country='UAE'):
    """Describing a city and specifying its country"""
    text = city.title() + " is a beautiful city in " + country.title() + "."
    print(text)
#displaying the countries and their cities
describe_city('Fujairah')
describe_city('reykjavik', 'iceland')
describe_city('Dubai')
