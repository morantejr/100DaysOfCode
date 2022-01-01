def bandName():
    
    print("Welcome to the Band Name Generator")
    city = input("What\'s the name of the city you were born in:\n")
    print(city)
    pet = input("What\'s your pet\'s name?:\n")
    print(f"Your band name could be {city.title()} {pet.title()}")
    
bandName()
