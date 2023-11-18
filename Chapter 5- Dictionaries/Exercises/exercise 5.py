e of animal': 'fish',
    'name': 'Mimi',
    'Favourite food ': 'dead rabits',
    'weight in kg': 43 ,
    'owner': 'Rahul',
}
pets.append(pet_info)

pet_info = {
    'animal type': 'bird',
    'name': 'Flock',
    'weight in kg': 20 ,
    'Favourite food ': 'worms only',
    'owner' : 'Rehman',
}
pets.append(pet_info)

pet_info = {
    'animal type': 'dog',
    'name': 'Frank',
    'weight in kg': 89,
    'Favourite food ': 'human flesh with bones',
    'owner': 'Lola',
}
pets.append(pet_info)

# printing information
for pet in pets:
    print("\nPet information about " + pet_info['name'].title() + ":")
    for key, value in pet_info.items():
        print("\t" + key + ": " + str(value))
